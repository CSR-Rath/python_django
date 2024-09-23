from datetime import datetime
from unicodedata import name

from django.db import models
from rest_framework.authtoken.admin import User


# maxlength numner
# unique = true only one name
# null=False need value not null or empty

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=35, unique=True, null=False)

    # createBy = models.ForeignKey(User, on_delete=models.CASCADE.null=True)
    # updateBy = models.IntegerField(null=True)
    # createAt = models.DateField(auto_now_add = datetime.datetime.now())
    # updateAt = models.DateField(null=True)

# class Product(models.Model):
#     name = models.CharField(max_length=20, unique=True, null=False)
#     barcode = models. IntegerField(unique=True, null=False)
#     unitPrice = models. FloatField(null=False)
#     qtyInstock = models.IntegerField(null=False)
#     photo = models.ImageField(upload_to="media/", null=False)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     createBy = models.ForeignKey(User, on_delete=models.CASCADE)
#     updateBy = models.IntegerField(null=True)
#     createAt = models.DateField(auto_now_add = datetime.datetime.now())
#     updateAt = models.DateField(null=True)
