from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('courses'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Gs3LhDbadlz58bbs1rIPY0UF66UXs8Yvn69y3M1DXia8mzFb4RizeMudeCNluHeDLys3ta3Aw5J19BgWLwowO3A004bw43WyT'  # noqa
    }

    return render(request, template, context)
