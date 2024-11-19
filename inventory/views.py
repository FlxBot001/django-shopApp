from django.shortcuts import render

# Create your views here.

def home(request):
   return render(request, 'home.html')

def base(request):
   return render(request, 'base.html')

def add_product(request):
   return render(request, 'add_product.html')