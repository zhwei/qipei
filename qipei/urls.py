#coding:utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

# from qipei

urlpatterns = patterns('',
    # url(r'^$', 'qipei.views.home', name='home'),
    # url(r'^qipei/', include('qipei.foo.urls')),
    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #search
    #(r'^search/', include('haystack.urls')),
    #需求相关url
    url(r'', include('qipei.apps.need.urls')),
    # accounts
    url(r'^accounts/', include("qipei.apps.account.urls")),
    # stores
    url(r'^store/', include("qipei.apps.store.urls")),
    # product
    url(r'^product/',include("qipei.apps.product.urls")),
    # custom
    url(r'^custom/',include("qipei.apps.custom.urls")),

    # forum
    url(r'^forum/',include("qipei.apps.forum.urls")),

    # welcome
    url(r'^wel/',include("qipei.apps.welcome.urls")),

    url(r'^$','qipei.apps.welcome.views.index'),
    # success page
    url(r'^ok',TemplateView.as_view(template_name="ok.html",),name='success'),

    url(r'^ueditor/', include('DjangoUeditor.urls')),

    url(r'', include('upload_avatar.urls')),

    url(r'^inbox/notifications/', include('notifications.urls')),



    # media managment
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
