from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


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
            print(money,order.total_sum,payback)
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



