#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url
from django.conf.urls import patterns
from django.contrib.auth.views import login
from django.views.generic import UpdateView
from django.contrib.auth.models import User


from .form import UserForm
from .views import Delete
from .decorators import ver_not_login, ver_not_login_with_template


urlpatterns = patterns('',
        url(r'^$', ver_not_login_with_template(login),
            {'template_name':'login.html'},
        ),
        url(r'^login/$', ver_not_login_with_template(login),
            {'template_name':'login.html'},
            name="login"),
        )

urlpatterns += patterns('qipei.apps.account',

    # url(r'^$', 'views.admin_login',name="login"),
    url(r'^logout/$', 'views.logout',name="logout"),
    url(r'^profile/$', 'views.index',name="admin_index"),
    url(r'^register/$', 'views.register',name="register"),
    url(r'^changepw/$', 'views.change_password',name="changepw"),


    url(r'^create/(?P<t>\d+)$', 'views.create_user',name="create_user"),

    url(r'^create/notify/$', 'views.create_notify',name="create_notify"),

    url(r'^list','views.manUser',name="list_user"),
    url(r'^delete/(?P<pk>\d+)$',Delete.as_view(),name="delete_user"),
    url(r'^pass/(?P<pk>\d+)$','views.passUser',name="pass_user"),

    url(r'^update/(?P<pk>\d+)$',
        UpdateView.as_view(
            model=User,
            form_class=UserForm,
            template_name="update_user.html",
            context_object_name="foo",
            success_url="/index/ok.html"
            ),
        name="update_user",
    ),
)
