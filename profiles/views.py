from django.http import Http404
from django.shortcuts import render

from config.forms import User
from order.models import Order, OrderDetail
from profiles.forms import UserEdiProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def profile_main_page(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    context = {'user':user}
    return render(request,'profile_main_page.html',context)

@login_required(login_url='/login')
def profile_user_order(request):
    user_id = request.user.id
    # orders_user = Order.objects.filter(user_id=user_id)

    all_order_details = OrderDetail.objects.filter(
        order__user_id=user_id
    ).select_related('product', 'order')
    
    # total_price = sum(detail.product_sum_in_cart() for detail in all_order_details)

    order_user = Order.objects.filter(user_id=request.user.id , paid=False).first()
    total_price = 0

    if order_user:
        total_price = order_user.get_total_price()
    

    context = {
        'all_order_details': all_order_details,
        'total_price':total_price
    }
    return render(request, 'profile_user_order.html', context)

@login_required(login_url='/login')
def profile_setting(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404()
    
    edit_form = UserEdiProfileForm(request.POST or None , initial={'first_name':user.first_name,'last_name':user.last_name})
    if edit_form.is_valid():
        first_name = edit_form.cleaned_data.get('first_name')
        last_name = edit_form.cleaned_data.get('last_name')
        user.first_name = first_name
        user.last_name = last_name
        user.save()

    context = {
        'edit_form':edit_form
    }
    return render(request, 'profile_setting.html', context)

@login_required(login_url='/login')
def profile_sidebar(request):
    context = {}
    return render(request, 'profile_sidebar.html', context)
