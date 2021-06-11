from django.urls import path,include
from .views import *

urlpatterns = [
    path('order/',order_page,name='order'),
    path('close_check/<int:order_id>/',close_check_page,name='close_check'),
    path('check_detail/<int:order_id>/',check_detail,name='check_detail'),
    path('meal_detail/<int:meal_id>/',meal_detail,name='meal_detail'),
    path('my_orders/',my_orders,name='my_orders'),
]