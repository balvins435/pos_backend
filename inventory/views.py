# inventory/views.py
from rest_framework import viewsets
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.db.models import F
from rest_framework.response import Response
from django.db import models

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('name')
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def low_stock_items(request):
    items = Item.objects.filter(quantity__lte=models.F('low_stock_threshold'))
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
