from django.shortcuts import get_object_or_404
from courses.models import Course


def cart_contents(request):

    cart_items = []
    total = 0
    course_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            course = get_object_or_404(Course, pk=item_id)
            total += item_data * course.price
            course_count += item_data
            cart_items.append({
                'item_id': item_id,
                'course': course,
            })
        else:
            course = get_object_or_404(Course, pk=item_id)
            for size in item_data['items_by_size'].items():
                total += course.price
                cart_items.append({
                    'item_id': item_id,
                    'course': course,
                    'size': size,
                })

    context = {
        'cart_items': cart_items,
        'course_count': course_count,
        'total': total,
    }

    return context
