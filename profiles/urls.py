


from django.urls import path

from profiles.api_views import profile_api
from profiles.views import profile_main_page, profile_setting, profile_user_order



app_name = 'profile'

urlpatterns = [
      path('profile',profile_main_page,name='profile_main'),
      path('profile/orders',profile_user_order,name='orders'),
      path('profile/setting',profile_setting,name='setting'),

      path('api/profile/', profile_api, name='profile_api'),

]



