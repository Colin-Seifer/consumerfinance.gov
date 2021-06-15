import re
import time

from typing import Dict

from django.http import HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest
from django.template.loader import render_to_string

from formtools.wizard.views import NamedUrlCookieWizardView

from .assessments import (
    Question, available_assessments, get_assessment, get_form_lists)
from . import urlEncode


class AssessmentWizard(NamedUrlCookieWizardView):
    def done(self, form_list, **kwargs):
        # Find assessment based on hidden "_k" question in page1
        first_page = self.get_form('page1')
        assessment_key = first_page.fields['_k'].initial
        if (not isinstance(assessment_key, str) or
                assessment_key not in available_assessments):
            # Hmm this isn't right
            response = HttpResponseRedirect('../')
            response.delete_cookie('resultUrl')
            response.delete_cookie('wizard_survey_wizard')
            return response

        assessment = get_assessment(assessment_key)

        # Calc score and encode in URL
        question_scores: Dict[Question, float] = assessment.get_score(
            self.get_all_cleaned_data())['question_scores']
        part_scores: Dict[str, float] = {}

        for question, score in question_scores.items():
            part = re.match(r'^\d+', question.section)[0]
            if part not in part_scores:
                part_scores[part] = 0
            part_scores[part] += score

        subtotals = (v for k, v in sorted(part_scores.items()))
        encoded = urlEncode.dumps(assessment, subtotals, time.time())

        # Send to results page
        response = HttpResponseRedirect('../../results/')
        response.set_signed_cookie('resultUrl', encoded)
        response.delete_cookie('wizard_survey_wizard')
        return response

    def process_step(self, form):
        # By default, the big CSRF tokens get needlessly stored in the cookie
        # and take up a lot of space. This is bad because cookies have a
        # small limit.
        dict = self.get_form_step_data(form)
        return {
            key: val for key, val in dict.items() if (
                key != 'csrfmiddlewaretoken')}

    @staticmethod
    def build_views():
        # Create view wrappers for our assessments.
        wizard_views = {}
        for k, form_list in get_form_lists().items():
            wizard_views[k] = AssessmentWizard.as_view(
                form_list=form_list,
                url_name=f'assessment_{k}_step',
                template_name='teachers_digital_platform/survey-page.html',
            )
        return wizard_views


def assessment_results(request: HttpRequest):
    if request.method != 'GET':
        return HttpResponse(status=404)

    try:
        result_url = request.get_signed_cookie('resultUrl')
        if (result_url is None):
            raise
    except:  # noqa: E722
        return HttpResponseRedirect('../')

    res = urlEncode.loads(result_url)
    if res is None:
        return HttpResponseRedirect('../')

    print(res)

    rendered = render_to_string(
        'teachers_digital_platform/survey-results.html',
        {
            'request': request,
            'assessment': res['assessment'],
            'subtotals': res['subtotals'],
            'time': res['time'],
        },
    )
    return HttpResponse(status=200, content=rendered)
