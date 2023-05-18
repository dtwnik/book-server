from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .serializer import *
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user_id=response.data["id"])

        user = User.objects.get(id=response.data["id"])
        Deposite.objects.create(owner=user, deposite=0)

        response.data["token"] = str(token)

        # Deposite.objects.create(owner=response.data["id"], deposit=0)

        return response


# class CustomObtainAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data['token'])
#         return Response({
#             'token': token.key,
#             'id': token.user_id,
#         })

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token': token.key,
            'id': user.id,
            'username': user.username,
            'last_name': user.last_name,
            'first_name': user.first_name,
            'email': user.email
        })


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['genre']

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(buyers=user)


class DepositeViewSet(viewsets.ModelViewSet):
    queryset = Deposite.objects.all()
    serializer_class = DepositeSerializer

    def get_queryset(self):
        user = self.request.user
        return Deposite.objects.filter(owner=user)

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)