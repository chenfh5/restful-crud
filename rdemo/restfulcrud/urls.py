# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from rdemo.views import PersonSet, PersonRESTSet

router = DefaultRouter(trailing_slash=True)

router.register(r'person', PersonSet, base_name='person')
router.register(r'personrest', PersonRESTSet, base_name='personrest')

urlpatterns = [
    url(r'^', include(router.urls)),
]
