from django.db import models

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=50, unique=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    qty_in_stock = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='photos/', null=True)  # Requires Pillow library

    # photo = models.ImageField(upload_to='photos/')  # Requires Pillow library
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
