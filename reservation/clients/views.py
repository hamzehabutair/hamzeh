from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import ClientTypes
from .forms import Client
from .forms import Product
from .forms import Order
from .models import Client
from .forms import ClientForm

def index(request):
    return HttpResponse("Clients home page")

def info(request):
	return render(request, "info.html", {})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('clients/dashboard')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

def your_view(request):
    if request.method == 'POST':
        form = ClientTypes(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = ClientTypes()
    return render(request, 'your_template.html', {'form': form})


def your_view(request):
    if request.method == 'POST':
        form = Client(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = Client()
    return render(request, 'your_template.html', {'form': form})


def your_view(request):
    if request.method == 'POST':
        form = Product(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = Product()
    return render(request, 'your_template.html', {'form': form})

def order_create_view(request):
    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = Order()
    return render(request, 'order_form.html', {'form': form})


def client_add_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Redirect to client list page after adding
    else:
        form = ClientForm()
    return render(request, 'client_add.html', {'form': form})

def client_list_view(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})