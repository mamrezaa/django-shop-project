


from django.urls import path

from products.api_views import product_by_category_api, product_detail_api, product_list_api
from .views import ProductsListByCategory, ProductsListView, SearchProducts, product_detail


app_name = 'products'

urlpatterns = [
      path('productss', ProductsListView.as_view(),name='product_list'),
      path('products/<product_id>/<title>',product_detail,name='product_detail'),
      path('products/search/', SearchProducts.as_view(), name='product_search'),
      path('productss/<category_name>', ProductsListByCategory.as_view(),name='product_list_category'),

    # API URLs
    path('api/products', product_list_api, name='product_list_api'),
    path('api/products/<int:product_id>/', product_detail_api, name='product_detail_api'),
    path('api/products/category/<str:category_name>/', product_by_category_api, name='product_by_category_api'),
    



 ]

    #   path('', ProductListView.as_view(), name='product_list'),

