from django.contrib import admin
from .models import *

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','meal','date_created','text']

admin.site.register(Review,ReviewAdmin)
