from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Order, OrderDetail
from products.models import Products
from .serializers import OrderSerializer, OrderDetailSerializer



@api_view(['GET'])
def user_cart_api(request):
    # ✅ چک کردن کاربر لاگین
    if not request.user.is_authenticated:
        return Response({
            "status": "error",
            "message": "شما باید وارد حساب کاربری خود شوید."
        }, status=status.HTTP_401_UNAUTHORIZED)

    # گرفتن سبد کاربر
    open_order = Order.objects.filter(user=request.user, paid=False).first()

    if not open_order:
        return Response({
            "status": "empty",
            "message": "سبد خرید شما خالی است."
        }, status=status.HTTP_200_OK)

    serializer = OrderSerializer(open_order)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_to_cart_api(request):
    product_id = request.data.get('product_id')
    count = request.data.get('count', 1)

    # چک کردن محصول
    product = get_object_or_404(Products, id=product_id)

    # ساخت یا گرفتن سفارش فعال
    order, created = Order.objects.get_or_create(user=request.user, paid=False)

    # اضافه کردن به سبد
    try:
        order_detail = order.orderdetail_set.get(product=product)
        order_detail.count += int(count)
        order_detail.save()
    except OrderDetail.DoesNotExist:
        order.orderdetail_set.create(
            product=product,
            count=count,
            price=product.price
        )

    return Response({
        'status': 'success',
        'message': 'محصول با موفقیت به سبد اضافه شد.'
    }, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def remove_from_cart_api(request, detail_id):
    detail = get_object_or_404(OrderDetail, id=detail_id, order__user=request.user)
    detail.delete()
    return Response({
        'status': 'deleted',
        'message': 'محصول از سبد حذف شد.'
    }, status=status.HTTP_200_OK)