from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'User', UserViewSet)
router.register(r'Book', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', CustomObtainAuthToken.as_view()),
]