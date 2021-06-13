from django.contrib.auth.models import AnonymousUser
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from content.models import Meal
from review.forms import CommentForm
from review.models import Review


def order_page(request):
    order_formset = formset_factory(MealToOrderForm,extra=3)
    user = request.user
    form = order_formset()
    if request.method == 'POST':
        form = order_formset(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            order = Order(user=user)
            order.save()
            total_sum = 0
            for data in cleaned_data:
                if data:
                    total_sum += data['meal'].price * data['quantity']

                    MealToOrder.objects.create(order=order,meal=data['meal'],quantity=data['quantity'])
            order.total_sum = total_sum
            order.save()
            return redirect('my_orders')
    return render(request,'order_page.html',{'form':form})



def close_check_page(request,order_id):
    form = BillForm()
    order = Order.objects.get(id=order_id)
    if order.status == 'closed':
        return HttpResponse('Check is closed!')
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            status_change = form.cleaned_data.get('change_status')
            money = form.cleaned_data.get('client_money')
            payback = money - order.total_sum
            if status_change == 'yes' and money >= order.total_sum:
                Bill.objects.create(order=order,client_money=money,payback=payback)
                order.status = 'closed'
                order.save()
                return redirect('check_detail', order_id)
            else:
                return HttpResponse('Неверные данные')


    return render(request,'close_check.html',{'form':form})



def check_detail(request,order_id):
    check = Bill.objects.get(order__id=order_id)
    return render(request,'check_detail.html',{'check':check})



def meal_detail(request,meal_id):
    meal = Meal.objects.get(id=meal_id)
    comment = meal.review_set.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            user = request.user
            Review.objects.create(meal=meal,text=text,user=user)

    return render(request,'meal_detail.html',{'meal':meal,'form':form,'comment':comment})



def my_orders(request,):
    user = request.user
    if isinstance(user, AnonymousUser):
        return HttpResponse('Please login!')
    order = Order.objects.filter(user=user)
    meal_to_order = MealToOrder.objects.filter(order__in=order)
    return render(request, 'my_orders.html', {'order': order,'mto':meal_to_order})



