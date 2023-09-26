from django.urls import path, include

from catalog.views import contract, home

urlpatterns = [
    path('', contract),
    path('', home),
]