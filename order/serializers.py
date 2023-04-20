from rest_framework import serializers
from .models import Order, User
from user.serializers import UserSerializer
from product.serializers import BookSerializer
from user.models import *

class OrderSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data.pop('user')
        validated_data['user_id'] = user.id
        order = super().create(validated_data)
        return order
    
        user = UserSerializer(read_only=True)
    products = BookSerializer(many=True, read_only=True)

    # user = UserSerializer()
    # class Meta:
    #     model = Order
    #     fields = ['user', 'products', 'total_amount']

    #     def create(self, validated_data):
    #         user_data = validated_data.pop('user')

    #         user = User.objects.create(**user_data)
            
    #         book = User.objects.create(
    #             user=user,
    #             **validated_data
    #         )
    #         return book