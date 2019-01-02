from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('timeline/', views.timeline, name="timeline"),
]
