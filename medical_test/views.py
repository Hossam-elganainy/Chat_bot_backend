from django.shortcuts import render
from .models import Medical
from .serializers import MedicalSerializer
from rest_framework import generics, permissions, parsers

class MedicalCreateAPIView(generics.CreateAPIView):
    queryset = Medical.objects.all()
    serializer_class = MedicalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset()
    