from django.contrib.auth.models import User
from django.db import models
from content.models import Meal

class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    total_sum = models.IntegerField(default=0)
    status = models.CharField(max_length=30, choices=(
        ('in_process', 'in_process'),
        ('closed', 'closed'),
    ),default='in_process')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Bill(models.Model):
    order = models.OneToOneField(Order,on_delete=models.SET_NULL,null=True)
    client_money = models.IntegerField(default=0)
    payback = models.IntegerField(default=0)



class MealToOrder(models.Model):
    meal = models.ForeignKey(Meal,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0)
