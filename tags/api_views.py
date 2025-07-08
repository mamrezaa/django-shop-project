from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tags
from .serializers import TagSerializer
from products.models import Products


# ✅ لیست تمام تگ‌ها
@api_view(['GET'])
def tag_list_api(request):
    tags = Tags.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)


# ✅ جزئیات یک تگ خاص
@api_view(['GET'])
def tag_detail_api(request, tag_id):
    try:
        tag = Tags.objects.get(id=tag_id)
    except Tags.DoesNotExist:
        return Response({'error': 'تگ یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TagSerializer(tag)
    return Response(serializer.data)


# ✅ افزودن یک تگ جدید
@api_view(['POST'])
def create_tag_api(request):
    title = request.data.get('title')
    description = request.data.get('description')
    active = request.data.get('active', True)

    if not title:
        return Response({'title': 'عنوان الزامی است.'}, status=status.HTTP_400_BAD_REQUEST)

    # ساختن تگ
    tag = Tags.objects.create(
        title=title,
        description=description,
        active=active
    )

    # اگر محصولاتی داده شده باشه، بهش اضافه کن
    product_ids = request.data.get('products', [])
    if product_ids:
        products = Products.objects.filter(id__in=product_ids)
        tag.products.add(*products)

    serializer = TagSerializer(tag)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# ✅ ویرایش یک تگ
@api_view(['PUT'])
def update_tag_api(request, tag_id):
    try:
        tag = Tags.objects.get(id=tag_id)
    except Tags.DoesNotExist:
        return Response({'error': 'تگ یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

    title = request.data.get('title')
    description = request.data.get('description')
    active = request.data.get('active')

    if title:
        tag.title = title
    if description:
        tag.description = description
    if active is not None:
        tag.active = active

    tag.save()

    # ویرایش محصولات (اختیاری)
    product_ids = request.data.get('products', [])
    if product_ids:
        tag.products.set(product_ids)

    serializer = TagSerializer(tag)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ حذف یک تگ
@api_view(['DELETE'])
def delete_tag_api(request, tag_id):
    try:
        tag = Tags.objects.get(id=tag_id)
    except Tags.DoesNotExist:
        return Response({'error': 'تگ یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

    tag.delete()
    return Response({'message': 'تگ با موفقیت حذف شد.'}, status=status.HTTP_204_NO_CONTENT)