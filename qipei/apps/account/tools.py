#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
各种工具函数
"""

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse, HttpResponseRedirect




def alert_backup(content):

    """
    弹框并后退到请求页面
    """

    js = '<script>alert("%s");location.replace(document.referrer);</script>' % content

    return str(js)


def alert_reload(content):

    """
    弹框并刷新本页
    """

    js = '<script>alert("%s");window.location.reload();</script>' % content

    return str(js)




def delete(request, obj=False, success_url='index', url_kwargs=None):

    """
    删除函数， 用于删除操作
    -------
    obj 被删除的实例 eg： subject = get_object_or_404(Subject, id=subject_id)
    success_url 删除成功后的跳转页面，直接写 url的name属性， 支持参数通过url_kwargs
    传入， 格式为 {"subject_id": subject_id}
    """

    if obj:

        foo = obj

        if request.method == "POST":

            post = request.POST.get('post', '')

            if post == "yes":

                obj.delete()

                if url_kwargs != None:
                    return HttpResponseRedirect(reverse_lazy(success_url, kwargs=url_kwargs))
                else:
                    return HttpResponseRedirect(reverse_lazy(success_url))
            else:
                raise Http404

    else:
        raise Http404


    return render_to_response('confirm_delete.html', locals(),
                              context_instance=RequestContext(request))


def super_or_author(request, obj=None, user_id=None):

    """
    判断请求者是管理员或者是文章或者主题的作者
    外键是 user或者 传入 user_id
    """
    if user_id:
        user_id = user_id
    else:
        user_id = obj.user_id

    if request.user.is_superuser:
        pass
    elif request.user.id == user_id:
        pass
    else:
        raise Http404


def r2r(request, template_name, local):

    """
    方便使用 render_to_response
    """

    return render_to_response(template_name, local,
                              context_instance = RequestContext(request))