from django.shortcuts import render, redirect
from .forms import OrderForms
# Create your views here.
from .REST_API import *

resp = RestApi()

def welcome(request):
    return render(request, "home.html", {"form" : OrderForms(), "orders" : resp.get_all_order()})

def save_order(request):
    """ Define the view function to save the data """

    if request.method == "POST":
        order_obj = COrder(order_date=request.POST["order_date"],
                            product=request.POST["product"],
                            user=request.POST["user"])
        # print(order_obj.__dict__)
        resp.post_order(order_obj)
        return redirect("home")


