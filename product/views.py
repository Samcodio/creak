from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from cart.cart import Cart
from .forms import *
from django.db import transaction
from cloudinary.uploader import upload as cloudinary_upload
from cloudinary.exceptions import Error as CloudinaryError
from django.contrib import messages
from django.db.models import Count

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





def admin_panel(request):
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect('product:home')
    catform = CategoryForm()
    prodform = ProductForm()
    products = Product.objects.all()
    categories = Category.objects.annotate(
        catCount=Count('categorize')
    )
    cat_count = Category.objects.all().count()
    prod_count = Product.objects.all().count()

    if request.method == 'POST' and 'category' in request.POST:
        catform = CategoryForm(request.POST, request.FILES)

        if catform.is_valid():
            try:
                with transaction.atomic():
                    category = catform.save(commit=False)
                    category_logo = request.FILES.get('category_logo')
                    if category_logo:
                        if category_logo.size > 5 * 1024 * 1024:  # 5MB limit
                            messages.warning(request, 'category logo is too large (max 5MB)')
                            return redirect('product:admin_panel')

                        try:
                            result = cloudinary_upload(
                                category_logo,
                                width=500,
                                height=500,
                                crop='fill',
                                format='jpg'
                            )
                            category.category_logo = result['secure_url']
                        except CloudinaryError:
                            messages.warning(request, 'Error uploading category logo')
                            return redirect('product:admin_panel')

                    category.save()
                    messages.success(request, 'category created successfully.')
                    return redirect('product:admin_panel')  # or any success page

            except Exception as e:
                messages.error(request, 'An error occurred while saving category.')

        else:
            for field, errors in catform.errors.items():
                for error in errors:
                    if field == '__all__':
                        # Non-field error
                        messages.error(request, error)
                    else:
                        messages.add_message(request, messages.ERROR,f"{field.capitalize()}: {error}",
                        extra_tags="field-error"
                        )


    if request.method == 'POST'  and 'product' in request.POST:
        prodform = ProductForm(request.POST, request.FILES)
        if prodform.is_valid():
            try:
                with transaction.atomic():
                    product = prodform.save(commit=False)
                    product_img = request.FILES.get('product_img')
                    if product_img:
                        if product_img.size > 5 * 1024 * 1024:  # 5MB limit
                            messages.warning(request, 'Item picture is too large (max 5MB)')
                            return redirect('product:admin_panel')
                        try:
                            result = cloudinary_upload(
                                product_img,
                                width=500,
                                height=500,
                                crop='fill',
                                format='jpg'
                            )
                            product.product_img = result['secure_url']
                        except CloudinaryError:
                            messages.warning(request, 'Error uploading category logo')
                            return redirect('product:admin_panel')

                    product.save()
                    messages.success(request, 'Product created successfully.')
                    return redirect('product:admin_panel')  # or any success page

            except Exception as e:
                messages.error(request, 'An error occurred while saving product.')

        else:
            for field, errors in prodform.errors.items():
                for error in errors:
                    if field == '__all__':
                        # Non-field error
                        messages.error(request, error)
                    else:
                        messages.add_message(
                            request,
                            messages.ERROR,
                            f"{field.capitalize()}: {error}", extra_tags="field-error")
    context = {
        'prodform': prodform,
        'catform': catform,
        'categories': categories,
        'products': products,
        'prod_count': prod_count,
        'cat_count': cat_count
    }
    return render(request, 'Admin/admin.html', context)


def del_category(request, id):
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect('product:home')
    item = get_object_or_404(Category, id=id)
    item.delete()
    messages.success(request, 'Category deleted')
    return redirect('product:admin_panel')

def del_product(request, id):
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect('product:home')
    item = get_object_or_404(Product, id=id)
    item.delete()
    messages.success(request, 'Product deleted')
    return redirect('product:admin_panel')



