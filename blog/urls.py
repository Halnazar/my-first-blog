from django.urls import path, include
from .views import Aylar

urlpatterns = [
    path('', Aylar)
]