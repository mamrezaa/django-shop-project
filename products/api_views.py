from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from .models import Products
from .serializers import ProductSerializer
from django.db.models import Q


@api_view(['GET'])
def product_list_api(request):
    query = request.GET.get('q')
    if query:
        products = Products.objects.search_products(query)
    else:
        products = Products.objects.get_active_product()

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail_api(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist:
        return Response({'error': 'محصول یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def product_by_category_api(request, category_name):
    products = Products.objects.get_product_by_category(category_name)
    if not products.exists():
        return Response({'message': 'محصولی یافت نشد'}, status=404)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)