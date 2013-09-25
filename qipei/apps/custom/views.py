#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.db import IntegrityError
from django.views.generic import View, UpdateView
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, get_list_or_404

from notifications.signals import notify
from notifications.models import Notification


from .models import Custom
# from .forms import UpdateAavatar
from qipei.apps.store.models import Stores
from qipei.apps.account.form import LoginForm
from qipei.apps.account.form import RegisterForm
from qipei.apps.account.decorators import ver_not_login, ver_not_login_with_template
from ..account.tools import r2r, super_or_author
from .forms import CustomForm

@ver_not_login
def cus_login(request):
    '''登陆视图'''
    form = LoginForm()
    if request.method == 'POST':

        form=LoginForm(request.POST.copy())

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user=authenticate(username=username,password=password)

            if user:
                if user.is_active and user.is_staff is False:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
            else:
                errors = "用户不存在，或者密码错误！"

    return render_to_response("custom-login.html",locals(),context_instance=RequestContext(request))


def _login(request,username,password):
    '''登陆核心方法'''
    ret=False

    user=authenticate(username=username,password=password)

    if user:
        if user.is_active and user.is_staff is False:
            login(request, user)
            ret=True
        else:
            messages.add_message(request, messages.INFO, _(u'用户没有激活'))
    else:
        messages.add_message(request, messages.INFO, _(u'用户不存在, 或者密码错误！'))
    return ret

@ver_not_login
def register(request):
    '''注册视图'''
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST.copy())
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            re_password = form.cleaned_data["re_password"]
            real_name = form.cleaned_data["real_name"]
            if password == re_password:
                user = User.objects.create_user(username, email, password)
                user.is_staff = 0
                user.first_name=real_name
                user.save()
                try:
                    custom = Custom(user=user, is_custom = True)
                    custom.save()
                except IntegrityError:
                    last_user = User.objects.all().order_by('-id')[0]
                    last_user.delete()

                notify.send(User.objects.get(id=1),recipient=user, verb='register successfully!')

                _login(request, username, password)
                return HttpResponse('<script>alert("注册成功！");location.replace(document.referrer);;</script>')
            else:
                return HttpResponse('<script>alert("两次密码必须相同！");history.go(-1);</script>')
        else:
            reverse_lazy('404')
    else:
        reverse_lazy('501')

    return render_to_response("custom-register.html", locals(), context_instance = RequestContext(request))


class DetailSelf(View):

    template_name = "custom-page.html"

    def get(self, request):

        user = request.user

        if user.is_superuser or user.is_staff:
            return HttpResponseRedirect(reverse_lazy('admin_index'))
        else:
            custom =  Custom.objects.get(user=user.id)

            return render_to_response(self.template_name,locals(),
                                      context_instance=RequestContext(request))

def ver_is_custom(req):
    """
    判断是否是普通用户
    """
    try:

        custom = req.user.custom

        return custom

    except Custom.DoesNotExist:

        return HttpResponse('<script>alert("您不是普通用户, 无法使用本功能！");location.replace(document.referrer);</script>')

def mark(request, store_id=False, product_id=False):

    custom = ver_is_custom(request)

    if store_id:
        custom.add_to_mark(store_id=int(store_id))
    elif product_id:
        custom.add_to_mark(product_id=int(product_id))
    else:
        raise Http404

    return HttpResponse('<script>alert("收藏成功！");location.replace(document.referrer);</script>')



def un_mark(request,  store_id, product_id):

    custom = ver_is_custom(request)

    if store_id:
        custom.remove_from_mark(store_id=int(store_id))
    elif product_id:
        custom.remove_from_mark(product_id=int(product_id))
    else:
        raise Http404

    return HttpResponse('<script>alert("已取消收藏！");location.replace(document.referrer);</script>')


@login_required(login_url='/custom/login/')
def update_self(request):

    custom_instance = get_object_or_404(Custom, id=request.user.user_info.id)

    form = CustomForm(request.POST or None, instance=custom_instance)

    if request.method == "POST":

        form = CustomForm(request.POST)

        print form

        if form.is_valid():

            cus = form.save(commit=False)
            cus.user = request.user
            cus.save()

            return HttpResponseRedirect(reverse_lazy('custom_page'))

        else:
            return HttpResponse('<script>alert("修改失败！");location.replace(document.referrer);</script>')


    return render_to_response('custom-update.html',locals(),
                              context_instance = RequestContext(request))


from upload_avatar import get_uploadavatar_context

@login_required(login_url='/custom/login/')
def update_avatar(request):

    return r2r(request, 'update_avatar.html', get_uploadavatar_context())



# def update_self(request):
#
#     custom = request.user.custom


@login_required(login_url='/custom/login/')
def get_notify(request):

    return r2r(request, 'custom-notifications.html', locals())



def detail_notify(request, notify_id):

    notify = get_object_or_404(Notification, id=notify_id)

    super_or_author(request, user_id=notify.recipient_id)

    return r2r(request, 'custom-detail-notify.html', locals())

def manage_notify(request, notify_id=False, unread=None, mark_all=False):
    """
    管理通知， 包括显示所用通知，标记已读，标记未读
    标记全部已读
    """
    if notify_id:

        notify = get_object_or_404(Notification, id=int(notify_id))
        super_or_author(request, user_id=notify.recipient_id)

        if unread == True:
            notify.mark_as_read()
        elif unread == False:
            notify.unread = True
            notify.save()

    if mark_all:
        request.user.notifications.mark_all_as_read()

    return r2r(request, 'custom-notifications.html', locals())
