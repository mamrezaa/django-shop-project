from django.db import models

# Create your models here.

class Setting(models.Model):
    email = models.EmailField(max_length=100,null=True, blank=True,verbose_name='ایمیل')
    phone = models.CharField(max_length=100,null=True, blank=True, verbose_name='تلفن تماس')
    mobile = models.CharField(max_length=100,null=True, blank=True, verbose_name='تلفن همراه')
    addres = models.CharField(max_length=100,null=True, blank=True, verbose_name='آدرس')
    about = models.CharField(max_length=300,null=True, blank=True, verbose_name='درباره ما')
    instagram = models.CharField(max_length=100,null=True, blank=True, verbose_name='اینستاگرام')

    
    class Meta():
        verbose_name = 'تنظیمات '
        verbose_name_plural = 'تنظیمات'



    def __str__(self):
        return 'تنظیمات سایت'
