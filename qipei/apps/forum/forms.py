#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm,CharField,EmailField,ChoiceField


from .models import Reply, Subject

class ReplyForm(ModelForm):

    class Meta:
        model=Reply
        fields=('title','content')


class SubjectForm(ModelForm):

    class Meta:
        model=Subject
        fields=('title','content')