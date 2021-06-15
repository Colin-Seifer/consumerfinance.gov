from typing import Dict, List, Tuple

from django import forms
from os.path import dirname

from django.forms import widgets

from .TemplateField import TemplateField

import hashlib
import json


class ChoiceList:
    """
    To save mem, we'll only need a couple of these objects in practice
    """

    def __init__(self, labels: List[str]):
        self.labels = labels
        self.choices = tuple(
            (str(k), v) for k, v in enumerate(labels)
        )


class Question:
    """
    Base question
    """

    def __init__(self, key: str):
        self.key = key

    def get_score(self):
        return 0

    def get_field(self):
        return None


class ChoiceQuestion(Question):
    """
    Choice question
    """

    def __init__(self, key: str, label: str, choice_list: ChoiceList, answer_values: List[float]):
        super().__init__(key)
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
        return {
            'key': self.key,
            'field': forms.ChoiceField(
                widget=forms.RadioSelect,
                choices=self.choice_list.choices,
                label=self.label,
                required=True,
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

        for question in self.questions:
            answer = all_cleaned_data[question.key]
            total += question.get_score(answer)

        return {
            'total': total,
        }

    def get_form_class(self, name: str, inserted_key_field: str, prefix_tpls: Dict[str, str]):
        fields = self.get_fields(prefix_tpls)

        # Put a hidden "_k" field in the form to tell the Assessment
        # wizard can figure out what assessment it's working with
        # We pull this from initial data so there's no way the client
        # can edit this.
        if inserted_key_field != '':
            fields['_k'] = forms.CharField(
                widget=forms.HiddenInput,
                initial=inserted_key_field,
                disabled=True,
            )

        return type(
            name,
            (forms.Form,),
            fields,
        )


class Assessment:
    """
    A full assessment
    """

    def __init__(self, key: str, pages: List[AssessmentPage], prefix_tpls: Dict[str, str]):
        self.key = key
        self.pages = pages
        self.prefix_tpls = prefix_tpls

    def get_score(self, all_cleaned_data) -> float:
        subtotals: List[float] = []
        total = 0

        for page in self.pages:
            subtotal = page.get_score(all_cleaned_data)['total']
            total += subtotal
            subtotals.append(subtotal)

        return {
            'subtotals': subtotals,
            'total': total,
        }

    def get_form_list(self, assessment_key: str):
        page_classes = []

        for page_i, page in enumerate(self.pages):
            name = 'page' + str(page_i + 1)
            inserted_key_field = self.key if page_i == 0 else ''

            # Unique class name for each assessment + page (not technically
            # required but feels safer)
            hash = hashlib.md5((assessment_key + '|' + name).encode())
            classname = 'FormPage' + hash.hexdigest()

            page_classes.append((name, page.get_form_class(
                classname, inserted_key_field, self.prefix_tpls)))

        return tuple(page_classes)

    @staticmethod
    def factory(key: str):
        assert key in available_assessments

        path = f'{dirname(__file__)}/assessment-data/{key}.json'
        print(f'Reading {path} ...')
        with open(path) as json_file:
            data = json.load(json_file)

        q = 0

        numbers = ChoiceList(['Zero', 'One', 'Two'])

        pages: List[AssessmentPage] = []

        for page_i, labels in enumerate(data['questions']):
            questions: List[Question] = []

            for label in labels:
                q_key = 'q' + str(q)
                q += 1
                question = ChoiceQuestion(q_key, label, numbers, [0, 10, 20])
                questions.append(question)

            page = AssessmentPage('Page ' + str(page_i + 1), questions)
            pages.append(page)

        return Assessment(key, pages, data['prefix_tpls'])


available_assessments = ('elem')


def get_assessment(key) -> Assessment:
    assert key in available_assessments
    return Assessment.factory('elem')


def get_all_assessments() -> Dict[str, Assessment]:
    return {
        'elem': get_assessment('elem')
    }

def get_form_lists():
    form_lists = {}
    for k, assessment in get_all_assessments().items():
        form_lists[k] = assessment.get_form_list(k)
    return form_lists
