from django.urls import path
from .api_views import (
    slider_list_api,
    slider_detail_api,
    create_slider_api,
    update_slider_api,
    delete_slider_api
)

app_name = 'slider'

urlpatterns = [
    # GET - لیست تمام اسلایدرها
    path('api/sliders/', slider_list_api, name='slider_list_api'),
    
    # GET - جزئیات یک اسلایدر
    path('api/sliders/<int:slider_id>/', slider_detail_api, name='slider_detail_api'),
    
    # POST - افزودن اسلایدر جدید
    path('api/sliders/create/', create_slider_api, name='create_slider_api'),
    
    # PUT - ویرایش اسلایدر
    path('api/sliders/<int:slider_id>/update/', update_slider_api, name='update_slider_api'),
    
    # DELETE - حذف اسلایدر
    path('api/sliders/<int:slider_id>/delete/', delete_slider_api, name='delete_slider_api'),
]