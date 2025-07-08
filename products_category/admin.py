from django.contrib import admin
from .models import Category

# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__','title']

admin.site.register(Category,ProductCategoryAdmin)