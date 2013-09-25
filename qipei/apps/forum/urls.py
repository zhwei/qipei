#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import patterns
# from django.views.generic import UpdateView
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import permission_required, login_required
#
#
# from qipei.apps.account.form import UserForm
# from qipei.apps.account.views import Delete
# from qipei.apps.account.decorators import ver_not_login, ver_not_login_with_template


urlpatterns = patterns('qipei.apps.forum.views',
        # url(r'^login/$',
        # 'views.cus_login',name="custom_login"),

        url(r'^/$', 'list_subject', name="list_subject"),
        url(r'^list/$', 'list_subject', name="list_subject"),


        url(r'^subject/create/$',                     'create_subject', name="create_subject"),
        url(r'^subject/(?P<subject_id>\d+)$',         'reply_subject',  name="detail_subject"),
        url(r'^subject/(?P<subject_id>\d+)/update/$', 'update_subject', name="update_subject"),
        url(r'^subject/(?P<subject_id>\d+)#reply$',   'reply_subject',  name="reply_subject"),
        url(r'^subject/(?P<subject_id>\d+)/delete/$', 'delete_subject', name="delete_subject"),


        url(r'^reply/(?P<reply_id>\d+)/update/$', 'update_reply', name="update_reply"),
        url(r'^reply/(?P<reply_id>\d+)/delete/$', 'delete_reply', name="delete_reply"),



        )
