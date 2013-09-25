#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from qipei.apps.product.models import Sorts,Products
#from qipei.apps.store.models import Stores
from qipei.apps.account.models import Links
#from qipei.apps.store.forms import EditStoreForm, StoreAdForm
#from django.contrib.comments import Comment
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from django.core.urlresolvers import reverse_lazy





urlpatterns = patterns('qipei.apps.product',
    ## products
    url(r'^create$',
        CreateView.as_view(
            model=Products,
            template_name="create_product.html",
            success_url=reverse_lazy("list_product")
        ),
        name="create_product",
    ),
    url(r'^create/self$', 'views.create_product', name="create_self_product"),
    url(r'^list$', 'views.list_product', name="list_product"),
    # url(r'^update/(?P<pk>\d+)$',
    #     UpdateView.as_view(
    #         model = Products,
    #         template_name="update_product.html",
    #         success_url = reverse_lazy("manage_products")
    #         ),
    #     name="update_product"
    # ),
    url(r'^update/(?P<product_id>\d+)$','views.update_product', name="update_product",),

    #### 删除多个model
    url(r'^delete/(?P<product_id>\d+)$','views.delete_product', name="delete_product",),


    ## 分类
    url(r'^sort/list$','views.show_sort',name="list_sort"),
    url(r'^sort/create/(?P<parent>\w+)/$','views.add_sort',name="create_sort"),
    url(r'^sort/delete/(?P<pk>\d+)/$',
        DeleteView.as_view(
            model=Sorts,
            context_object_name="foo",
            template_name="confirm_delete.html",
            success_url=reverse_lazy("list_sort"),
        ),
        name="delete_sort",
     ),


    ## 友情链接
    url(r'^links/list$',
        ListView.as_view(
            queryset=Links.objects.all(),
            context_object_name="links",
            template_name="list_link.html",
        ),
        name='list_link'
    ),
    url(r'^links/create',
        CreateView.as_view(
            model=Links,
            template_name="create_link.html",
            success_url=reverse_lazy("list_link"),
        ),
        name='create_link'
    ),
    url(r'^links/delete/(?P<pk>\d+)/$',
        DeleteView.as_view(
            model=Links,
            context_object_name="foo",
            template_name="confirm_delete.html",
            success_url=reverse_lazy("list_link"),
        ),
        name="delete_link",
     ),
)
