# -*- coding: utf-8 -*-

# Create your models here.

from django.core.validators import MinLengthValidator
from django.db import models


class CommonInfo(models.Model):
    """
    公共字段，所有表（model）都需要包含这些字段
    """
    # @see https://docs.djangoproject.com/en/1.8/topics/db/models/#abstract-base-classes
    created_by = models.CharField(max_length=128, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=128, default='')
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(default='')

    class Meta:
        abstract = True

    objects = models.Manager()


class Person(CommonInfo):
    name = models.CharField(max_length=20)
    phone = models.CharField('phone Number', max_length=11, validators=[MinLengthValidator(11)])
    age = models.IntegerField()
    address = models.TextField()

    class Meta:
        db_table = "person"
        unique_together = (("name", "phone"),)
