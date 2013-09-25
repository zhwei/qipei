#coding=utf-8

from django.db import models

# friend link
class Links(models.Model):
    site=models.CharField(max_length=10,verbose_name='站点名称',)
    url=models.URLField(verbose_name='站点网址',max_length=64)

    def __unicode__(self):
        return self.site
