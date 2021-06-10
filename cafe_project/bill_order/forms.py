from django import forms
from .models import *



class MealToOrderForm(forms.ModelForm):
    class Meta:
        model = MealToOrder
        fields = ['meal','quantity']


class BillForm(forms.Form):
    change_status = forms.ChoiceField(choices=(
        ('yes','yes'),
        ('no','no'),
    ))
    client_money = forms.IntegerField()