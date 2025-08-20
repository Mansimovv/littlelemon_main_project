from django.shortcuts import render
from .models import Menu
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'index.html')

def menu(request):
    # FIX 1: Corrected 'oreder_by' to 'order_by'
    menu_data = Menu.objects.all().order_by('name') 
    context = {'menu_data': menu_data}
    # FIX 2: Corrected 'menu_html' to 'menu.html'
    return render(request, 'menu.html', context)

def menu_item(request,pk):
    item = Menu.objects.get(pk=pk)
    context = {'item': item}
    return render(request, 'menu_item.html', context)

def book(request):
    return render(request,'book.html')