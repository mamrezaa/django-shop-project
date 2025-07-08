from django.contrib import admin

from contact_us.models import ContactUs

# Register your models here.



# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['__str__','fullName','email','message','time','read']

admin.site.register(ContactUs,ContactUsAdmin)
