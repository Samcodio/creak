from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from cart.cart import Cart

# Create your views here.

def base(request):
    context = {}
    return render(request, 'base.html', context)


def home(request):
    cart = Cart(request)
    category = Category.objects.all()
    products = Product.objects.all()[:12]
    context = {
        'category': category,
        'products': products,
        'cart': cart
    }
    return render(request, 'index.html', context)

# navbar pages
def contact(request):
    context = {}
    return render(request, 'navbar/contact.html', context)

def about(request):
    context = {}
    return render(request, 'navbar/about.html', context)

def news(request):
    context = {}
    return render(request, 'navbar/news.html', context)

def products(request):
    category = Category.objects.all()
    items = Product.objects.all().order_by('-id')  # or any ordering

    paginator = Paginator(items, 9)  # 9 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "products": page_obj,
        "category": category
    }
    return render(request, 'navbar/products.html', context)

def capability(request):
    context = {}
    return render(request, 'navbar/capability.html', context)

# end of navbar pages

# footer pages
def company(request):
    context = {}
    return render(request, 'footer/company.html', context)

def quality(request):
    context = {}
    return render(request, 'footer/quality.html', context)

def privacy(request):
    context = {}
    return render(request, 'footer/privacy.html', context)

def website(request):
    context = {}
    return render(request, 'footer/website.html', context)

def terms_sales(request):
    context = {}
    return render(request, 'footer/terms_sales.html', context)

def purchase_terms(request):
    context = {}
    return render(request, 'footer/purchase_terms.html', context)

def anti_bribery(request):
    context = {}
    return render(request, 'footer/anti_bribery.html', context)

def environmental(request):
    context = {}
    return render(request, 'footer/environmental.html', context)

def equal_opportunities(request):
    context = {}
    return render(request, 'footer/equal_opportunities.html', context)

def health(request):
    context = {}
    return render(request, 'footer/health.html', context)

def obsolescence(request):
    context = {}
    return render(request, 'footer/obsolescence.html', context)

def risk_management(request):
    context = {}
    return render(request, 'footer/risk_management.html', context)

# end of footer pages

def category(request, id):
    cat = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category_id=id).order_by('-id')

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "category": cat,
        "products": page_obj
    }
    return render(request, "Category/category.html", context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, 'Product/product_detail.html', context)



