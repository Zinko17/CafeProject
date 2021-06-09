from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Meal(models.Model):
    photo = models.ImageField(default='soup.jpeg')
    ingredients = models.CharField(max_length=60)
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    gramms = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title


