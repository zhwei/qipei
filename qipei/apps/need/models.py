# coding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from DjangoUeditor.models import UEditorField

class Need(models.Model):

    """用户发布需求model"""

    class Meta:
        db_table = 'needs'  # 数据库中表名称

    car_type = models.CharField(max_length=50)  # 发布需求的车具体型号
    short_dsc = models.CharField(max_length=100)  # 本次需求的简短描述
    # long_dsc = models.TextField(max_length=400)  # 本次需求的具体描述
    long_dsc = UEditorField(verbose_name='描述',imagePath='need/img', toolbars='img')
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)  # 链接普通会员

    order_records = []

    def get_absolute_url(self):
        return reverse('need_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return '[' + self.car_type + ']  ' + self.short_dsc


class OrderRecord(models.Model):

    """商家接单的记录"""

    class Meta:
        db_table = 'order_records'
    need = models.ForeignKey(Need)
    user = models.ForeignKey(User)  # 链接接单商家店主用户
    created_at = models.DateTimeField(auto_now=True)
