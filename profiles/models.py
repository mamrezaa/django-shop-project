from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# در فایل models.py اپلیکیشن مربوطه (مثلا profiles/models.py)

from django.db import models
from django.conf import settings # برای ارجاع به مدل User فعال در پروژه

class UserProfile(models.Model):
    # این فیلد UserProfile را به یک کاربر خاص متصل می کند
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    # از روش جایگزین برای جلوگیری از واردات چرخشی احتمالی استفاده می کنیم:
    user = models.OneToOneField(
        'auth.User', # یا نام مدل کاربری سفارشی شما (مثلا settings.AUTH_USER_MODEL اگر از آن استفاده می کنید)
        on_delete=models.CASCADE,
        related_name='profile'
    )


    # فیلد شماره تلفن
    phone_number = models.CharField(
        max_length=11, # یا طول مناسب برای شماره تلفن های شما
        blank=True, # اجازه می دهد در فرم ها خالی باشد
        null=True # اجازه می دهد در پایگاه داده NULL باشد
        # اگر می خواهید الزامی باشد، blank=False, null=False و در فرم required=True بگذارید
    )

    # شما می توانید فیلدهای اضافی دیگری مانند آدرس، تاریخ تولد و ... را نیز در اینجا اضافه کنید.
    # مثال:
    # address = models.CharField(max_length=255, blank=True, null=True)
    # birth_date = models.DateField(blank=True, null=True)
    
    class Meta():
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل'

    def __str__(self):
        # نمایش نام کاربری کاربر مرتبط به عنوان نمایش متنی شیء پروفایل
        return f"پروفایل کاربری {self.user.username}"