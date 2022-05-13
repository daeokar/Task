from Product.models import Products, Orders, users
from rest_framework import serializers

#-- serializer for product
class ProductSerializer(serializers.ModelSerializer):
    """ Define the serializer for the Product  """

    class Meta:
        model = Products
        fields = "__all__"

#-- serializer for order
class OrderSerializer(serializers.ModelSerializer):
    """ Define the serializer for the Order  """

    class Meta:
        model = Orders
        fields = "__all__"

#-- serializer for user
class UserSerializer(serializers.ModelSerializer):
    """ Define the serializer for the users  """

    class Meta:
        model = users
        fields = "__all__"
