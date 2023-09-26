from django.shortcuts import render

# Create your views here.
def contract(request):
    return render(request, 'catalog/contract.html')

def home(request):
    return render(request, 'catalog/home.html')