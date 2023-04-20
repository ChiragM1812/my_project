from rest_framework import serializers
from .models import Payment
from order.serializers import OrderSerializer

class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ['order', 'amount']