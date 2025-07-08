from django.http import Http404
from django.shortcuts import redirect, render

from order.forms import UserNewOrderForm
from order.models import Order, OrderDetail
from products.models import Products
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def add_new_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        order = Order.objects.filter(user_id=request.user.id , paid=False).first()
        if order is None:
            order = Order.objects.create(user_id=request.user.id , paid=False)

        product_id = new_order_form.cleaned_data.get('product_id')
        product = Products.objects.get_product_by_id(product_id)
        count = new_order_form.cleaned_data.get('count')

        
        
        if count < 0 :
            count=1

        order.orderdetail_set.create(product_id=product.id , count=count , price=product.price)
        # OrderDetail.objects.create(order=order, product=..., count=..., price=...)
        return redirect(f'/products/{product.id}/{product.title}')
    

@login_required(login_url='/login')
def cart(request):
    context = {
        'order':None,
        'details':None,
        'total_price':0
    }

    open_order = Order.objects.filter(user_id=request.user.id , paid=False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
        context['total_price'] = open_order.get_total_price()

    return render(request,'cart_page.html',context)


@login_required(login_url='/login')
def remove_cart_item(request,detail_id):
    order_detail = OrderDetail.objects.get_queryset().get(id=detail_id,order__user=request.user)
    if order_detail is not None:
        order_detail.delete()
        return redirect('/cart')
    
    raise Http404()
    