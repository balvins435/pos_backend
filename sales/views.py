# sales/views.py
from rest_framework import viewsets
from .models import Sale
from .serializers import SaleSerializer
from rest_framework.permissions import IsAuthenticated

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('-date')
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
