#coding:utf-8

from django import forms
from models import Need, OrderRecord

class NeedForm(forms.ModelForm):
    """需求表单"""

    class Meta:
        model = Need
        exclude = ('user','created_at',)

class OrderRecordForm(forms.ModelForm):
    """接单记录生成表单"""

    class Meta:
        model = OrderRecord
        exclude = ('user')
