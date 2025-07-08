from django.urls import path
from .api_views import (
    category_list_api,
    category_detail_api,
    create_category_api,
    update_category_api,
    delete_category_api
)

app_name = 'category'

urlpatterns = [
    # GET - لیست تمام دسته‌بندی‌ها
    path('api/categories/', category_list_api, name='category_list_api'),
    
    # GET - جزئیات یک دسته‌بندی
    path('api/categories/<int:category_id>/', category_detail_api, name='category_detail_api'),
    
    # POST - افزودن دسته‌بندی
    path('api/categories/create/', create_category_api, name='create_category_api'),
    
    # PUT - ویرایش دسته‌بندی
    path('api/categories/<int:category_id>/update/', update_category_api, name='update_category_api'),
    
    # DELETE - حذف دسته‌بندی
    path('api/categories/<int:category_id>/delete/', delete_category_api, name='delete_category_api'),
]