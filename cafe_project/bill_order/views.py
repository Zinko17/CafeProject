from django.forms import formset_factory
from django.shortcuts import render
from .models import *
from .forms import *


def order_page(request):
    order_formset = formset_factory(MealToOrderForm,extra=3)
    form = order_formset()
    if request.method == 'POST':
        form = order_formset(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            order = Order()
            order.save()
            total_sum = 0
            for data in cleaned_data:
                total_sum += data['meal'].price * data['quantity']

                MealToOrder.objects.create(order=order,meal=data['meal'],quantity=data['quantity'])
            order.total_sum = total_sum
            order.save()
    return render(request,'order_page.html',{'form':form})
