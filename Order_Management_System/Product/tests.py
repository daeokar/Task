from django.test import TestCase, Client
from .models import *
from .serializers import *
from rest_framework import status
from django.urls import reverse

client = Client()

# Create your tests here.

class GetSinglProductTest(TestCase):
    """ Test module for GET single puppy API """

    def setUp(self):
        self.Laptop = Products.objects.create(
            name='Laptop', product_price=48000, product_quantity=8)
        self.TV = Products.objects.create(
            name='TV', product_price=12000, product_quantity=12)
        self.Mobile = Products.objects.create(
            name='Mobile', product_price=22000, product_quantity=9)

    def test_get_valid_single_Product(self):
        response = client.get(reverse('Prods', kwargs={'pk': self.Laptop.pk}))
        puppy = Products.objects.get(pk=self.Laptop.pk)
        serializer = ProductSerializer(puppy)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(
            reverse('Prods', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


