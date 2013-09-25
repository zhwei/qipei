#!/usr/bin/env python2.7
#coding=utf-8

#from django.contrib import messages
from django.template import RequestContext
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from notifications.signals import notify

from .form import NotifyForm
from ..store.models import Stores
from ..custom.models import Custom
from .tools import alert_backup, r2r
from .decorators import ver_not_login
from .form import RegisterForm, ChangePasswordForm, CreateUserForm


@login_required
@user_passes_test(lambda u: u.is_staff)
def index(request):
    '''首页视图'''
    template_var = {"w": _(u"欢迎您 游客!")}
    if request.user.is_staff:
        template_var["w"] = _(u"欢迎您 %s!")%request.user.username
    return render_to_response("welcome.html", template_var, context_instance = RequestContext(request))


@ver_not_login
def register(request):
    '''注册视图'''
    template_var = {}
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
                user.first_name = real_name
                user.is_staff = 1
                user.is_active = 0
                user.save()
                #_login(request, username, password)
                #注册完毕 直接登陆
                return HttpResponse('<script>alert("提交成功，等待管理员认证！");top.location="/"</script>')
            else:
                return HttpResponse('<script>alert("两次密码必须相同！");history.go(-1);</script>')
    template_var["form"] = form

    return render_to_response("register.html", template_var, context_instance = RequestContext(request))



@login_required
def logout(request):
    '''注销视图'''
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))


# 管理用户，传递用户

def manUser(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("404"))


    store_user = User.objects.filter(is_staff=1,is_superuser=0, is_active=1).order_by('-date_joined')
    pre_store = User.objects.filter(is_staff=1,is_active=0)
    custom = User.objects.filter(is_staff= 0, is_active = 1)
    super_user=User.objects.filter(is_superuser=1)

    return render_to_response("list_user.html",locals(),context_instance=RequestContext(request))

# 审核用户并创建商铺

def passUser(request,pk):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("404"))
    if pk:
        user=User.objects.get(id=pk)
        user.is_staff= 1
        user.is_active = 1
        user.save()
        store_name = user.username
        store = Stores(name = store_name, boss=user)
        store.save()
        return HttpResponse('<script>alert("已通过！");top.location="/accounts/list"</script>')
    else:
        HttpResponseRedirect(reverse('list_user'))




class Delete(DeleteView):
    """
    删除用户
    """
    model = User
    template_name = "confirm_delete.html"
    context_object_name = "foo"
    success_url = reverse_lazy("list_user")
    



#更改用户密码

@login_required
def change_password(request):
    #if not request.user.is_authenticated():
    #    return HttpResponseRedirect(reverse("404"))
    template = {}
    form = ChangePasswordForm()
    if request.method=="POST":
        form = ChangePasswordForm(request.POST.copy())
        if form.is_valid():
            username = request.user.username
            oldpassword = form.cleaned_data["old_password"]
            newpassword = form.cleaned_data["new_password"]
            newpassword1 = form.cleaned_data["new_password1"]
            user = authenticate(username=username,password=oldpassword)
            if user: #原口令正确
                if newpassword == newpassword1:#两次新口令一致
                    user.set_password(newpassword)
                    user.save()
                    print '1'
                    return HttpResponse('<script>alert("修改密码成功！");top.location="/account/index";</script>')
                else:#两次新口令不一致
                    template["word"] = '两次输入口令不一致'
                    template["form"] = form
                    print '2'
                    return render_to_response("change_password.html",template,
                                              context_instance=RequestContext(request))
            else:  #原口令不正确
                if newpassword == newpassword1:#两次新口令一致
                    template["word"] = '原口令不正确'
                    template["form"] = form
                    print '3'
                    return render_to_response("change_password.html",template,
                                              context_instance=RequestContext(request))
                else:#两次新口令不一致
                    template["word"] = '原口令不正确，两次输入口令不一致'
                    template["form"] = form
                    print '4'
                    return render_to_response("change_password.html",template,
                                              context_instance=RequestContext(request))
    template["form"] = form
    return render_to_response("change_password.html",template,
                              context_instance=RequestContext(request))




def create_user(request, t):
    """
    创建管理员、商户、普通用户
    """
    if request.user.is_superuser != True:
        raise Http404

    t = int(t)

    if t not in [1,2,3]:
        raise Http404

    title = {1:'添加商户', 2:'添加普通用户', 3:'添加管理员'}[t]

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST.copy())

        if form.is_valid() == True:
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            new_user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password)
            if t == 1:
                # 创建商户
                store = Stores.objects.create(boss=new_user,
                                              name=str(username)+"的商铺")
                new_user.is_staff, new_user.is_active = (True, True)
                new_user.save()
                return HttpResponse(alert_backup('创建成功！'))

            elif t == 2:
                # 创建普通用户
                custom = Custom.objects.create(user = new_user,
                                               is_custom = True)
                return HttpResponse(alert_backup('创建成功！'))

            elif t == 3:
                # 创建管理员
                new_user.is_staff, new_user.is_active = (True, True)
                new_user.is_superuser = True
                new_user.save()
                return HttpResponse(alert_backup('创建成功！'))

            else:
                raise Http404



    return render_to_response('create.html', locals(),
                                  context_instance=RequestContext(request))




def create_notify(request):

    if request.user.is_superuser != True:
        raise  Http404

    form = NotifyForm()

    title = '创建通知'

    if request.method == "POST":

        form = NotifyForm(request.POST)

        if form.is_valid():

            recipient_id = form.cleaned_data['recipient']
            recipient=get_object_or_404(User, id=recipient_id)

            verb = form.cleaned_data['verb']

            description = form.cleaned_data['description']

            notify.send(request.user, recipient=recipient,
                        verb=verb, description=description)

            return HttpResponseRedirect(reverse_lazy("create_notify"))

    return r2r(request, 'create.html', locals() )























