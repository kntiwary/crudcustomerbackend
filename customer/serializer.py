from rest_framework import serializers
from .models import Customer
Customer = Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

