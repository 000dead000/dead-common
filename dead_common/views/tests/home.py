# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class TestsHomeCBV(TemplateView):
    template_name = "dead-common/tests/home.html"

    def get_context_data(self, **kwargs):
        context = super(TestsHomeCBV, self).get_context_data(**kwargs)

        context['tests_tab'] = None

        return context

TestsHome = TestsHomeCBV.as_view()
