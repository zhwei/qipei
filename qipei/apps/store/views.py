#!/usr/bin/env python
# -*- coding: utf-8 -*-

#coding=utf-8
#from django.core.urlresolvers import reverse
#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic import View, ListView, UpdateView, DetailView, DeleteView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

from qipei.apps.store.models import Stores
from qipei.apps.account.models import Links
from qipei.apps.product.models import Products, Sorts
from qipei.apps.store.forms import EditStoreForm, StoreAdForm, StoreForm


# @user_passes_test(lambda u: u.is_superuser)
class List(ListView):
    queryset = Stores.objects.all()
    template_name = "list_stores.html"
    context_object_name = "foo"

# @user_passes_test(lambda u: u.is_superuser)
# class Create(CreateView):
#     model = Stores
#     template_name = "create_store.html"
#     form_class = StoreForm
#     context_object_name = "foo"
#     success_url = reverse_lazy("list_store")


# @user_passes_test(lambda u: u.is_superuser)
class Detail(DetailView):
    model = Stores
    template_name = "detail_store.html"
    context_object_name = "store"

# 用于商户查看自己的信息.

# class DetailSelf(View):
#     template_name = "detail_store.html"
#
#     @user_passes_test(lambda u: u.is_staff)
#     def get(self, request):
#         foo = {}
#         foo["store"] =  Stores.objects.get(boss=request.user.id)
#         return render_to_response(self.template_name,foo,context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_staff)
def detail_self(request):

    store = get_object_or_404(Stores, boss=request.user.id)

    return render_to_response('detail_store.html', locals(),
                              context_instance=RequestContext(request))

# @user_passes_test(lambda u: u.is_superuser)
class Update(UpdateView):
    model = Stores
    template_name = "update_store.html"
    #form_class = EditStoreForm
    context_object_name = "foo"
    success_url = reverse_lazy("list_store")

#class UpdateSelf(View):
#    template_name = "update_store.html"
#    def get(self, request):

@login_required()
@user_passes_test(lambda u: u.is_staff)
def updateSelf(request):
    store_instance = Stores.objects.get(boss_id =request.user.id)
    form = EditStoreForm(request.POST or None, instance = store_instance)
    if form.is_valid():
        form.save()
        return reverse_lazy('detail_self_store')
    return render_to_response('update_store.html', locals(),
                              context_instance=RequestContext(request))

#@user_passes_test(lambda u: u.is_superuser)
#class UpdateAd(UpdateView):
#    model = Stores
#    template_name = "update_store_ad.html"
#    form_class = StoreAdForm
#    context_object_name = "foo"
#    success_url = reverse_lazy("success")
#

#@user_passes_test(lambda u: u.is_staff)
#def update_store_ad(request, store_id):
#
#    store_instance = get_object_or_404(Products, id=store_id)
#
#
#    form = StoreAdForm(request.POST or None, instance=store_instance)
#
#    if request.method == "POST":
#        form = StoreAdForm(request.POST.copy())
#        if form.is_valid():
#            form.save()
#
#    return render_to_response('update_store_ad.html', locals(),
#                              context_instance=RequestContext(request))
#

@user_passes_test(lambda u: u.is_staff)
def delete_store(request, store_id):

    foo = get_object_or_404(Products, id=store_id)

    return render_to_response("confirm_delete.html", locals(),
                              context_instance = RequestContext(request))


@user_passes_test(lambda u: u.is_staff)
def update_store_ad(request):
    """
    商户用来修改广告及logo
    """
    target_user = request.user.id
    store = Stores.objects.get(boss_id = target_user)
    form = StoreAdForm(request.POST, request.FILES, instance = store)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return  render_to_response('update_store_ad.html',locals(),
            context_instance=RequestContext(request))


class Index(View):
    """
    商铺首页显示
    """
    template_name = "index/index_store.html"

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id = store_id)
        owner = User.objects.get(id=store.boss_id)
        products = Products.objects.filter(company = store)
        links = Links.objects.all()
        return render_to_response(self.template_name, locals(),
                context_instance = RequestContext(request))


def detail_product(request, store_id, prod_id):
    """
    前台显示单个商品
    """
    store = get_object_or_404(Stores,id=store_id)
    product = get_object_or_404(Products, id = prod_id)
    return render_to_response('index/detail_product.html',locals(),
            context_instance=RequestContext(request))


def classfiy(request, store_id, sort_id):
    """
    商铺产品分类显示
    """
    store = get_object_or_404(Stores,id=store_id)
    if sort_id == "0":
        sorts = Sorts.objects.filter(level = 0)
        products  = Products.objects.filter(company = store )
    elif sort_id:
        sorts = Sorts.objects.filter(id=sort_id)
        products  = Products.objects.filter(company = store , sort = sort_id)

    all_sorts = Sorts.objects.all().order_by('-id')[:4]
        

    return render_to_response("index/classfiy.html",locals(),
            context_instance = RequestContext(request))

def comment(request, store_id):

    store = get_object_or_404(Stores,id=store_id)

    return render_to_response("comment.html", locals(),
            context_instance = RequestContext(request))
