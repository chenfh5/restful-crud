# -*- coding: utf-8 -*-

# Create your views here.
import logging

from django.forms import model_to_dict
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from rdemo.models import Person

logging.basicConfig(level=logging.INFO)


class PersonSet(GenericViewSet):
    lookup_field = 'person_id'

    # @see https://www.django-rest-framework.org/api-guide/routers/#simplerouter
    # `create` is an existing route(by default)
    @list_route(methods=['get'], url_path='create1')
    def create1(self, request):
        # parameter initial
        name = request.query_params["name"]
        phone = request.query_params["phone"]
        age = request.query_params.get("age", 1)
        address = request.query_params.get("address", "China")
        logging.info("this is the name=%s, phone=%s, age=%s, address=%s" % (name, phone, age, address))

        # create table
        obj = Person.objects.create(name=name, phone=phone, age=age, address=address)
        return Response(model_to_dict(obj))

    @list_route(methods=['get'], url_path='retrieve1')
    def retrieve1(self, request):
        # parameter initial
        name = request.query_params.get("name")
        phone = request.query_params.get("phone")
        age = request.query_params.get("age")
        address = request.query_params.get("address")
        logging.info("this is the name=%s, phone=%s, age=%s, address=%s" % (name, phone, age, address))

        # table filter
        obj = Person.objects.all()
        if is_not_blank(name):
            obj = obj.filter(name__contains=name)
        if is_not_blank(phone):
            obj = obj.filter(phone=phone)
        if is_not_blank(age):
            obj = obj.filter(age__lte=age)  # default is 1
        if is_not_blank(address):
            obj = obj.filter(address__contains=address)

        # table render
        dic = {}
        for idx, one in enumerate(obj):
            dic[idx] = model_to_dict(one)
        return Response(dic)

    @list_route(methods=['get'], url_path='update1')
    def update1(self, request):
        # parameter initial
        name = request.query_params["name"]
        phone = request.query_params["phone"]
        age = request.query_params.get("age")
        address = request.query_params.get("address")
        logging.info("this is the name=%s, phone=%s, age=%s, address=%s" % (name, phone, age, address))

        # table filter
        obj = Person.objects.filter(name=name).filter(phone=phone)
        if obj.count() > 0:
            # table update
            if is_not_blank(age):
                obj.first().age = age
            if is_not_blank(address):
                obj.first().address = address
            obj.save()
            # table render
            return Response(model_to_dict(obj))
        else:
            return Response("record with name=%s, phone=%s not found" % (name, phone))

    @list_route(methods=['get'], url_path='destroy1')
    def destroy1(self, request):
        # parameter initial
        name = request.query_params.get("name")
        phone = request.query_params.get("phone")
        age = request.query_params.get("age")
        address = request.query_params.get("address")
        logging.info("this is the name=%s, phone=%s, age=%s, address=%s" % (name, phone, age, address))

        # table filter
        obj = Person.objects.all()
        if is_not_blank(name):
            obj = obj.filter(name=name)
        if is_not_blank(phone):
            obj = obj.filter(phone=phone)
        if is_not_blank(age):
            obj = obj.filter(age__lte=age)  # default is 1
        if is_not_blank(address):
            obj = obj.filter(address__contains=address)
        obj.delete()
        return Response('destroy %s records' % obj.count())


def is_not_blank(str):
    """判断某字符串是否不为空且长度不为0且不由space构成"""
    """@see https://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python"""
    return bool(str and str.strip())
