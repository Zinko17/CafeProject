from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Category,CategoryAdmin)


class MealAdmin(admin.ModelAdmin):
    list_display = ['title','price','gramms','photo','ingredients','category']
admin.site.register(Meal,MealAdmin)
