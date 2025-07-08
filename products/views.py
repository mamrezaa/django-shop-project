from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from order.forms import UserNewOrderForm
from products.models import ProductGallery, Products
from products_category.models import Category


# Create your views here.
class ProductsListView(ListView):
    template_name = 'products_list.html'  # اسم تمپلت رو مشخص می‌کنیم
    context_object_name = 'products'              # اسم متغیر توی تمپلت
    paginate_by = 2                            # تعداد آیتم در هر صفحه (اختیاری)

    def get_queryset(self):
        # می‌تونی اینجا کوئری رو سفارشی کنی
        return Products.objects.get_active_product()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    

class ProductsListByCategory(ListView):
    template_name = 'products_list.html'  # اسم تمپلت رو مشخص می‌کنیم
    context_object_name = 'products' # نامی که لیست محصولات در تمپلت با آن قابل دسترسی است
    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = Category.objects.filter(name__iexact=category_name)

        if category is None:
            raise Http404('error 404')

        
        return Products.objects.get_product_by_category(category_name)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    
# def products_categoris_partial(request):
#     categories = Products.objects.all()
#     context = {'categories':categories}

#     return render(request,'product_view_partial.html',context)


def product_detail(request,product_id, title):
    

    product = Products.objects.get_product_by_id(product_id)
    categories = Category.objects.all()
    gallery = ProductGallery.objects.filter(product_id=product_id)

    new_order_form = UserNewOrderForm(request.POST or None , initial=({'product_id':product_id}))

    # related_products = Products.objects.get_queryset().filter(categories__product=product)

    related_products = Products.objects.filter(
            category__in=product.category.all()
        ).exclude(id=product.id).distinct()
        


    if product is None :
        raise Http404('محصول یافت نشد ')
    
    product.visits+=1
    product.save()
    

    context = {
        'product': product,
        'categories': categories,
        'gallery':gallery,
        'related_products':related_products,
        'new_order_form':new_order_form
        
    }

    return render(request,'product_detail.html',context)


class SearchProducts(ListView):
    template_name = 'products_list.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
           return Products.objects.search_products(query)
        
        return Products.objects.get_active_product()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context