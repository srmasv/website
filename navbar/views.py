from django.shortcuts import render

from .models import *

# Create your views here.
from srmasv.views import get_all_navitems, get_breadcrumbs

def get_hometext():
    return HomeText.objects.first()

def get_journeytext():
    return JourneyText.objects.first()

def get_domains():
    return DomainText.objects.order_by("position")

def get_carouselitems():
    return CarouselItem.objects.all().reverse()

def get_recenttext():
    return Recent.objects.first()

def get_objectivetext():
    return ObjectiveText.objects.first()

def get_objectives():
    return Objective.objects.all()

def get_logo():
    return Logo.objects.first()

def home(request):
    params = {}
    params["navitems"] = get_all_navitems
    params["breadcrumbs"] = get_breadcrumbs(request)
    params["hometext"] = get_hometext()
    params["carouselitems"] = get_carouselitems()
    params["journeytext"] = get_journeytext()
    params["domains"] = get_domains()
    params["recenttext"] = get_recenttext()
    params["objectivetext"] = get_objectivetext()
    params["objectives"] = get_objectives()
    params["logo"] = get_logo()
    return render(request, 'home.html', params)
