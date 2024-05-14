from django.db import models
class ClientTypes(models.Model):
    type = models.IntegerField(primary_key=True, max_length=5,default=0)
    name = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=500)
def __str__(self):
    return self.name
class Client(models.Model):
    gender_choices = [(1, "Male"), (2, "Female")]
    cid = models.IntegerField(primary_key=True, max_length=5,default=0)
    name = models.CharField(max_length=150, null=False)
    gender = models.IntegerField(choices=gender_choices)
    email= models.EmailField(unique=True)
    birthdate = models.DateField()
    type= models.ForeignKey(ClientTypes,on_delete=models.CASCADE, default=0)

class Product(models.Model):
    pid = models.IntegerField(primary_key=True, max_length=5,default=0)
    name = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=500)
def __str__(self):
    return self.name
class Order(models.Model):
    oid = models.IntegerField(primary_key=True, max_length=5,default=0)
    cid= models.ForeignKey(Client,on_delete=models.CASCADE)
    pid= models.ForeignKey(Product,on_delete=models.CASCADE) #could be manytomany
    orderdate = models.DateField()
    shippingdate = models.DateField()