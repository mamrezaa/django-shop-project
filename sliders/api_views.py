from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Slider
from .serializers import SliderSerializer


# ✅ لیست تمام اسلایدرها
@api_view(['GET'])
def slider_list_api(request):
    sliders = Slider.objects.all()
    serializer = SliderSerializer(sliders, many=True)
    return Response(serializer.data)


# ✅ جزئیات یک اسلایدر خاص
@api_view(['GET'])
def slider_detail_api(request, slider_id):
    try:
        slider = Slider.objects.get(id=slider_id)
    except Slider.DoesNotExist:
        return Response({'error': 'اسلایدر یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

    serializer = SliderSerializer(slider)
    return Response(serializer.data)


# ✅ افزودن اسلایدر (اختیاری)
@api_view(['POST'])
def create_slider_api(request):
    serializer = SliderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ ویرایش اسلایدر (اختیاری)
@api_view(['PUT'])
def update_slider_api(request, slider_id):
    try:
        slider = Slider.objects.get(id=slider_id)
    except Slider.DoesNotExist:
        return Response({'error': 'اسلایدر یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

    serializer = SliderSerializer(slider, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ حذف اسلایدر (اختیاری)
@api_view(['DELETE'])
def delete_slider_api(request, slider_id):
    try:
        slider = Slider.objects.get(id=slider_id)
    except Slider.DoesNotExist:
        return Response({'error': 'اسلایدر یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

    slider.delete()
    return Response({'message': 'اسلایدر حذف شد.'}, status=status.HTTP_204_NO_CONTENT)