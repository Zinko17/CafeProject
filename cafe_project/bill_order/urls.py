from django.urls import path,include
from .views import *

urlpatterns = [
    path('order/',order_page,name='order')
]