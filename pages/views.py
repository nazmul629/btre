from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import bedroom_choices, price_choices, state_choice

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_publish  = True)[:3]

    context = {
        'listings':listings,
        'bedroom_choices': bedroom_choices,
        'price_choices':price_choices,
        'state_choice':state_choice


    }
    return render(request, 'pages/index.html',context)

def about(request):


    realtor = Realtor.objects.order_by('-hire_date')
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        "realtors" : realtor,
        "mvp_realtor" : mvp_realtor
    }
    return render(request, 'pages/about.html',context)