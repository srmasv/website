from django.shortcuts import render

from .models import HomeText, JourneyText, DomainText, CarouselItem

# Create your views here.
from srmasv.views import get_all_navitems, get_breadcrumbs

def get_hometext():
    return HomeText.objects.first()

def get_journeytext():
    return JourneyText.objects.first()

def get_domains():
    return DomainText.objects.order_by("position")

def get_carouselitems():
    return CarouselItem.objects.order_by("-id")

def home(request):
    params = {}
    params["navitems"] = get_all_navitems
    params["breadcrumbs"] = get_breadcrumbs(request)
    params["hometext"] = get_hometext()
    params["carouselitems"] = get_carouselitems()
    params["journeytext"] = get_journeytext()
    params["domains"] = get_domains()
    return render(request, 'home.html', params)
