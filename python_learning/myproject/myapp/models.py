# from datetime import datetime
import datetime
from collections import deque

from django.db import models


class Category(models.Model):
    # id = models.AutoField(primary_key=True)  # Automatically creates an integer ID
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Product(models.Model):
    # id = models.AutoField(primary_key=True)
    product_name = models.CharField(unique=True, null=False, blank=True)
    barcode = models.BigIntegerField(unique=True, null=False, blank=True)
    sell_price = models.FloatField(null=True, blank=True)
    qty_in_stock = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='media/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_by = models.IntegerField(null=False, blank=False)
    update_by = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now=datetime.datetime.now())
    update_at = models.IntegerField(null=True, blank=True)

# null=False, is not empty
