#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from django import forms
#from django.http import HttpResponse
from django.forms import ModelForm,Textarea
from qipei.apps.store.models import Stores
#from django.utils.translation import ugettext_lazy as _


#add store
class StoreForm(ModelForm):
    class Meta:
        model=Stores


#edit store
class EditStoreForm(ModelForm):
    class Meta:
        fields=('name','tel','qq','address','notice','it_description')
        model=Stores
        widgets={
            'notice':Textarea(attrs={'cols':10,'rows':10}),
            'it_description':Textarea(attrs={'cols':10,'rows':10}),
            }

#store ad
class StoreAdForm(ModelForm):
    class Meta:
        fields=('logo','loc')
        model=Stores
