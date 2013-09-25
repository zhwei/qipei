#!/usr/bin/env python2.7
#coding=utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from qipei.apps.product.models import Products, Sorts
from qipei.apps.account.models import Links
from qipei.apps.store.models import Stores
from django.contrib.auth.models import User

def index(request):

    products = Products.objects.all().order_by("-id")[:5]
    links = Links.objects.all()
    sorts = Sorts.objects.filter(parent_id = None)
    stores = Stores.objects.all().order_by("-id")[:10]
    users = User.objects.filter(is_active=1, is_staff=0).order_by("-id")[:10]

    return render_to_response("index.html", locals(), context_instance = RequestContext(request))



def classfiy(request, sort_id):
    """
    商铺产品分类显示
    """
    if sort_id == "0":
        sorts = Sorts.objects.filter(level = 0)
        products  = Products.objects.all()
    elif sort_id:
        sorts = Sorts.objects.filter(id=sort_id)
        products  = Products.objects.filter(sort = sort_id)

    all_sorts = Sorts.objects.all().order_by('-id')[:4]

    return render_to_response("index-classfiy.html",locals(),
            context_instance = RequestContext(request))
