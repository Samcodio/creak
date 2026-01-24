from django.shortcuts import render, get_object_or_404
from .cart import Cart
from django.views.decorators.csrf import csrf_exempt
from product.models import Product
from django.template.loader import render_to_string
from django.http import JsonResponse
import json


# listing items in the cart page
def cart_summary(request):
    cart = Cart(request)
    cart_products, total_sum = cart.get_prods()

    context = {
        'cart_products': cart_products,
        'total_sum': total_sum,
               }
    return render(request, 'Cart/cart_summary.html', context)


# adding items to the cart
def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        print(f"Received POST data: product_id={product_id}, quantity={quantity}")


        # look for product in DB
        product = get_object_or_404(Product, id=product_id)
        # save to session
        cart.add(product=product, quantity=quantity)

        print(f"Cart data after adding: {cart.cart.get(product_id)}")

        cart_quantity = cart.total_quantities()
        product_cart_data = cart.cart.get(product_id, {})
        # size_in_cart = product_cart_data.get('quantity', {}).get('size', '')

        response = JsonResponse({
            'qty': cart_quantity,
            'cart_data': {
                'product_id': product_id,
                'quantity': quantity,
                'full_cart_data': product_cart_data
            }
        })
        return response  # Ensure you return the response


# deleting shit from the cart
@csrf_exempt
def cart_delete(request):
    if request.POST.get('action') == 'post':
        try:
            cart = Cart(request)
            product_id = request.POST.get('product_id')

            if product_id:
                removed = cart.remove(product_id)
                if removed:
                    cart_products, total_sum = cart.get_prods()
                    total_quantity = cart.total_quantities()

                    return JsonResponse({
                        'success': True,
                        'total_quantity': total_quantity,
                        'message': 'Item removed from cart'
                    })

            return JsonResponse({
                'success': False,
                'message': 'Item not found in cart'
            }, status=400)

        except Exception as e:
            # For debugging
            import traceback
            print(traceback.format_exc())
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)

