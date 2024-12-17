from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    pro_name=models.CharField(max_length=30)
    image=models.FileField()
    price=models.IntegerField()
    offer_price=models.IntegerField()


# class Cart(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     Product=models.ForeignKey(products,on_delete=models.CASCADE)

# class buy(models.Model):