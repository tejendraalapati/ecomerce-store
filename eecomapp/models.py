from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    images=models.ImageField(upload_to='products')

    def _str_ (self):
        return self.title
    

class items(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    images=models.ImageField(upload_to='products')
    def _str_ (self):
        return self.title
    

class Cart(models.Model):
    products=models.ManyToManyField(items)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class contact(models.Model):
    Name=models.CharField(max_length=100)
    Phone_number=models.CharField(max_length=10)
    Email=models.EmailField(max_length=100)
    Message=models.TextField()

    
