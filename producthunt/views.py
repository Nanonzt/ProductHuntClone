from django.shortcuts import render

def home(request):
    return render(request, 'products/templates/products/home.html')
