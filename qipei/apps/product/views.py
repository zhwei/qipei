#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from django.http import Http404
from django.template import RequestContext
from django.contrib.comments import Comment
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response, redirect, get_object_or_404

from .models import Sorts,Products
from .forms import  AddForm, ProductsStaffForm, ProductsForm
from ..account.tools import delete


##############################工具函数############################
#验证是否是正整数
def IsNUM(varObj):
    rule = '^\+?[1-9][0-9]*$'
    match = re.match( rule , varObj )
    if match:
        return True
    return False


##################################################################

#添加商品

@user_passes_test(lambda u: u.is_staff)
def create_product(request):
    user = request.user
    form = ProductsStaffForm()
    form['sort'].field.help_text ='<p class="alert alert-info">按下Ctrl键支持多选</p>'
    form['exit_date'].field.help_text ='<p class="alert alert-info">日期格式<strong><em>2012-12-21</em></strong></p>'
    product = Products()
    if request.method =='POST':
        form = ProductsStaffForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit = False)
            product.company = user.stores
            product.save()
            #return reverse_lazy("list_product")
            return redirect(list_product)

    return  render_to_response('create_product.html',locals(),context_instance=RequestContext(request))


# 添加商品 
#def create_product(request):
#    """
#    商户添加商品
#    """
#    form = 


#管理商品
@user_passes_test(lambda u: u.is_staff)
def list_product(request):

    if request.user.is_superuser:
        products = Products.objects.all()
    elif request.user.is_staff:
        products = Products.objects.filter(company=request.user.stores)
    else:
        return HttpResponseRedirect(reverse("404"))

    return render_to_response("list_product.html",locals(),
                              context_instance=RequestContext(request))



@user_passes_test(lambda u: u.is_staff)
def update_product(request, product_id):

    """
    管理员删除任何商品
    商户删除自己的商品
    """

    product_instance = get_object_or_404(Products, id=product_id)

    if request.user.is_superuser or request.user == product_instance.company.boss_id:
        pass
    else:
        raise Http404

    form = ProductsForm(request.POST or None, instance=product_instance)

    if request.method == "POST":
        form = ProductsForm(request.POST.copy())
        if form.is_valid():
            form.save()

    return render_to_response('update_product.html', locals(),
                              context_instance=RequestContext(request))




@user_passes_test(lambda u: u.is_staff)
def delete_product(request, product_id):

    product = get_object_or_404(Products, id=product_id)

    if request.user.is_superuser:
        foo = product

    elif request.user.is_staff and product.company.boss == request.user:

        foo = product

    else:
        raise Http404

    return delete(request, foo, 'list_product')


#显示分类
@user_passes_test(lambda u: u.is_staff)
def show_sort(request):
    return render_to_response("list_sort.html",
        {'nodes':Sorts.objects.all()},
        context_instance=RequestContext(request))

#添加子分类
@user_passes_test(lambda u: u.is_staff)
def add_sort(request,parent):
    template_var={}
    form = AddForm()

    if request.method=="POST":
        form = AddForm(request.POST.copy())
        if form.is_valid():
            if parent!="root" and parent:
                sortname=form.cleaned_data['name']
                parent = Sorts.objects.get(id=parent)
                Sorts.objects.create(name=sortname,parent=parent,)
                return HttpResponseRedirect(reverse("list_sort"))

            elif parent == "root":
                sortname=form.cleaned_data['name']
                Sorts.objects.create(name=sortname)
                return HttpResponseRedirect(reverse("list_sort"))
            else:
                return HttpResponse('<script>alert("填写错误!");history.go(-1);</script>')
    template_var['par']=parent
    template_var['form']=form
    return  render_to_response("create_sort.html",template_var,context_instance=RequestContext(request))


#删除
@user_passes_test(lambda u: u.is_staff)
def dele(request, id, model):
    if IsNUM(id):
        p=model.objects.get(id=id)
        if p:
            p.delete()
        else:
            return HttpResponse('<script>alert("删除对象不存在");top.location="/accounts/index";</script>')
        return HttpResponse('<script>alert("删除成功");location.href=document.referrer;</script>')
    else:
        return HttpResponse('<script>alert("删除错误!");top.location="/accounts/index";</script>')


#messages
def comments(request):
    if request.user.is_superuser:
        comments=Comment.objects.all()
    elif request.user.is_staff:
        user_id=request.user.id
        comments=Comment.objects.filter(user=user_id)
    else:
        return HttpResponseRedirect(reverse("404"))
    template_var={
        'comments':comments,
    }
    return render_to_response('comments.html',template_var,context_instance=RequestContext(request))
