from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from contact_us.models import ContactUs
from contact_us.serializers import ContactUsSerializer


@api_view(['POST'])
def contact_us_api(request):
    serializer = ContactUsSerializer(data=request.data)
    
    if serializer.is_valid():
        # ذخیره در دیتابیس
        fullName = serializer.validated_data.get('fullName')
        email = serializer.validated_data.get('email')
        message = serializer.validated_data.get('message')

        ContactUs.objects.create(
            fullName=fullName,
            email=email,
            message=message
        )

        return Response({
            'status': 'success',
            'message': 'پیام شما با موفقیت ثبت شد.'
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)