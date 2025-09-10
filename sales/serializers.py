# sales/serializers.py
from rest_framework import serializers
from .models import Sale, SaleItem
from customers.models import Customer

class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ['item', 'quantity', 'unit_price']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'email', 'date_joined', 'loyalty_points']
class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    customer_phone = serializers.CharField(write_only=True, required=False)
    
    read_only_fields = ['customer', 'total']

    class Meta:
        model = Sale
        fields = ['id', 'user', 'customer', 'date', 'total', 'payment_method', 'items', 'customer_phone']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        phone = validated_data.pop('customer_phone', None)

        # Auto-create or fetch customer
        customer = None
        if phone:
            customer, _ = Customer.objects.get_or_create(phone=phone, defaults={
                'name': 'Walk-in',
                'email': None
            })

        # Calculated total
        total = sum(item['quantity'] * item['unit_price'] for item in items_data)

        # ✅ Ensure customer is linked
        sale = Sale.objects.create(customer=customer, **validated_data)
     

        # Add items to sale
        for item_data in items_data:
            SaleItem.objects.create(sale=sale, **item_data)

        # Award loyalty points
        if customer:
            points = sale.total // 100  # 1 point per 100 KES
            customer.loyalty_points += points
            customer.save()

        return sale
