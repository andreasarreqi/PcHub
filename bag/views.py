from django.shortcuts import (
    render, redirect, reverse,
    HttpResponse, get_object_or_404
    )

from django.contrib import messages
from products.models import Computers


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a product to the shopping bag """

    computer = get_object_or_404(Computers, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added {computer.name} to your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {computer.name} to your bag')

    request.session['bag'] = bag

    return redirect(redirect_url)
