from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_meme_image/', views.generate_captioned_image, name='generate_captioned_image'),
        # Add more URL patterns as needed
]
