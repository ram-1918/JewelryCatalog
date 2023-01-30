from django.shortcuts import render
from products.models import Products, Price, GoldPrice, Category
from products.serializers import ProductSerializer, PriceSerializer, GoldPriceSerializer, CategorySerializer
from rest_framework import generics, permissions, status

# Create your views here.

# Product View - list
class listProductsView(generics.ListCreateAPIView):
    # goldprice = 192.23
    # Products.objects.update(price = F('price')*goldprice)
    # print(Products.objects.all())
    # print("select ", Products.objects.select_related('category').all())
    # print("prefetch_related ", Products.objects.prefetch_related('category').all())
    queryset = Products.objects.all() #prefetch_related('price').all()
    serializer_class = ProductSerializer

class getProductsView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

# Products with prices view
class listPriceView(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class getPriceView(generics.RetrieveAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

# Gold Price (Should be an API call to get LIVE price)
class createGoldPriceView(generics.CreateAPIView):
    queryset = GoldPrice.objects.all()
    serializer_class = GoldPriceSerializer

class updateGoldPriceView(generics.RetrieveUpdateAPIView):
    queryset = GoldPrice.objects.all()
    serializer_class = GoldPriceSerializer

# Category View - list
class listCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
