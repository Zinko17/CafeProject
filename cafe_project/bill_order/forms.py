from django.forms import ModelForm
from .models import *


class MealToOrderForm(ModelForm):
    class Meta:
        model = MealToOrder
        fields = ['meal','quantity']