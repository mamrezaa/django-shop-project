from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category
from .serializers import CategorySerializer


# ✅ لیست تمام دسته‌بندی‌ها
@api_view(['GET'])
def category_list_api(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


# ✅ جزئیات یک دسته‌بندی خاص
@api_view(['GET'])
def category_detail_api(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'دسته‌بندی یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category)
    return Response(serializer.data)


# ✅ افزودن دسته‌بندی (اختیاری)
@api_view(['POST'])
def create_category_api(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ ویرایش دسته‌بندی (اختیاری)
@api_view(['PUT'])
def update_category_api(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'دسته‌بندی یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ حذف دسته‌بندی (اختیاری)
@api_view(['DELETE'])
def delete_category_api(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'دسته‌بندی یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

    category.delete()
    return Response({'message': 'دسته‌بندی حذف شد'}, status=status.HTTP_204_NO_CONTENT)