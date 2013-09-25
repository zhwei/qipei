#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from qipei.settings import DOMAIN

from DjangoUeditor.models import UEditorField


#商铺
class Stores(models.Model):
    boss=models.OneToOneField(User,verbose_name='商铺主')

    name=models.CharField(max_length=10,verbose_name='商铺名称',unique=True)

    logo=models.ImageField(upload_to='store_logo',verbose_name='商店logo',blank=True)

    loc=models.ImageField(upload_to='index',verbose_name='首页广告',blank=True)

    tel=models.CharField(max_length=11,verbose_name='联系电话',blank=True)

    qq=models.CharField(max_length=11,verbose_name='QQ',blank=True)

    address=models.CharField(max_length=30,verbose_name='地址',blank=True)

#    sell=models.ManyToManyField(Sorts,max_length=100,verbose_name='主营产品',blank=True)
    notice=models.CharField(max_length=600,verbose_name='商铺公告',blank=True)

    it_description=UEditorField(max_length=200,verbose_name='商铺描述',blank=True,
                                toolbars='mini',imagePath='store/img', filePath='store/file')

    def logo_url(self):

        if self.logo:
            return self.logo.url()
        else:

            default_logo = DOMAIN + "/static/img/defaultlogo.jpg"

            return default_logo

    def loc_url(self):

        if self.loc:
            return self.loc.url()
        else:
            default_loc = DOMAIN + "/static/img/defaultlogo.jpg"

            return default_loc


    def get_url(self):
        url = DOMAIN + "/store/" + str(self.id) + "/"
        return url

    def __unicode__(self):
        return self.name

# friend link
class Links(models.Model):
    site=models.CharField(max_length=10,verbose_name='站点名称',)
    url=models.URLField(verbose_name='站点网址',max_length=64)
