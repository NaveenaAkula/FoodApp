from rest_framework.serializers import ModelSerializer
from .models import Order, Menu, Customer


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        # fields = ('pk', 'customer', 'menu', 'orderType',
        #         'time_of_arrival', 'unit_size')


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
