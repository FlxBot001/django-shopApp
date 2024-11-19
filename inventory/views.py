from django.shortcuts import render

# Create your views here.

def home(request):
   return render(request, 'index.html')

def inventoryapp(request):
   return render(request, 'base.html')