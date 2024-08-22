
from django.db import models

class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class CartItem(models.Model):
    objects = None
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'


# Create your models here.

