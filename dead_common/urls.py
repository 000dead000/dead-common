# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views.tests import TestsHome
from .views.tests.basic import TestsBasicNormal

urlpatterns = [
    url(
        r'^$',
        TestsHome,
        name='tests-home'
    ),

    url(
        r'^basic$',
        TestsBasicNormal,
        name='tests-basic-normal'
    ),
]