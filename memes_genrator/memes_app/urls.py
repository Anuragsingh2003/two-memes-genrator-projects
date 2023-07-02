from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_meme, name='generate_meme'),
    # Add more URL patterns as needed
]
