# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.contrib import messages
from django.core.exceptions import SuspiciousOperation # 400
from django.core.exceptions import PermissionDenied # 403
from django.http import Http404 # 404


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

    def display_error_page(self, code):
        # 400
        if code == 1:
            raise SuspiciousOperation
        # 403
        elif code == 2:
            raise PermissionDenied
        # 404
        elif code == 3:
            raise Http404
        # 500
        elif code == 4:
            raise Exception

    def get_context_data(self, **kwargs):
        context = super(TestsBasicNormalCBV, self).get_context_data(**kwargs)

        context['tests_tab'] = 'basic'
        context['tests_subtab'] = 'normal'

        context['test_name'] = self.request.GET.get("test_name", "")

        if context['test_name'] == "mensajes":
            self.generar_mensajes()
        elif context['test_name'] == "error":
            context['code'] = int(self.request.GET.get("code"))
            self.display_error_page(context['code'])

        return context

TestsBasicNormal = TestsBasicNormalCBV.as_view()
