from django.shortcuts import render

from contact_us.forms import ContactUsForm
from contact_us.models import ContactUs

# Create your views here.


def contact_us_page(request):


        contact_form = ContactUsForm(request.POST or None)

        if contact_form.is_valid():
            # ذخیره در دیتابیس
            fullName=contact_form.cleaned_data.get('fullName')
            email=contact_form.cleaned_data.get('email')
            message=contact_form.cleaned_data.get('message')
            ContactUs.objects.create(fullName=fullName,email=email,message=message )


        context = {
           'contact_form': contact_form,
       }

        return render(request, 'contact_us.html', context)