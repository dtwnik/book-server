from datetime import datetime

from django.utils import timezone
# from django.utils import timezone
# from rest_framework import serializers
# from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import *


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user



# class OrderSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'
#         read_only_fields = ('due_date',)
#
#     def create(self, validated_data):
#         book_data = validated_data.pop('book')
#
#         validated_data['created_at'] = datetime.now()
#         validated_data['due_date'] = timezone.now().date() + timedelta(days=7)
#
#         order = Order.objects.create(**validated_data)
#
#         for book in book_data:
#             order.book.add(book)
#
#         return order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('due_date',)

    def create(self, validated_data):
        book_names = validated_data.pop('book')

        validated_data['created_at'] = datetime.now().date()
        validated_data['due_date'] = timezone.now().date() + timedelta(days=7)

        order = Order.objects.create(**validated_data)
        order.book = ''.join(book_names)
        order.save()

        return order



