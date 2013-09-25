#coding:utf-8

from django.conf.urls import patterns, url
from .need_con import NeedList, needDetail, UpdateNeed, DeleteNeed, CreateNeed
from .admin_con import AdminNeedList, adminNeedDetail, AdminDeleteNeed
from .order_record_con import createOrderRecord
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
        url(r'^needs/$', NeedList.as_view(), name='needs_list'),
        url(r'^need/create/$', login_required(CreateNeed.as_view(),
            login_url='/custom/login'), name='create_need'),
        #url(r'need/(?P<pk>\d+)/$', NeedDetail.as_view(), name='need_detail'),
        url(r'^need/(?P<pk>\d+)/$', needDetail, name='need_detail'),
        url(r'^need/(?P<pk>\d+)/delete/$', DeleteNeed.as_view(), name='delete_need'),
        url(r'^need/(?P<pk>\d+)/update/$', UpdateNeed.as_view(), name='update_need'),

        url(r'^orderrecord/create/$', createOrderRecord, name='create_order_record'),

        #管理状态监控
        url(r'^admin_needs/$', AdminNeedList.as_view(), name='admin_need_list'),
        url(r'^admin_need/(?P<pk>\d+)/$', adminNeedDetail, name='admin_need_detail'),
        url(r'^admin_need/(?P<pk>\d+)/delete/$', AdminDeleteNeed.as_view(), name='admin_need_delete'),
        )
