# -*- coding: utf-8 -*-

from rest_framework import serializers


class rDemoSerializer(serializers.Serializer):
    """序列化器，需要校验的参数将在这里定义"""
    name = serializers.CharField()
    phone = serializers.CharField(max_length=11, min_length=11)


class Validation(object):

    def params_valid(self, request, serializer, skip=False):
        """
        校验参数是否满足 serializer 规定的格式
        """
        # 校验request中的参数
        if request.method == 'GET':
            params = request.query_params
        else:
            params = request.data

        serializer = serializer(data=params)
        if not skip:
            serializer.is_valid(raise_exception=True)

        return params
