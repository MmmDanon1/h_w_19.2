from django.urls import path

from catalog.views import contract, home

urlpatterns = [
    path('', contract),
    path('', home),
]