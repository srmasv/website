from django.shortcuts import render

from .models import HomeText

# Create your views here.
from srmasv.views import get_all_navitems, get_breadcrumbs

def get_hometext():
    return HomeText.objects.first()

def home(request):
    params = {}
    params["navitems"] = get_all_navitems
    params["breadcrumbs"] = get_breadcrumbs(request)
    params["hometext"] = get_hometext()
    return render(request, 'home.html', params)
