from django.urls import path
from .api_views import setting_api

app_name = 'setting'

urlpatterns = [
    path('api/setting/', setting_api, name='setting_api'),
]