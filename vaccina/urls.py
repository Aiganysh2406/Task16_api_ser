from django.contrib import admin
from django.urls import path, include
from .views import get_vaccina, create_vacina, get_one_vaccina



urlpatterns = [
    path('get_vaccina/<int:id>/', get_vaccina)
]