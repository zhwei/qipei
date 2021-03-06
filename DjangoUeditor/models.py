#!/usr/bin/env python
# coding: utf-8

from django.db import models
from django.contrib.admin import widgets as admin_widgets
from DjangoUeditor.widgets import UEditorWidget,AdminUEditorWidget
from DjangoUeditor.utils import MadeUeditorOptions

class UEditorField(models.TextField):
    """
    百度HTML编辑器字段,初始化时，可以提供以下参数
        initial:初始内容
        plugins:元组
        mode：工具按钮的配置数量，
        toolbars:提供工具按钮列表,取值为列表，如['bold', 'italic'],取值为：mini,normal,full，代表小，一般，全部
        imagePath:图片上传的路径,如"images/",实现上传到"{{MEDIA_ROOT}}/images"文件夹
        filePath:附件上传的路径,如"files/",实现上传到"{{MEDIA_ROOT}}/files"文件夹
        imageManagerPath:图片管理器显示的路径，如果不指定则默认=imagepath
        options：其他UEditor参数，字典类型
        css:编辑器textarea的CSS样式
    """

    def __init__(self,verbose_name,width=600,height=300,plugins=(),toolbars="full",filePath="",imagePath="",scrawlPath="",imageManagerPath="",css="",options={},**kwargs):
        self.ueditor_options = MadeUeditorOptions(width,height,plugins,toolbars,filePath,imagePath,scrawlPath,imageManagerPath,css,options)
        kwargs["verbose_name"] = verbose_name

        super(UEditorField,self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': UEditorWidget(**self.ueditor_options)}
        defaults.update(kwargs)
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = AdminUEditorWidget(**self.ueditor_options)
        return super(UEditorField, self).formfield(**defaults)

 
