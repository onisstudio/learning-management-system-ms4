from django.shortcuts import get_object_or_404
from courses.models import Course


def cart_contents(request):

    cart_items = []
    total = 0
    cart_total = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            course = get_object_or_404(Course, pk=item_id)
            total += item_data * course.price
            cart_items.append({
                'item_id': item_id,
                'course': course,
            })
        else:
            course = get_object_or_404(Course, pk=item_id)

    if total > 0:
        cart_total = str(total) + ' £'
    else:
        cart_total = '0.00 £'

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }

    return context
