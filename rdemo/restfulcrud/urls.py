# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from rdemo.views import PersonSet

router = DefaultRouter(trailing_slash=True)

router.register(r'person', PersonSet, base_name='person')

urlpatterns = [
    url(r'^', include(router.urls)),
]
