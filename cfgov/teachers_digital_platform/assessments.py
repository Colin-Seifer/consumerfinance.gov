import csv
import hashlib
import json
from os.path import dirname
from typing import Any, Dict, List, Tuple

from django import forms

from .forms import AssessmentForm, markup
from .TemplateField import TemplateField


PREFILL_ANSWERS = False

AVAILABLE_ASSESSMENTS = ('3-5', '6-8', '9-12')


def _question_row(row: Dict[str, str]):
    return {
        'q': row['Question'],
        's': row['Section'],
        'pt': row['Part'],
        'pg': row['Page'],
        'a': row['Answer type'],
        'w': row['Answer worth'],
    }


def _answer_types_row(row: Dict[str, str]):
    return {
        'k': row['Key'],
        'c': row['Choices'],
    }


class ChoiceList:
    """
    To save mem, we'll only need a few of these objects in practice
    """

    def __init__(self, labels: List[str]):
        self.labels = labels
        self.choices = tuple(
            (str(k), v) for k, v in enumerate(labels)
        )

    @staticmethod
    def from_string(s: str):
        labels = list(x.strip() for x in s.split('|'))
        return ChoiceList(labels)


choice_lists: Dict[str, ChoiceList] = {}


class Question:
    """
    Base question
    """

    def __init__(self, num: int, part: str):
        self.key = f'q{num}'
        self.num = num
        self.part = part

    def get_score(self, answer):
        return 0

    def get_field(self):
        return None


class ChoiceQuestion(Question):
    """
    Choice question
    """

    def __init__(self, num: int, part: str, label: str,
                 choice_list: ChoiceList, answer_values: List[float]):
        super().__init__(num, part)
        self.choice_list = choice_list
        self.label = label
        self.answer_values = answer_values

    def get_choices(self) -> Tuple[Tuple[str, str], ...]:
        return self.choice_list.choices

    def get_score(self, answer) -> float:
        answer = int(answer)
        assert answer >= 0
        assert answer < len(self.choice_list.labels)
        return self.answer_values[answer]

    def get_field(self):
        label = ''.join([
            markup('<strong class="question-num">'),
            str(self.num),
            '.',
            markup('</strong>'),
            ' ',
            self.label,
        ])

        initial = None
        if PREFILL_ANSWERS:
            initial = self.answer_values.index(max(self.answer_values))

        return {
            'key': self.key,
            'field': forms.ChoiceField(
                widget=forms.RadioSelect({
                    'class': 'ChoiceField'
                }),
                choices=self.choice_list.choices,
                label=label,
                required=True,
                initial=initial,
            ),
        }


class AssessmentPage:
    """
    Page of an assessment
    """

    def __init__(self, heading: str, questions: List[Question]):
        self.heading = heading
        self.questions = questions

    def get_fields(self, prefix_tpls: Dict[str, str]):
        fields = {}

        for question in self.questions:
            if question.key in prefix_tpls:
                fields[f'before_{question.key}'] = TemplateField(
                    prefix_tpls[question.key])

            obj = question.get_field()
            fields[obj['key']] = obj['field']

        return fields

    def get_score(self, all_cleaned_data):
        total = 0
        question_scores = {}

        for question in self.questions:
            answer = all_cleaned_data[question.key]
            score = question.get_score(answer)
            total += score
            question_scores[question] = score

        return {
            'total': total,
            'question_scores': question_scores,
        }

    def get_form_class(self, name: str, prefix_tpls: Dict[str, str]):
        return type(
            name,
            (AssessmentForm,),
            self.get_fields(prefix_tpls),
        )


class Assessment:
    """
    A full assessment
    """

    def __init__(self, key: str, meta: Dict[str, Any],
                 pages: List[AssessmentPage]):
        self.key = key
        self.meta = meta
        self.pages = pages

    def num_questions_by_page(self) -> List[int]:
        return list(len(page.questions) for page in self.pages)

    def get_score(self, all_cleaned_data) -> float:
        total = 0
        question_scores = {}
        page_scores = {}

        for page in self.pages:
            score = page.get_score(all_cleaned_data)
            subtotal = score['total']
            page_scores[page] = subtotal
            question_scores.update(score['question_scores'])
            total += subtotal

        return {
            'question_scores': question_scores,
            'page_scores': page_scores,
            'total': total,
        }

    def get_score_multiplier(self) -> float:
        if 'score_multiplier' in self.meta:
            return self.meta['score_multiplier']
        return 1

    def get_form_list(self):
        page_classes = []

        for page_i, page in enumerate(self.pages):
            name = f'p{page_i + 1}'

            # Unique class name for each assessment + page (not technically
            # required but feels safer)
            hash = hashlib.md5((self.key + '|' + name).encode())
            classname = 'FormPage' + hash.hexdigest()

            page_classes.append((name, page.get_form_class(
                classname, self.meta['prefix_tpls'])))

        return tuple(page_classes)

    @staticmethod
    def setup_choices():
        if len(choice_lists) > 0:
            return
        path = f'{dirname(__file__)}/assessment-data/answer-types.csv'
        with open(path, encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in (_answer_types_row(row) for row in reader):
                choice_lists[row['k']] = ChoiceList.from_string(row['c'])

    @staticmethod
    def factory(key: str):
        """Build an assessment from CSV"""
        assert key in AVAILABLE_ASSESSMENTS

        Assessment.setup_choices()

        q = 1
        last_page = None
        pages: List[AssessmentPage] = []
        questions: List[Question] = []

        def end_page(last_page: str):
            page = AssessmentPage(f'Page {last_page}', questions.copy())
            pages.append(page)
            questions.clear()

        path = f'{dirname(__file__)}/assessment-data/{key}.csv'
        with open(path, encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in (_question_row(row) for row in reader):
                if last_page is None:
                    last_page = row['pg']
                if row['pg'] != last_page:
                    end_page(last_page)

                last_page = row['pg']

                values = list(int(x.strip()) for x in row['w'].split(' '))
                if row['a'] not in choice_lists:
                    msg = f'Unknown answer type {row["a"]}'
                    raise NameError(msg)

                question = ChoiceQuestion(
                    q, row['pt'], row['q'], choice_lists[row['a']], values)
                questions.append(question)
                q += 1
        end_page(last_page)

        path = f'{dirname(__file__)}/assessment-data/{key}-meta.json'
        with open(path) as json_file:
            meta = json.load(json_file)

        return Assessment(key, meta, pages)


def get_assessment(key) -> Assessment:
    assert key in AVAILABLE_ASSESSMENTS
    return Assessment.factory(key)
