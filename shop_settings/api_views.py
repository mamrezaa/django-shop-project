from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Setting
from .serializers import SettingSerializer


@api_view(['GET', 'PUT'])
def setting_api(request):
    # فقط یک رکورد وجود داره
    try:
        site_setting = Setting.objects.get(id=1)  # فرض: تنظیمات سایت فقط یک ردیف داره
    except Setting.DoesNotExist:
        return Response({'error': 'تنظیمات وجود ندارد'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SettingSerializer(site_setting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SettingSerializer(site_setting, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)