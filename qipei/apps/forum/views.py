#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.db import IntegrityError
from django.template import RequestContext
from django.views.generic import View, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import DetailView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404

from qipei.apps.custom.models import Custom
from qipei.apps.store.models import Stores
from qipei.apps.account.form import LoginForm
from qipei.apps.account.form import RegisterForm
from qipei.apps.account.decorators import ver_not_login

from .models import Subject, Reply
from .forms import SubjectForm, ReplyForm
from ..account.tools import alert_reload, alert_backup, delete, super_or_author

def list_subject(request):

    """
    列出所有专家讲座
    """
    subject = Subject.objects.all()

    return render_to_response('list_subject.html',locals(),
                              context_instance = RequestContext(request))


@user_passes_test(lambda u: u.is_staff)
def create_subject(request):

    form = SubjectForm()

    if request.method == 'POST':

        form  = SubjectForm(request.POST, request.FILES)

        if form.is_valid():

            subject = form.save(commit=False)

            subject.user = request.user

            subject.save()

            return HttpResponseRedirect(reverse_lazy('list_subject'))

    return render_to_response('create_subject.html',locals(),
                              context_instance = RequestContext(request))

@login_required(login_url='/custom/login')
def reply_subject(request, subject_id):

    """
    对某一条主题创建回复
    """

    subject = get_object_or_404(Subject, id=subject_id)

    replys = subject.reply_set.all()

    form = ReplyForm()

    if request.method == 'POST':

        form = ReplyForm(request.POST, request.FILES)

        if form.is_valid:
            replay = form.save(commit=False)

            replay.user = request.user

            replay.subject = subject

            replay.save()

            js = '<script>alert("回复成功!");top.location="/forum/subject/%s";</script>' \
                 % str(subject_id)

            return HttpResponse(js)


    return render_to_response('reply_subject.html',locals(),
                              context_instance = RequestContext(request))




def delete_subject(request, subject_id):

    obj = get_object_or_404(Subject, id=subject_id)

    super_or_author(request, obj)

    return delete(request, obj, 'list_subject')

def delete_reply(request, reply_id):

    reply = get_object_or_404(Reply, id=reply_id)

    super_or_author(request, reply)

    return delete(request, obj=reply, success_url='detail_subject',
                  url_kwargs= {'subject_id' : reply.subject_id, })




def update_subject(request, subject_id):

    subject_instance = get_object_or_404(Subject, id=subject_id)

    super_or_author(request, subject_instance)

    form = SubjectForm(request.POST or None, instance=subject_instance)

    if request.method == "POST":
        form = SubjectForm(request.FILES)

        if form.valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('detail_subject',
                                                     kwargs={'subject_id': subject_id}))

    return render_to_response('update_forum.html', locals(),
                              context_instance=RequestContext(request))



def update_reply(request, reply_id):

    reply_instance = get_object_or_404(Reply, id=reply_id)

    super_or_author(request, reply_instance)

    form = ReplyForm(request.POST or None, instance=reply_instance)

    if request.method == "POST":
        form = ReplyForm(request.POST, request.FILES)

        if form.valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('detail_subject',
                                        kwargs={'subject_id':reply_instance.subject_id}))

    return render_to_response('update_forum.html', locals(),
                              context_instance=RequestContext(request))





















