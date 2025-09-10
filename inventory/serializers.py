# inventory/serializers.py
from rest_framework import serializers
from .models import Item, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        # Extract and handle category
        category_data = validated_data.pop("category")
        category, _ = Category.objects.get_or_create(**category_data)
        # Create the item
        item = Item.objects.create(category=category, **validated_data)
        return item

    def to_representation(self, instance):
        """Ensure category is always returned as full object"""
        representation = super().to_representation(instance)
        representation["category"] = CategorySerializer(instance.category).data
        return representation

