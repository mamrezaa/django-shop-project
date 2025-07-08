from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Inline برای نمایش UserProfile در UserAdmin
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'پروفایل'

# سفارشی کردن UserAdmin
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    # اضافه کردن فیلد phone_number به لیست نمایش (اختیاری)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_phone_number')
    
    def get_phone_number(self, instance):
        return instance.profile.phone_number if hasattr(instance, 'profile') else '-'
    
    get_phone_number.short_description = 'شماره تلفن'

# حذف User Admin پیش‌فرض و ثبت جدید
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)






