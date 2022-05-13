
from pyexpat import model
from django.db import models

# Create your models here.

class Common(models.Model):
    """ Define the common function to reduce and the reuseble code  """
    name = models.CharField(max_length=100)

    def __str__(self):                                              #-- str method 
        return self.name

    class Meta:
        abstract = True                                             #-- to not creation of the table om data base

class users(Common):                                                #-- common  is te base class of the users
    """ Cretae teh model of the user """
    address = models.TextField(max_length=200)
    email = models.CharField(max_length=100)
    mobile_number = models.IntegerField(unique=True)

    class Meta:
        db_table = "users"                                          #-- table create by these name

class Products(Common):
    """ Creating the model of Products """
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    
    def get_total_price(self):
        """ Define the function to get teh total price of the product """

        return f"{self.product_price * self.product_quantity}"

    class Meta:
        db_table = "prods"                                          #-- table create by these name

class Orders(models.Model):
    """ Creating the model of Orders """
    order_date = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ManyToManyField(users)

    class Meta:
        db_table = "order"                                          #-- table create by these name










