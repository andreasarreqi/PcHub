from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Computers, Monitors
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ComputerForm


def computers(request):
    """ A view to return the computers page """
    computers = Computers.objects.all()

    context = {
        'computers': computers,
    }
    return render(request, 'products/computers.html', context)


def computer_detail(request, computer_id):
    """ A view to show individual product details """

    computer = get_object_or_404(Computers, pk=computer_id)

    context = {
        'computer': computer,
    }

    return render(request, 'products/computer_detail.html', context)


def monitors(request):
    """ A view to return the computers page """
    monitors = Monitors.objects.all()

    context = {
        'monitors': monitors,
    }
    return render(request, 'products/monitors.html', context)


def monitor_detail(request, monitor_id):
    """ A view to show individual monitors """

    monitors = get_object_or_404(Monitors, pk=monitor_id)

    context = {
        'monitors': monitors,
    }

    return render(request, 'products/monitors_detail.html', context)


@login_required
def add_computer(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ComputerForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('computer_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
                )
    else:
        form = ComputerForm()

    template = 'products/add_computer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_computer(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Computers, pk=product_id)
    if request.method == 'POST':
        form = ComputerForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated computer!')
            return redirect(reverse('computer_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update computer'
                           'Please ensure the form is valid.'
                           )
    else:
        form = ComputerForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_computer.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_computer(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Computers, pk=product_id)
    product.delete()
    messages.success(request,
                     f'{ product.name } was deleted! from the store')
    return redirect(reverse('computers'))
