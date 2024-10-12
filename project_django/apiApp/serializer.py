
from rest_framework import serializers

from apiApp.models import Category, Product


# Serializers: Using for convert date(DB) to json
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'