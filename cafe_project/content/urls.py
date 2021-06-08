from django.urls import path
from .views import *

urlpatterns = [
    path('meals',meals_page,name='meals'),
    path('',homepage,name='home'),
    path('detail/<int:category_id>',category_detail,name='detail'),
]