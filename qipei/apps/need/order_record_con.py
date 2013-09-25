#coding:utf-8
from django.views.generic.edit import DeleteView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from models import OrderRecord
from django.core.urlresolvers import reverse_lazy
from form import OrderRecordForm
from django.contrib.auth.decorators import login_required

@login_required
def createOrderRecord(request):

    if request.method == 'GET':
        return HttpResponse('only post')

    f = OrderRecordForm(request.POST)

    if f.is_valid():
        need = f.cleaned_data['need']
        user_id = request.user
        if OrderRecord.objects.filter(user = user_id, need = need):
            return HttpResponse('<script type="text/javascript">alert("已经接过单啦")</script>')

        o = OrderRecord(user = user_id, need = need)
        o.save()
        return HttpResponseRedirect('/need/%s/' % (need.id))
    else:
        return HttpResponse('输入错误')
