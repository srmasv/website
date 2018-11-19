from django.shortcuts import render

from .models import Blog

# Create your views here.
def recent(request):
    params = {}
    params["blogs"] = Blog.objects.order_by('-pub_date')[:5]
    return render(request, 'blogs/recent.html', params)
