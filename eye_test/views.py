from django.shortcuts import render
from .serializers import TestSerializer
from .models import Test
from rest_framework import generics, permissions, parsers
from rest_framework.response import Response
from rest_framework import status

def test_ai_model(image):
    return 0.75

class TestCreateAPIView(generics.CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (parsers.MultiPartParser,parsers.FormParser)

    def post(self, request, *args, **kwargs):

        user = request.user

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            test = serializer.save(user=user)

            # Example AI model processing function
            ai_score = test_ai_model(test.attachment)
            test.response = ai_score
            test.save()

            response = {
                'message': "Test created successfully."
            }

            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)