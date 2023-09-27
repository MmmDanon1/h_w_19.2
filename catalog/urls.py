from django.urls import path

from catalog.views import contact, home

urlpatterns = [
    path('/contact/', contact),
    path('', home),
]