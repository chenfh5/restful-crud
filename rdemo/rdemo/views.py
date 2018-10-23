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
        """
        @api {get} /person/create1/?name=xxx&phone=xxx&age=11&address=cn 新增实例
        @apiGroup PersonSet
        @apiParam {String} name
        @apiParam {String} phone
        @apiParam {Number} age
        @apiParam {String} address
        @apiParamExample {json} 参数样例:
        {
            "name": "c1",
            "phone": "13800138000",
            "age": "23",
            "address": "深圳",
        }
        @apiSuccessExample {json} 成功返回:
        {
            "name": "c1",
            "age": "11",
            "address": "深圳",
            "created_by": "",
            "phone": "13800138000",
            "updated_by": "",
            "id": 34,
            "description": ""
        }
        """
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
        """
        @api {get} /person/retrieve1/?name=xxx&phone=xxx&age=11&address=xxx 获取单个实例详情
        @apiGroup PersonSet
        @apiParam {String} [name] optional
        @apiParam {String} [phone] optional
        @apiParam {Number} [age] optional
        @apiParam {String} [address] optional
        @apiSuccessExample {json} 成功返回:
        {
            "0": {
                "name": "qq",
                "age": 99,
                "address": "中国",
                "created_by": "",
                "phone": "13800138000",
                "updated_by": "",
                "id": 31,
                "description": ""
            },
            "1": {
                "name": "qqqq",
                "age": 45,
                "address": "us",
                "created_by": "",
                "phone": "13800138000",
                "updated_by": "",
                "id": 33,
                "description": ""
            },
            "2": {
                "name": "c1",
                "age": 11,
                "address": "cn",
                "created_by": "",
                "phone": "13800138000",
                "updated_by": "",
                "id": 34,
                "description": ""
            }
        }
        """
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
        """
        @api {get} /person/update1/?name=xxx&phone=xxx&age=11&address=xxx 替换实例内容
        @apiGroup PersonSet
        @apiParam {String} name
        @apiParam {String} phone
        @apiParam {Number} [age] optional
        @apiParam {String} [address] optional
        @apiParamExample {json} 参数样例:
        {
            "name": "c1",
            "phone": "13800138000",
            "age": "23",
            "address": "深圳",
        }
        @apiSuccessExample {json} 成功返回:
        {
            "name": "c1",
            "age": "11",
            "address": "深圳",
            "created_by": "",
            "phone": "13800138000",
            "updated_by": "",
            "id": 34,
            "description": ""
        }
        """
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
        """
        @api {get} /person/update1/?name=xxx&phone=xxx&age=11&address=xxx 删除实例
        @apiGroup PersonSet
        @apiParam {String} [name] optional
        @apiParam {String} [phone] optional
        @apiParam {Number} [age] optional
        @apiParam {String} [address] optional
        @apiSuccessExample {String} 成功返回:
        "destroy 3 records"
        """

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
        """
        @api {post} /personrest 新增实例
        @apiGroup PersonRESTSet
        @apiParam {String} name
        @apiParam {String} phone
        @apiParam {Number} age
        @apiParam {String} address
        @apiParamExample {json} 参数样例:
        {
            "name": "c1",
            "phone": "13800138000",
            "age": "23",
            "address": "深圳",
        }
        @apiSuccessExample {json} 成功返回:
        {
            "message": "bkdata",
            "code": "89",
            "data": {
                "name": "r1",
                "age": 23,
                "address": "深圳",
                "created_by": "",
                "phone": "13800138000",
                "updated_by": "",
                "id": 35,
                "description": ""
            },
            "result": true
        }
        """
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
        """
        @api {get} /personrest/99?age=2 获取单个实例详情
        @apiGroup PersonRESTSet
        @apiParam {String} [name] optional
        @apiParam {String} [phone] optional
        @apiParam {Number} [age] optional
        @apiParam {String} [address] optional
        @apiSuccessExample {json} 成功返回:
        {
            "message": "bkdata",
            "code": "88",
            "data": [
                {
                    "description": "",
                    "created_at": "2018-10-23T13:08:24.732000Z",
                    "updated_at": "2018-10-23T13:08:24.732000Z",
                    "created_by": "",
                    "name": "r1",
                    "phone": "13800138000",
                    "address": "cn",
                    "age": 23,
                    "id": 35,
                    "updated_by": ""
                },
                {
                    "description": "",
                    "created_at": "2018-10-23T13:18:06.265000Z",
                    "updated_at": "2018-10-23T13:18:06.265000Z",
                    "created_by": "",
                    "name": "r2",
                    "phone": "13800138000",
                    "address": "深圳",
                    "age": 23,
                    "id": 36,
                    "updated_by": ""
                }
            ],
            "result": true
        }
        """
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
        """
        @api {put} /personrest/99?age=2 获取单个实例详情
        @apiGroup PersonRESTSet
        @apiParam {String} name
        @apiParam {String} phone
        @apiParam {Number} [age] optional
        @apiParam {String} [address] optional
        @apiParamExample {json} 参数样例:
        {
            "name": "c1",
            "phone": "13800138000",
            "age": "23",
            "address": "深圳",
        }
        @apiSuccessExample {json} 成功返回:
        {
            "message": "bkdata",
            "code": "89",
            "data": {
                "name": "r1",
                "age": 34,
                "address": "cn",
                "created_by": "",
                "phone": "13800138000",
                "updated_by": "",
                "id": 35,
                "description": ""
            },
            "result": true
        }
        """
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
        """
        @api {delete} /personrest/99?age=2 获取单个实例详情
        @apiGroup PersonRESTSet
        @apiParam {String} [name] optional
        @apiParam {String} [phone] optional
        @apiParam {Number} [age] optional
        @apiParam {String} [address] optional
        @apiParamExample {json} 参数样例:
        {
            "name": "c1"
        }
        @apiSuccessExample {json} 成功返回:
        {
            "message": "bkdata",
            "code": "89",
            "data": "destroy 1 records",
            "result": true
        }
        """
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


class PersonLevelSet(GenericViewSet, Validation):
    lookup_field = 'age'
    serializer_class = rDemoSerializer

    def create(self, request, name, phone):
        """
        @api {post} v3/personlevel/names/:name/phones/:phone/ages 新增实例
        @apiGroup PersonLevelSet
        @apiParam {String} names
        @apiParam {String} phones
        @apiParam {Number} ages
        @apiParamExample {json} 参数样例:
        {
            "name": "placeholder for serializer",
            "phone": "12345678912",
            "age": 45,
            "address": "us"
        }
        @apiSuccessExample {json} 成功返回:
        {
            "message": "bkdata",
            "code": "79",
            "data": {
                "name": "qqqq",
                "age": 45,
                "address": "us",
                "created_by": "",
                "phone": "13800138000",
                "updated_by": "",
                "id": 38,
                "description": ""
            },
            "result": true
        }
        """
        # parameter initial
        params = self.params_valid(request, serializer=rDemoSerializer)
        age = params.get("age", 1)
        address = params.get("address", "China")
        logging.info("this is the name=%s, phone=%s, age=%s, address=%s" % (name, phone, age, address))

        # create table
        obj = Person.objects.create(name=name, phone=phone, age=age, address=address)
        return Response({"result": True, "data": model_to_dict(obj), "message": "bkdata", "code": "79"})

    def retrieve(self, request, name, phone, age):
        """
        @api {get} v3/personlevel/names/:name/phones/:phone/ages/:age 获取单个实例详情
        @apiGroup PersonLevelSet
        @apiParam {String} names None
        @apiParam {String} phone None
        @apiParam {Number} ages 0
        @apiSuccessExample {json} 成功返回:
        {
            "message": "bkdata",
            "code": "78",
            "data": [
                {
                    "description": "",
                    "created_at": "2018-10-23T13:18:06.265000Z",
                    "updated_at": "2018-10-23T13:18:06.265000Z",
                    "created_by": "",
                    "name": "r2",
                    "phone": "13800138000",
                    "address": "深圳",
                    "age": 23,
                    "id": 36,
                    "updated_by": ""
                },
                {
                    "description": "",
                    "created_at": "2018-10-23T13:22:40.437000Z",
                    "updated_at": "2018-10-23T13:22:40.437000Z",
                    "created_by": "",
                    "name": "qqqq",
                    "phone": "13800138000",
                    "address": "us",
                    "age": 45,
                    "id": 38,
                    "updated_by": ""
                }
            ],
            "result": true
        }
        """
        # parameter initial
        params = self.params_valid(request, serializer=rDemoSerializer, skip=True)

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
        return Response({"result": True, "data": obj.values(), "message": "bkdata", "code": "78"})

    def update(self, request, name, phone, age):
        """
        @api {put} v3/personlevel/names/:name/phones/:phone/ages/:age 替换实例内容
        @apiGroup PersonLevelSet
        @apiParam {String} names
        @apiParam {String} phone
        @apiParam {Number} ages
        @apiParamExample {json} 参数样例:
        {
            "name": "placeholder for serializer",
            "phone": "12345678912",
            "age": 99,
            "address": "中国"
        }
        @apiSuccessExample {json} 成功返回:
        {
            "message": "bkdata",
            "code": "79",
            "data": {
                "name": "qqqq",
                "age": 99,
                "address": "中国",
                "created_by": "",
                "phone": "13800138000",
                "updated_by": "",
                "id": 38,
                "description": ""
            },
            "result": true
        }
        """
        # parameter initial
        params = self.params_valid(request, serializer=rDemoSerializer)
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
            return Response({"result": True, "data": model_to_dict(obj), "message": "bkdata", "code": "79"})
        else:
            return Response({"result": False, "data": "record with name=%s, phone=%s not found" % (name, phone), "message": "bkdata", "code": "79"})

    def destroy(self, request, name, phone, age):
        """
        @api {delete} v3/personlevel/names/:name/phones/:phone/ages/:age 删除实例
        @apiGroup PersonLevelSet
        @apiParam {String} names
        @apiParam {String} phone
        @apiParam {Number} ages
        @apiParamExample {json} 参数样例:
        {
            "name": "r1"
        }
        @apiSuccessExample {json} 成功返回:
        {
            "message": "bkdata",
            "code": "79",
            "data": "destroy 1 records",
            "result": true
        }
        """
        # parameter initial
        params = self.params_valid(request, serializer=rDemoSerializer, skip=True)
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
        return Response({"result": True, "data": "destroy %s records" % cnt, "message": "bkdata", "code": "79"})


def is_not_blank(str):
    """判断某字符串是否不为空且长度不为0且不由space构成"""
    """@see https://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python"""
    return bool(str and str.strip() and str.strip() != "None")
