from typing import Iterable
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=50)
    inStockQuantity = models.IntegerField()
    productPrice = models.IntegerField()

    def __str__(self) -> str:   
        return self.productName
    
class Bill(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    total = models.IntegerField(null = True)



class BilledProduct(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='billedProduct')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField()
    price = models.IntegerField(null = True)

    def save(self, *args, **kwargs):
        self.price = self.quantity*self.product.productPrice
        return super().save(*args, **kwargs)

