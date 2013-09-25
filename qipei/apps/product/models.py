#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel,TreeForeignKey

from DjangoUeditor.models import UEditorField

from qipei.settings import DOMAIN
from ..store.models import Stores


BOOLE_CHOICES=(
    ('是','1'),
    ('否','0'),
    )

#分类
class Sorts(MPTTModel):
    name=models.CharField(max_length=20,verbose_name="分类名称",unique=True)
    parent=TreeForeignKey("self", blank=True, null=True, related_name="children")


    def get_url(self):
        link='/wel/classfiy/'+  str(self.id) + '.html'
        return link

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name




#商品
class Products(models.Model):
    it_name=models.CharField(max_length=10,verbose_name='商品名称')

    company=models.ForeignKey(Stores,max_length=20,verbose_name='所属商铺',blank=True)

    sort=models.ManyToManyField(Sorts,verbose_name='分类')

    brand=models.CharField(max_length=10,verbose_name='品牌',blank=True)


    exit_date=models.DateField(verbose_name='上市时间',blank=True)

    price=models.CharField(max_length=20,verbose_name='价格')

    img=models.ImageField(verbose_name='商品图片',upload_to='image',blank=True)

    version=UEditorField(max_length=60,verbose_name='其他参数',
                         toolbars='list', blank=True)
    
    description=UEditorField(max_length=200,verbose_name='详细描述', toolbars='mini',
                             imagePath='product/img',filePath='product/file')


    def get_url(self):
        link=DOMAIN +'/store/'+  str(self.company.id) + '/view/' + str(self.id) + '.html'
        return link

    def img_url(self):

        if self.img:
            return self.img.url()
        else:
            default_img  = DOMAIN + "/static/img/defaultlogo.jpg"
            return default_img

    def __unicode__(self):
        return self.it_name



#留言
#class Messages(models.Model):
#    store=models.ForeignKey(Stores,verbose_name='商户名称',unique=True)
#    is_read=models.BooleanField(max_length='5',choices=BOOLE_CHOICES)
#    contact_number=models.DecimalField(max_digits='11',decimal_places='0',verbose_name='您的联系电话',blank=True)
#    content=models.CharField(max_length=200,verbose_name='留言内容')
#
#    def __unicode__(self):
#        return self.contact_number
#
## index ad*6
#class Ad_6(models.Model):
#    url1=models.URLField(verbose_name='图片链接1')
#    loc1=models.ImageField(verbose_name='首页小图1',upload_to="ad")
#
#    url2=models.URLField(verbose_name='图片链接2')
#    loc2=models.ImageField(verbose_name='首页小图2',upload_to="ad")
#
#    url3=models.URLField(verbose_name='图片链接3')
#    loc3=models.ImageField(verbose_name='首页小图3',upload_to="ad")
#
#    url4=models.URLField(verbose_name='图片链接4')
#    loc4=models.ImageField(verbose_name='首页小图4',upload_to="ad")
#
#    url5=models.URLField(verbose_name='图片链接5')
#    loc5=models.ImageField(verbose_name='首页小图5',upload_to="ad")
#
#    url6=models.URLField(verbose_name='图片链接6')
#    loc6=models.ImageField(verbose_name='首页小图6',upload_to="ad")
#
##index ad*3
#class Ad_middle(models.Model):
#    url1=models.URLField(verbose_name='图片链接1')
#    loc1=models.ImageField(verbose_name='首页中图1',upload_to="ad_middle")
#
#    url2=models.URLField(verbose_name='图片链接2')
#    loc2=models.ImageField(verbose_name='首页中图2',upload_to="ad_middle")
#
#    url3=models.URLField(verbose_name='图片链接3')
#    loc3=models.ImageField(verbose_name='首页中图3',upload_to="ad_middle")
#

#class News(models.Model):
#    title=models.CharField(max_length=20,verbose_name='标题')
#    content=models.CharField(max_length=500,verbose_name=' 内容 ')
#    store=models.ForeignKey(Stores)
#
#    def get_url(self):
#        link=DOMAIN +'/'+  str(self.store.id) + '/news/' + str(self.id) + '.html'
#        return link
#
#    def __unicode__(self):
#        return self.title
