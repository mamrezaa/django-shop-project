from rest_framework import serializers
from .models import Tags
from products.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Tags
        fields = ['id', 'title', 'description', 'active', 'slug', 'products']