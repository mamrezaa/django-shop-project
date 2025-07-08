


from django.urls import path
from order.views import add_new_order, cart, remove_cart_item
from .api_views import user_cart_api, add_to_cart_api, remove_from_cart_api


app_name = 'order'


urlpatterns = [
      path('add-new-order',add_new_order),
      path('cart',cart),
      path('remove-cart-item/<detail_id>',remove_cart_item),

      # API URLs
      path('api/order/cart/', user_cart_api, name='user_cart_api'),
      path('api/order/add-to-cart/', add_to_cart_api, name='add_to_cart_api'),
      path('api/order/remove/<int:detail_id>/', remove_from_cart_api, name='remove_from_cart_api'),


 ]


