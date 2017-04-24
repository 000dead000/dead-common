# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.contrib import messages


class TestsBasicNormalCBV(TemplateView):
    template_name = "dead-common/tests/basic/normal.html"

    def generar_mensajes(self):
        messages.add_message(
            self.request,
            messages.DEBUG,
            'Mensaje DEBUG'
        )

        messages.add_message(
            self.request,
            messages.INFO,
            'Mensaje INFO'
        )

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Mensaje SUCCESS'
        )

        messages.add_message(
            self.request,
            messages.WARNING,
            'Mensaje WARNING'
        )

        messages.add_message(
            self.request,
            messages.ERROR,
            'Mensaje ERROR'
        )

    def get_context_data(self, **kwargs):
        context = super(TestsBasicNormalCBV, self).get_context_data(**kwargs)

        context['tests_tab'] = 'basic'
        context['tests_subtab'] = 'normal'

        context['test_name'] = self.request.GET.get("name", "")

        if context['test_name'] == "mensajes":
            self.generar_mensajes()

        return context

TestsBasicNormal = TestsBasicNormalCBV.as_view()
