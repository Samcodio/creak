from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.messages import constants as messages
from django.contrib import messages
from .forms import *
# from ecommerce.views import BaseView
import json
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
# import resend
# from cart.cart import Cart
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from product.models import User, UserProfile
from django.contrib import messages
# from django.conf import settings

# Create your views here.


# logging in and re-adding products to cart and wishlist after logging in
def login_page(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.GET.get('next')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            UserProfile.objects.get_or_create(user=user)
            #  shopping cart stuff
            # current_user = UserProfile.objects.get(user__id=request.user.id)
            # saved_cart = current_user.old_cart
            # saved_wishlist = current_user.old_wishlist
            # if saved_cart:
            #     cart_string = saved_cart
            #     cart_dict = json.loads(cart_string)  # Convert JSON string back to dictionary
            #     cart = Cart(request)
            #     cart.remove_non_existent_products()
            #     for product_id, item in cart_dict.items():
            #         try:
            #             product = Product.objects.get(id=int(product_id))
            #             quantity = item['quantity']['quantity']
            #             cart.db_add(product, quantity)
            #         except Product.DoesNotExist:
            #             pass

            if next_url:
                messages.success(request, 'Login Successful')
                return redirect(next_url)

            return redirect('product:home')
        else:
            messages.warning(request, 'Invalid details')
    context = {}
    return render(request, 'Authentication/login.html', context)


def logout_button(request):
    logout(request)
    return redirect('accounts:login')

def signUp(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created')
            return redirect('accounts:login')
        else:
            # Loop through errors and push them into messages
            for field, errors in form.errors.items():
                for error in errors:
                    if field == '__all__':
                        # Non-field error
                        messages.error(request, error)
                    else:
                        messages.add_message(
                            request,
                            messages.ERROR,
                            f"{field.capitalize()}: {error}",
                            extra_tags="field-error"
                        )

    context = {
        'form': form,
    }
    return render(request, 'Authentication/register.html', context)

