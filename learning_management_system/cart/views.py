from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages

from courses.models import Course

# Create your views here.


def view_cart(request):
    """ A view to show all courses in the cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add item to cart """

    course = get_object_or_404(Course, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[item_id] = 1

    messages.success(request, f'{course.title} added to the cart')
    request.session['cart'] = cart

    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from cart"""

    try:
        course = get_object_or_404(Course, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        messages.success(request, f'{course.title} removed from the cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing course: {e}')
        return HttpResponse(status=500)