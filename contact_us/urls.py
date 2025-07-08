from django.urls import path
from contact_us.api_views import contact_us_api

app_name = 'contact_us'

urlpatterns = [
    path('api/contact-us', contact_us_api, name='contact_us_api'),
]