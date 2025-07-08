

from django.shortcuts import redirect, render

from config.forms import Login_form, Register_form
from django.contrib.auth import authenticate,login as auth_login , get_user_model,logout

from products.models import Products
from products_category.models import Category
from profiles.models import UserProfile
from shop_settings.models import Setting
from sliders.models import Slider
from django.contrib.auth import login






def header(request):
    setting = Setting.objects.first()
    context = {'setting':setting}
    return render(request,'base/header.html',context)

def footer(request):
    setting = Setting.objects.first()
    context = {'setting':setting}
    return render(request,'base/footer.html',context)


def home_page(request):
    categories = Category.objects.all()
    sliders = Slider.objects.all()
    featured_product = Products.objects.filter(featured=True)
    most_visits_products = Products.objects.order_by('-visits').all()[:4]
    latest_products = Products.objects.order_by('-id').all()[:4]


    
    context = {
        'categories': categories,
        'sliders':sliders,
        'featured_product':featured_product,
        'most_visits_products':most_visits_products,
        'latest_products':latest_products
        }
    return render(request,'home_page.html',context)



def login_page(request):
    print(request.user.is_authenticated)

    login_form = Login_form(request.POST or None)
    
    if login_form.is_valid():
        username = login_form.cleaned_data.get('userName')
        password = login_form.cleaned_data.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/profile')
        else:
            print('error')


    context = {
        'login_form':login_form
    }
    return render(request, 'login.html', context)


User = get_user_model()

def register_page(request):
    register_form = Register_form(request.POST or None)

    if register_form.is_valid():
        firstName = register_form.cleaned_data.get('firstName')
        lastName = register_form.cleaned_data.get('lastName')
        username = register_form.cleaned_data.get('userName')
        email    = register_form.cleaned_data.get('email')
        phone_number = register_form.cleaned_data.get('phone_number')
        password = register_form.cleaned_data.get('password')
        user =  User.objects.create_user(first_name=firstName,last_name=lastName,username=username,email=email,password=password)
       
        UserProfile.objects.create(
            user=user,
            phone_number=phone_number  # می‌تونه None باشه چون null=True
        )

        login(request, user)


        return redirect('profile:profile_main')

    context = {
        'register_form':register_form
    }
    return render(request,'register.html',context)


def log_out(request):
    logout(request)
    return redirect('/login')
