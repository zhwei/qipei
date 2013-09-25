#coding:utf-8

from django.views.generic.edit import DeleteView 
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.contrib.auth.models import User
from models import OrderRecord, Need
from form import OrderRecordForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

def need_superuser(user):
    return  user.is_superuser


class AdminNeedList(ListView):
    model=Need
    context_object_name = 'needs'
    template_name='need/admin_need_list.html'

    @method_decorator(user_passes_test(need_superuser))
    def dispatch(self, *args, **kwargs):
        return super(AdminNeedList, self).dispatch(*args, **kwargs)

@user_passes_test(need_superuser)
def adminNeedDetail(request, pk):

    need = Need.objects.get(pk=pk)
    order_records = need.orderrecord_set.all()  

    if need:
        return render_to_response('need/admin_need_detail.html',
                {'need': need, 'order_records' : order_records},
                context_instance=RequestContext(request))
    else:
        raise Http404

class AdminDeleteNeed(DeleteView):
    model = Need
    success_url = reverse_lazy('admin_need_list')

    @method_decorator(user_passes_test(need_superuser))
    def dispatch(self, *args, **kwargs):
        return super(AdminDeleteNeed, self).dispatch(*args, **kwargs)
