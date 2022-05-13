from django.contrib import admin
from Product.models import Orders, Products, users

# Register your models here.

admin.site.register([Products, users, Orders])

