from django.urls import path
from . import views
from .views import your_view
from .views import order_create_view
from .views import client_add_view, client_list_view


urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('client-types/', views.ClientTypes, name='ClientTypes'),
    path('client/', views.Client, name='Client'),
    path('Product/', views.Product, name='Product'),
    path('order/', views.Order, name='Order'),
    path('client/add/', client_add_view, name='client_add'),
    path('client/', client_list_view, name='client_list'),
]


