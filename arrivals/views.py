from django.shortcuts import render
from .models import Arrivals


def arrivals(request):
    """ A view to return the arrivals page """
    arrivals = Arrivals.objects.all()

    context = {
        'arrivals': arrivals,
    }

    return render(request, 'arrivals/arrivals.html', context)
