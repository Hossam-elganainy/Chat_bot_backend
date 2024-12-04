from .views import MedicalCreateAPIView
from django.urls import path

urlpatterns = [
   path('', MedicalCreateAPIView.as_view(), name='Tests_create'),  # Replace 'Tests_create' with your API endpoint name
   


]
