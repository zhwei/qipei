#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from qipei.apps.store.models import Stores

from DjangoUeditor.models import UEditorField





class Subject(models.Model):

    """
    专家讲坛主题
    """

    title = models.CharField(verbose_name='标题',max_length=50)

    content = UEditorField(verbose_name='内容', imagePath='forum/img',
                           toolbars='mini', filePath='forum/file')    # 帖子的内容

    create_date = models.DateTimeField(verbose_name='发表时间',auto_now_add=True)   # 回复的时间

    update_date = models.DateTimeField(verbose_name='修改时间',auto_now=True)

    user = models.ForeignKey(User)



    def __unicode__(self):

        return self.title


class Reply(models.Model):

    """
    讲坛回复
    """

    title = models.CharField(verbose_name='标题',max_length=50)

    content = UEditorField(verbose_name='内容', max_length=1000, imagePath='forum/img',
                           toolbars='mini', filePath='forum/file')    # 回复的内容

    create_date = models.DateTimeField(verbose_name='发表时间',auto_now_add=True)   # 回复的时间

    update_date = models.DateTimeField(verbose_name='修改时间',auto_now=True)

    subject = models.ForeignKey(Subject)

    user = models.ForeignKey(User)    # 回复的普通用户



    def __unicode__(self):
        return self.title
