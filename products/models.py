import os
import random
from django.db import models
from django.db.models import Q

from products_category.models import Category

# Create your models here.

def get_file_extention(file):
    base_name = os.path.basename(file)
    name,ext = os.path.splitext(base_name)
    return name,ext


def upload_image(instance,filename):
    rand_name = random.randint(1,999999999)
    name , ext = get_file_extention(filename)
    final_name = f'{instance.id}-{rand_name}-{ext}'
    return f'products/{final_name}'


def upload_image_gallery(instance,filename):
    rand_name = random.randint(1,999999999)
    name , ext = get_file_extention(filename)
    final_name = f'{instance.id}-{rand_name}-{ext}'
    return f'gallery/{final_name}'



class ActiveProductManager(models.Manager):
    def get_active_product(self):
        return self.get_queryset().filter(active=True)
    
    def get_product_by_id(self,product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1: 
            return qs.first()
        else:
            return None
        
    def search_products(self,query):
        Lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(tags__title__icontains=query)
        return self.get_queryset().filter( Lookup, active = True)


    def get_product_by_category(self,category_name):
        return self.get_queryset().filter(category__name__iexact=category_name)


class Products(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    image = models.ImageField(upload_to=upload_image ,null=True,blank=True)
    active = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category,blank=True)
    featured = models.BooleanField(default=False,verbose_name='محصول ویژه')
    visits = models.IntegerField(default=0,verbose_name='تعداد مشاهده')

    objects = ActiveProductManager()

    class Meta():
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def __str__(self):
        return self.title
    

class ProductGallery(models.Model):
        title = models.CharField(max_length=100,null=True, blank=True)
        image = models.ImageField(upload_to=upload_image_gallery ,null=True,blank=True)
        product = models.ForeignKey(Products,on_delete=models.CASCADE)

        class Meta():
           verbose_name = 'گالری تصاویر'
           verbose_name_plural = 'گالری تصاویر'

        def __str__(self):
            return self.title


