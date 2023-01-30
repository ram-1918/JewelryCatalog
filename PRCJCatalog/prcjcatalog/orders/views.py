from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Orders, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerialzier
from rest_framework import generics, permissions, status


# Create your views here.

def practice(request):
    orders = Orders.objects.all()
    print(orders[0].get_cart_total)
    print(orders[0].no_of_items_in_cart)
    for i in orders:
        print(i.users.name, i.status)
    return HttpResponse({'values': orders})

# Order View - Create, retrieve, update, Destroy
class listOrdersView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class modifyOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

# OrderItem View - create, retrieve, update, destroy
class listOrderItemView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerialzier

class modifyOrderItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerialzier
