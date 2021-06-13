from django.contrib.auth.models import User
from django.db import models
from content.models import Meal

class Review(models.Model):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True)