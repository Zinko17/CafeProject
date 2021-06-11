from django import forms
from .models import *


class CommentForm(forms.Form):
    text = forms.CharField()