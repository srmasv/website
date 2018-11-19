from . import views
from django.urls import path

urlpatterns = [
    path('recent/', views.recent, name='recent'),
    path('', views.recent, name='blogs')
]
