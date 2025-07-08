from rest_framework import serializers
from .models import Order, OrderDetail
from products.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title', 'price']


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = OrderDetail
        fields = ['product', 'count', 'price', 'product_sum_in_cart']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product_sum_in_cart'] = instance.product_sum_in_cart()
        return data


class OrderSerializer(serializers.ModelSerializer):
    orderdetail_set = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'paid', 'pay_date', 'orderdetail_set', 'get_total_price']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['total_price'] = instance.get_total_price()
        return data