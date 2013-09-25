#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

from DjangoUeditor.models import UEditorField


class Expert(models.Model):

    user = models.ForeignKey(User, verbose_name='用户姓名')

    avatar = models.ImageField(upload_to='expert_avatar', blank=True) #头像

    description = UEditorField(verbose_name='专家介绍', max_length='500')

    date_show = models.DateTimeField(verbose_name='交流日期')

    date_joined = models.DateTimeField(verbose_name='入驻日期', default=timezone.now)
