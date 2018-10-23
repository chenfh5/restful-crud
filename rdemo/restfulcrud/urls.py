# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from rdemo.views import PersonSet, PersonRESTSet, PersonLevelSet

router = DefaultRouter(trailing_slash=True)

# Add the generated REST URLs
router.register(r'person', PersonSet, base_name='person')
router.register(r'personrest', PersonRESTSet, base_name='personrest')
router.register(r'v3/personlevel/names/(?P<name>\w+)/phones/(?P<phone>\w+)/ages', PersonLevelSet, base_name='personlevel')

urlpatterns = [
    url(r'^', include(router.urls)),
]
