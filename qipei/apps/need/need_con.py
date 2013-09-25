#coding:utf-8
from models import Need, OrderRecord
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse_lazy
from form import NeedForm
#from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import Http404
from django.contrib.auth.decorators import login_required

class NeedList(ListView):

    model = Need
    context_object_name = 'needs'


#class NeedDetail(DetailView):
#	
#	model = Need
#
#	def get_object(self):
#
#		object = super(NeedDetail, self).get_object()
#		object.order_records = object.orderrecord_set.all()
#
#		return object

def needDetail(request, pk):

    need = Need.objects.get(pk=pk)
    order_records = need.orderrecord_set.all()	

    # 判断是否显示接单按钮
    is_order = False
    is_dian = False
    if request.user.is_authenticated():
        user = User.objects.get(pk=request.user.id)
        if user.is_staff:
            is_dian = True
            if OrderRecord.objects.filter(user=request.user.id, need=pk):
                is_order = True
    if need:
        return render_to_response('need/need_detail.html',
                {'need': need, 'is_order': is_order, 'is_dian': is_dian, 'order_records' : order_records},
                context_instance=RequestContext(request))
    else:
        raise Http404


class UpdateNeed(UpdateView):

    model = Need
    form_class = NeedForm

#class CreateNeed(CreateView):
#	model = Need
class CreateNeed(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            f = NeedForm()
            return render_to_response('need/need_form.html', {'form':f}, context_instance=RequestContext(request))
        else:
            return HttpResponse('需要登录')

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated():
            return HttpResponse("需要登录")

        f = NeedForm(request.POST)
        if not f.is_valid():
            return HttpResponseRedirect('/need/create/')

        need = Need()
        need.car_type  = f.cleaned_data['car_type']
        need.short_dsc = f.cleaned_data['short_dsc']
        need.long_dsc  = f.cleaned_data['long_dsc']
        need.user      = request.user
        need.save()
        return HttpResponseRedirect('/needs/')

class DeleteNeed(DeleteView):

    model = Need
    success_url = reverse_lazy('need_list')
