from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image=models.ImageField(null=True,blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    reviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    inStock = models.IntegerField(null=True, blank=True, default=0)
    CreatedAt = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)


    def __str__(self) -> str:
        return self.name