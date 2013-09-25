#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import patterns
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required


from qipei.apps.store.views import List, Detail,  Update, Index#, Create


urlpatterns = patterns('qipei.apps.store',

    url(r'^list$',List.as_view(),name="list_store"),

    # url(r'^create$',Create.as_view(),name="create_store"),

    url(r'^detail/(?P<pk>\d+)$',Detail.as_view(),name="detail_store"),

    url(r'^detail/self/$', 'views.detail_self',name="detail_self_store"),

    url(r'^update/(?P<pk>\d+)$',Update.as_view(),name="update_store",),

    url(r'^update/self/$','views.updateSelf',name="update_self_store"),

    url(r'^delete/(?P<store_id>\d+)$','views.delete_store',name="delete_store",),

    #ad
    url(r'^ad/update','views.update_store_ad',name="update_store_ad",),

    # 商铺首页展示
    url(r'^(?P<store_id>\d+)/$',Index.as_view(),name="store_index"),
    ## 商铺产品分类 & 查看单个商品
    url(r'^(?P<store_id>\d+)/classfiy/(?P<sort_id>\d+).html$','views.classfiy',name='index_store_classfiy'),
    url(r'^(?P<store_id>\d+)/view/(?P<prod_id>\d+).html$','views.detail_product',name='index_view_product'),

    url(r'^(?P<store_id>\d+)/comment.html$','views.comment',name='store_comment'),


    # 测试页面
    url(r'^test$',TemplateView.as_view(template_name = "index/classfiy.html"),name="test",),
)


#urlpatterns += patterns('qipei.apps.account',
#        
#        )
