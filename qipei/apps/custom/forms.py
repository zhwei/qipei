#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.forms import ModelForm, ChoiceField,CheckboxInput, Select

from .models import Custom


class CustomForm(ModelForm):

    class Meta:

        model = Custom

        fields = ['sex','age','car_type','area','tel','mobile','qq']

        widgets = {
            'sex': Select(choices=((True,'男'),(False,'女')))
        }



