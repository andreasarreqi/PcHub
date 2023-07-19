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
    """
    Adds product to bag,
    Updates bag with product and product quantity.
    """
    computer = get_object_or_404(Computers, id=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    try:
        if item_id in list(bag.keys()):
            if computer.quantity >= bag[item_id] + quantity:
                bag[item_id] += quantity
                messages.success(
                    request, f'{computer.name} succesfully added to bag!')
            else:
                messages.error(
                    request,
                    f'Sorry, only {computer.quantity}\
                        of these are curently available.\
                        You have {bag[item_id]} in your cart already.')
        else:
            bag[item_id] = quantity
            messages.success(
                    request, f'{computer.name} succesfully added to bag!')
    except RuntimeError:
        messages.error(
            request,
            "Whoops, We've encountered a problem, we'll get straight onto it,\
                in the meantime you could always try again??")

    request.session['bag'] = bag
    return redirect(redirect_url)
