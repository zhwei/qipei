#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from upload_avatar.signals import avatar_crop_done
from upload_avatar.models import UploadAvatarMixIn

from qipei.apps.store.models import Stores
from qipei.apps.product.models import Products


class Custom(models.Model, UploadAvatarMixIn):

    """用户表"""

    user = models.OneToOneField(User, parent_link=True, related_name='user_info')

    is_custom = models.BooleanField(default=False)

    # self information

    avatar_name = models.CharField(max_length=128)

    sex = models.BooleanField(verbose_name = '性别', default=True)

    age = models.CharField(verbose_name='年龄', max_length=2, blank=True, null=True)

    description = models.TextField(verbose_name='个人描述',max_length=140 ,blank=True)

    # car type
    car_type = models.CharField(verbose_name='车辆类型',max_length=10, blank=True)

    # 地区
    area = models.CharField(verbose_name='所在地区', max_length=50)

    # connection
    tel = models.CharField(verbose_name='固定电话', max_length=12,blank=True, null=True)
    mobile = models.CharField(verbose_name='手机号', max_length=11, blank=True, null=True)
    qq = models.CharField(verbose_name='QQ',max_length=11, blank=True, null=True)

    # datetime
    last_login = models.DateTimeField(verbose_name='最近登录', auto_now=True, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    money = models.FloatField(verbose_name='财富值', blank=True, null=True)

    # 收藏的 产品 和 店铺
    mark_product = models.ManyToManyField(Products, symmetrical=False,)
    mark_store = models.ManyToManyField(Stores, symmetrical=False,)


    def get_uid(self):
        return self.user.id

    def get_avatar_name(self, size):
        return UploadAvatarMixIn.build_avatar_name(self, self.avatar_name, size)

    def get_avatar_large(self):

        return self.get_avatar_url(180)

    def get_avatar_middle(self):

        return self.get_avatar_url(100)

    def get_avatar_small(self):

        return self.get_avatar_url(50)

    def url(self):

        url = "/custom/user/" + str(self.id)

        return url

    def add_money(self, num):

        self.money = self.mondy + float(num)

    def del_money(self, num):

        self.money = self.mondy - float(num)

    def add_to_mark(self, store_id, product_id):

        if store_id:

            store = get_object_or_404(Stores, id=store_id)

            self.mark_store.add(store)

        elif product_id:

            product = get_object_or_404(Products, id=product_id)

            self.mark_product.add(product)

        else:
            return False

    def remove_from_mark(self, store_id, product_id):

        if store_id:

            store = get_object_or_404(Stores, id=store_id)
            self.mark_store.remove(store)

        elif product_id:

            product = get_object_or_404(Products, id=product_id)
            self.mark_product.remove(product)

        else:
            return False



    def __unicode__(self):
        return self.user.username



def save_avatar_in_db(sender, uid, avatar_name, **kwargs):
    if Custom.objects.filter(user_id=uid).exists():
        Custom.objects.filter(user_id=uid).update(avatar_name=avatar_name)
    else:
        Custom.objects.create(user_id=uid, avatar_name=avatar_name)

avatar_crop_done.connect(save_avatar_in_db)