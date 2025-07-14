from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import FIR
from .serializers import FIRSerializer

class FIRViewSet(viewsets.ModelViewSet):
    queryset = FIR.objects.all()
    serializer_class = FIRSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request, *args, **kwargs):
        # print("nice!!!!!!", request.user.citizen)
        # request.data["citizen"] = request.user.citizen.id
        data = request.data.copy()
        if hasattr(request.user, 'citizen'):  
            data["citizen"] = request.user.citizen.id
        else:
            return Response(
                {"detail": "Authenticated user does not have a linked Citizen profile."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = FIRSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
