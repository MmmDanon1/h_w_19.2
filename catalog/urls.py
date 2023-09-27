from django.urls import path

from catalog.views import contact, home

urlpatterns = [
    path('/templates/contact/', contact),
    path('', home),
]