from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
import logging

from .models import FIR
from .serializers import FIRSerializer


logger = logging.getLogger('VPN_backend.fir.views')


class FIRViewSet(viewsets.ModelViewSet):
    queryset = FIR.objects.all()
    serializer_class = FIRSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        cache_key = f"fir_list_user_{request.user.id}"
        cached_data = cache.get(cache_key)

        if cached_data:
            logger.info(f"Cache hit for {cache_key}")
            return Response(cached_data)

        logger.info(f"Cache miss for {cache_key}")
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        cache.set(cache_key, data, timeout=60 * 5)  # Cache for 5 minutes
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        cache_key = f"fir_detail_{instance.id}"
        cached_data = cache.get(cache_key)

        if cached_data:
            logger.info(f"Cache hit for {cache_key}")
            return Response(cached_data)

        logger.info(f"Cache miss for {cache_key}")
        serializer = self.get_serializer(instance)
        data = serializer.data
        cache.set(cache_key, data, timeout=60 * 5)
        return Response(data)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if hasattr(request.user, 'citizen'):
            data["citizen"] = request.user.citizen.id
        else:
            logger.warning("User without citizen tried to create FIR")
            return Response(
                {"detail": "Authenticated user does not have a linked Citizen profile."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = FIRSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            logger.info(f"FIR created with ID {instance.id}")
            # Invalidate relevant cache
            cache.delete(f"fir_list_user_{request.user.id}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.error(f"FIR creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
