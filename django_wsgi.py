#!/usr/bin/env python
import os  
os.environ['DJANGO_SETTINGS_MODULE'] = 'qipei.settings'  
import django.core.handlers.wsgi  
application = django.core.handlers.wsgi.WSGIHandler()
