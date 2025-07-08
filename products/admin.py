from django.contrib import admin

from products.models import Products,ProductGallery

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','title','price','active']

admin.site.register(Products,ProductAdmin)
admin.site.register(ProductGallery)