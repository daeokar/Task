from django.shortcuts import render
from .models import Products, Orders, users
from .serializers import ProductSerializer, OrderSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from rest_framework.decorators import action

# Create your views here.

class ProductViewsets(ModelViewSet):
    """ Define the views for the Product """

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    #-- Customise url 
    @action(detail=True, methods=['get'], url_name="get_product_price")
    def get_book_total_price(self, request, pk=None):
        Prod_obj = Products.objects.get(id=pk)
        ret_val = Prod_obj.get_total_price()
        python_dict = {"Product Total Price" : ret_val}
        return JsonResponse(python_dict)

class OrderViewsets(ModelViewSet):
    """ Define the views for the Order """

    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class UsersViewsets(ModelViewSet):
    """ Define the views for the user """

    queryset = users.objects.all()
    serializer_class = UserSerializer

