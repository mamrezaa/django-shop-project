"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from config import settings

from django.conf.urls.static import static

from contact_us.views import contact_us_page
from products.views import ProductsListView

from .views import home_page,header,footer,login_page,register_page,log_out


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page),
    path('header',header,name='header'),
    path('footer',footer,name='footer'),
    path('login/', login_page, name='login'),
    path('register/',register_page,name='register'),
    path('log_out/',log_out,name='log_out'),
    path('',include('products.urls'),name='products'),
    path('',include('order.urls'),name='order'),
    path('',include('profiles.urls'),name='profile'),


    path('contact-us',contact_us_page,name='contact'),
    path('', include('contact_us.urls')),

    path('', include('products_category.urls')),
    path('', include('shop_settings.urls')),
    path('', include('sliders.urls')),

    path('', include('tags.urls')),
    
    # path('products_categoris_partial',products_categoris_partial,name='products_categoris_partial'),




]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)