from rest_framework import serializers

from apiApp.models import Category


# Serializers: Using for convert date(DB) to json
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
