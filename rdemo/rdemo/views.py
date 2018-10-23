# -*- coding: utf-8 -*-

# Create your views here.
import logging

from django.forms import model_to_dict
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from rdemo.models import Person
from rdemo.serializers import rDemoSerializer, Validation

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
            obj = obj.filter(name=name)
        if is_not_blank(phone):
            obj = obj.filter(phone=phone)
        if is_not_blank(age):  # get para is str
            obj = obj.filter(age__gte=age)  # default is 1
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
            obj = obj.get()  # need to get the instance, otherwise UNIQUE constraint failed caused by save()
            # table update
            if is_not_blank(age):
                obj.age = age
            if is_not_blank(address):
                obj.address = address
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
            obj = obj.filter(age=age)  # default is 1
        if is_not_blank(address):
            obj = obj.filter(address=address)
        cnt = obj.count()
        obj.delete()
        return Response('destroy %s records' % cnt)


class PersonRESTSet(GenericViewSet, Validation):
    lookup_field = 'instance_id'
    serializer_class = rDemoSerializer

    def create(self, request):
        # parameter initial
        params = self.params_valid(request, serializer=rDemoSerializer)
        name = params["name"]
        phone = params["phone"]
        age = params.get("age", 1)
        address = params.get("address", "China")
        logging.info("this is the name=%s, phone=%s, age=%s, address=%s" % (name, phone, age, address))

        # create table
        obj = Person.objects.create(name=name, phone=phone, age=age, address=address)
        return Response({"result": True, "data": model_to_dict(obj), "message": "bkdata", "code": "89"})

    def retrieve(self, request, instance_id):
        # parameter initial
        params = self.params_valid(request, serializer=rDemoSerializer, skip=True)

        name = params.get("name")
        phone = params.get("phone")
        age = params.get("age")
        address = params.get("address")
        logging.info("this is the name=%s, phone=%s, age=%s, address=%s" % (name, phone, age, address))

        # table filter
        obj = Person.objects.all()
        if is_not_blank(name):
            obj = obj.filter(name=name)
        if is_not_blank(phone):
            obj = obj.filter(phone=phone)
        if age and age > 0:  # json para is not str
            obj = obj.filter(age__gte=age)  # default is 1
        if is_not_blank(address):
            obj = obj.filter(address__contains=address)

        # table render
        return Response({"result": True, "data": obj.values(), "message": "bkdata", "code": "88"})

    def update(self, request, instance_id):
        # parameter initial
        params = self.params_valid(request, serializer=rDemoSerializer)
        name = params["name"]
        phone = params["phone"]
        age = params.get("age")
        address = params.get("address")
        logging.info("this is the name=%s, phone=%s, age=%s, address=%s" % (name, phone, age, address))

        # table filter
        obj = Person.objects.filter(name=name).filter(phone=phone)
        if obj.count() > 0:
            obj = obj.get()  # need to get the instance, otherwise UNIQUE constraint failed caused by save()
            # table update
            if age and age > 0:
                obj.age = age
            if is_not_blank(address):
                obj.address = address
            obj.save()
            # table render
            return Response({"result": True, "data": model_to_dict(obj), "message": "bkdata", "code": "89"})
        else:
            return Response({"result": False, "data": "record with name=%s, phone=%s not found" % (name, phone), "message": "bkdata", "code": "89"})

    def destroy(self, request, instance_id):
        # parameter initial
        params = self.params_valid(request, serializer=rDemoSerializer, skip=True)
        name = params.get("name")
        phone = params.get("phone")
        age = params.get("age")
        address = params.get("address")
        logging.info("this is the name=%s, phone=%s, age=%s, address=%s" % (name, phone, age, address))

        # table filter
        obj = Person.objects.all()
        if is_not_blank(name):
            obj = obj.filter(name=name)
        if is_not_blank(phone):
            obj = obj.filter(phone=phone)
        if age and age > 0:
            obj = obj.filter(age=age)  # default is 1
        if is_not_blank(address):
            obj = obj.filter(address=address)
        cnt = obj.count()
        obj.delete()
        return Response({"result": True, "data": "destroy %s records" % cnt, "message": "bkdata", "code": "89"})


def is_not_blank(str):
    """判断某字符串是否不为空且长度不为0且不由space构成"""
    """@see https://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python"""
    return bool(str and str.strip())
