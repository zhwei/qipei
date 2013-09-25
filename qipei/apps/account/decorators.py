__author__ = 'zhwei'


from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy



def ver_login(func):
    def ver(*args):
        request = args[0]
        if request.user.is_authenticated():
            return func(request)
        else:
            return HttpResponseRedirect(reverse_lazy('index'))
    return ver

def ver_not_login(func):
    def ver(*args):
        request = args[0]
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            return func(request)
    return ver

def ver_not_login_with_template(func):
    def ver(*args, **kwargs):
        request = args[0]
        template_name = kwargs['template_name']
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            return func(request, template_name)
    return ver