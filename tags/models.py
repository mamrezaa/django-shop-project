from django.db import models
from products.models import Products
from django.db.models.signals import pre_save

from tags.utils import unique_slug_generator



# Create your models here.

class Tags(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Products,blank=True)

    class Meta():
        verbose_name = 'برچسب/تگ'
        verbose_name_plural = 'برچسب ها / تگ ها'

    def __str__(self):
        return self.title
    

def tags_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)