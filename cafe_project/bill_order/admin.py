from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','status','date_created','total_sum']
    readonly_fields = ['total_sum','user']

admin.site.register(Order,OrderAdmin)


class BillAdmin(admin.ModelAdmin):
    list_display = ['order','client_money','payback','date_created']

admin.site.register(Bill,BillAdmin)


class MTOadmin(admin.ModelAdmin):
    list_display = ['meal','quantity','order']

admin.site.register(MealToOrder,MTOadmin)
