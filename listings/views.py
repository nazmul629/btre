from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import bedroom_choices, price_choices, state_choice


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_publish=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    context = {
        'listings': paged_listing
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queyset_list = Listing.objects.order_by('-list_date')

    # Keyword
    if "keywords" in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queyset_list = queyset_list.filter(description__icontains=keywords)

     # citys
    if "city" in request.GET:
        city = request.GET['city']
        if city:
            queyset_list = queyset_list.filter(city__iexact=city)

     # state
    if "state" in request.GET:
        state = request.GET['state']
        if state:
            queyset_list = queyset_list.filter(state__iexact=state)

     # bathrooms
    if "bedrooms" in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queyset_list = queyset_list.filter(bathrooms__lte=bedrooms)

     # price
    if "price" in request.GET:
        price = request.GET['price']
        if price:
            queyset_list = queyset_list.filter(price__lte=price)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choice': state_choice,
        'listings': queyset_list,
        'values': request.GET,

    }
    return render(request, 'listings/search.html', context)
