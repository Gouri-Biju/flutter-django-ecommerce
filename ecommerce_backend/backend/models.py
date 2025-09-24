from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    hname=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)

class Products(models.Model):
    pname=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.FileField(upload_to='product_images')
    last_updated=models.DateTimeField()

class OrderMaster(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    total=models.IntegerField()
    status=models.CharField(max_length=100)
    date=models.DateTimeField()

class OrderDetails(models.Model):
    ordermaster=models.ForeignKey(OrderMaster,on_delete=models.CASCADE)
    pid=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()

