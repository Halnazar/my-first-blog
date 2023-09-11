from django.urls import path, include
from .views import aylar

urlpatterns = [
    path('', aylar)
]