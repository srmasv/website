from django.shortcuts import render
from navbar.models import NavItem

def get_all_navitems():
    return NavItem.objects.order_by('position')

def get_breadcrumbs(request):
    if(request.resolver_match.url_name=="homepage"):
        return None
    return request.get_full_path().split("/")[1:]

def navbar(request):
    params = {"navitems": get_all_navitems(), "breadcrumbs": get_breadcrumbs(request)}
    return render(request, 'navbar.html', params)
