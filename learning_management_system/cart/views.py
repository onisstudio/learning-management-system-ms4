from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view to show all courses in the cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add item to cart """

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[item_id] = 1

    request.session['cart'] = cart

    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from cart"""

    print('test')
    cart = request.session.get('cart', {})
    cart.pop(item_id)

    request.session['cart'] = cart
    return render(request, 'cart/cart.html')
