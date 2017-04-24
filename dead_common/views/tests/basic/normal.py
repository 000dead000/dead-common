# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class TestsBasicNormalCBV(TemplateView):
    template_name = "dead-common/tests/basic/normal.html"

    def get_context_data(self, **kwargs):
        context = super(TestsBasicNormalCBV, self).get_context_data(**kwargs)

        context['tests_tab'] = 'basic'
        context['tests_subtab'] = 'normal'

        return context

TestsBasicNormal = TestsBasicNormalCBV.as_view()
