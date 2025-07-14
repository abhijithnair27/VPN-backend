# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse

from rest_framework import viewsets
from .models import Citizen
from .serializers import CitizenSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from authentication.models import User


class CreateCitizenView(generics.CreateAPIView):
    serializer_class = CitizenSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        # Check if the logged-in user already has a citizen linked
        if request.user.citizen:
            return Response(
                {"detail": "User already has a linked citizen."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        citizen = serializer.save()
        
        # Link the new citizen to the user
        request.user.citizen = citizen
        request.user.save()
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

    def create(self, request, *args, **kwargs):
        return Response(
            {"detail": "Use the 'create-citizen' endpoint to create a citizen."},
            status=status.HTTP_400_BAD_REQUEST
        )
