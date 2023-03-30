from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InputForm, Booking
from .models import Cuisine, Menu

# Create your views here.

def form_view(request):
    form = InputForm()
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("Reservation Success!")

    else :    
        context = {"form": form}
        return render(request, "booking.html", context)

def reservation(request):
    form = Booking()
    if request.method == "POST":
        form = Booking(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"sucessbook.html",{"form": form, 'successful_submit': False} )
        
    context = {"form": form, 'successful_submit': False}
    return render(request, "booking.html", context)


def home(request):
    return render(request,'home.html')


def about(request):
    #about_content = {'about' : "Order food online and get it delivered to you Hot and fresh at your doorstep!"}
    return render(request,"about.html")

def menu(request):
    cuisines = Cuisine.objects.all()
    menus = Menu.objects.all()
    context = {'cuisines': cuisines, 'menus': menus}
    return render(request, 'menu.html', context)