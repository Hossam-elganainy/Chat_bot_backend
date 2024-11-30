from .views import TestCreateAPIView
from django.urls import path

urlpatterns = [
    path('', TestCreateAPIView.as_view(), name='test create'),
    # Add more URL patterns as needed for other API endpoints


]
