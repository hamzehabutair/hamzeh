from django import forms
from .models import ClientTypes
from .models import Client
from .models import Product
from .models import Order
from .models import Client

class ClientTypes(forms.ModelForm):
    class Meta:
        model = ClientTypes
        fields = ['type', 'name', 'description']

class Client(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['gender_choices', 'cid', 'name', 'email', 'birthday']



class Product(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['pid', 'name', 'description']

class Order(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['oid', 'cid', 'pid', 'orderdate', 'shippingdate']



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email']