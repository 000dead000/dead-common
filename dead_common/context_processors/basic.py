# -*- coding: utf-8 -*-

from django.conf import settings


def basic(request):
    params = {
        # Titles
        'WINDOW_TITLE': settings.WINDOW_TITLE,
        'NAVBAR_TITLE': settings.NAVBAR_TITLE,
        'FOOTER_LEFT_TITLE': settings.FOOTER_LEFT_TITLE,
        'FOOTER_RIGHT_TITLE': settings.FOOTER_RIGHT_TITLE,

        # Flags
        'SHOW_ADMIN_TITLE': settings.SHOW_ADMIN_TITLE,
        'SHOW_NAVBAR_TITLE': settings.SHOW_NAVBAR_TITLE,
        'SHOW_FOOTER_LEFT_TITLE': settings.SHOW_FOOTER_LEFT_TITLE,
        'SHOW_FOOTER_RIGHT_TITLE': settings.SHOW_FOOTER_RIGHT_TITLE,
        'SHOW_FOOTER_CONTAINER_MODE_SELECTOR': settings.SHOW_FOOTER_CONTAINER_MODE_SELECTOR,
        'SHOW_NAVBAR': settings.SHOW_NAVBAR,
        'SHOW_FOOTER_GO_UP': settings.SHOW_FOOTER_GO_UP,
        'SHOW_FOOTER_GO_DOWN': settings.SHOW_FOOTER_GO_DOWN,
        'SHOW_FOOTER_REFRESH': settings.SHOW_FOOTER_REFRESH,

        'BASE_TEMPLATE': settings.BASE_TEMPLATE,
    }

    return params
