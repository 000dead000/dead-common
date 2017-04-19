# -*- coding: utf-8 -*-

from .. import utilities


def current_application_and_view(request):
    params = {
        'CURRENT_APPLICATION':
            utilities.get_current_application(request),
        'CURRENT_VIEW':
            utilities.get_current_view(request),
    }

    return params
