#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from qipei.apps.product.models import Products, Sorts
from qipei.apps.store.models import Stores

class StoresAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel')
    search_fields = ('name', 'description')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('it_name', 'version', 'exit_date')
    search_fields = ('it_name', 'company', 'series')
class SortsAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Stores, StoresAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Sorts, SortsAdmin)
