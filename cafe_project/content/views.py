from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm

def meals_page(request):
    meal = Meal.objects.all()
    return render(request,'meals.html',{'meal':meal})


def homepage(request):
    category = Category.objects.all()
    return render(request,'category.html',{'category':category})


def category_detail(request,category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
       return HttpResponse('404')
    meal = category.meal_set.all()
    return render(request,'detail.html',{'category':category,'meal':meal})


def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'register.html',{'form':form})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'login.html')



