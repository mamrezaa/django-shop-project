import os
import random
from django.db import models

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


class Slider(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    url = models.URLField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_image ,null=True,blank=True)

    
    class Meta():
        verbose_name = 'اسلایدها'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title
    