from django.contrib import admin
from django.contrib.auth.models import User
from models import Need, OrderRecord


class NeedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Need,NeedAdmin)

class OrderRecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrderRecord,OrderRecordAdmin)
