from django.shortcuts import render
from .models import *

def meals_page(request):
    meal = Meal.objects.all()
    return render(request,'meals.html',{'meal':meal})


def homepage(request):
    category = Category.objects.all()
    return render(request,'category.html',{'category':category})


def category_detail(request,category_id):
    category = Category.objects.get(id=category_id)
    meal = category.meal_set.all()
    return render(request,'detail.html',{'category':category,'meal':meal})