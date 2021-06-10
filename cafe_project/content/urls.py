from django.urls import path
from .views import *

urlpatterns = [
    path('meals/',meals_page,name='meals'),
    path('',homepage,name='home'),
    path('detail/<int:category_id>/',category_detail,name='detail'),
    path('register/',register_page,name='register'),
    path('login/',login_page,name='login'),
]