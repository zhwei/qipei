#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = patterns('qipei.apps.welcome',
        url(r'^$','views.index',name='index'),
        url(r'^classfiy/(?P<sort_id>\d+).html$','views.classfiy', name="wel_classfiy"),
        url(r'^comment$', TemplateView.as_view(template_name="comment.html"), name="comment_online"),
        url(r'^about$', TemplateView.as_view(template_name="about.html"), name="about_us"),
        )
