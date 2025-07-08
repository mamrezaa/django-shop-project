from rest_framework import serializers
from .models import Products, ProductGallery, Category
from products_category.models import Category

class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ['image', 'title']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # اسم فیلد title هست ولی توی مدل Category شما name هست


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    gallery = ProductGallerySerializer(source='productgallery_set', many=True)

    class Meta:
        model = Products
        fields = ['id', 'title', 'description', 'price', 'active', 'category', 'gallery']