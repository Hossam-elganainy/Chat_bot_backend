from .views import TestCreateAPIView
from django.urls import path

urlpatterns = [
    path('', TestCreateAPIView.as_view(), name='eye_test create'),
    # Add more URL patterns as needed for other API endpoints


]
