#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import patterns
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from qipei.apps.account.views import Delete
from django.views.generic import UpdateView
from django.contrib.auth.decorators import permission_required, login_required

from ..account.form import UserForm
from .views import update_avatar, update_self
from .views import  DetailSelf, mark, un_mark, cus_login
from ..account.decorators import ver_not_login, ver_not_login_with_template

urlpatterns = patterns('qipei.apps.custom',
        # url(r'^login/$',
        # 'views.cus_login',name="custom_login"),

        url(r'^login/$', cus_login, name="custom_login"),

        url(r'^register/$', 'views.register',
            name="custom_register"),

        # update
        url(r'^self/$', login_required(DetailSelf.as_view()), name="custom_page"),
        url(r'^self/update$', update_self, name="update_custom_self"),
        url(r'^self/update/avatar$', login_required(update_avatar), name="update_custom_avatar"),


        url(r'^self/notifications/$', 'views.manage_notify', name="custom_notify"),

        url(r'^self/notifications/(?P<notify_id>\d+)/$', 'views.detail_notify', name="custom_detail_notify"),

        url(r'^self/notifications/mark/read/all/$', 'views.manage_notify',
            {'mark_all': True, 'unread': True}, name="mark_all_read"),

        url(r'^self/notifications/mark/read/(?P<notify_id>\d+)/$', 'views.manage_notify',
            {'unread': True}, name="mark_read"),

        url(r'^self/notifications/mark/unread/(?P<notify_id>\d+)/$', 'views.manage_notify',
            {'unread': False}, name="mark_unread"),



        url(r'^mark/store/(?P<store_id>\d+)$',
            login_required(mark, login_url='/custom/login'), name="mark_store"),

        url(r'^mark/product/(?P<product_id>\d+)/$',
            login_required(mark, login_url='/custom/login'), name="mark_product"),

        url(r'^unmark/store/(?P<store_id>\d+)$',
            login_required(un_mark, login_url='/custom/login'), name="un_mark_store"),

        url(r'^unmark/product/(?P<product_id>\d+)/$',
            login_required(un_mark, login_url='/custom/login'), name="un_mark_product"),
        )
