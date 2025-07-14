from rest_framework import serializers
from .models import FIR, Citizen

class FIRSerializer(serializers.ModelSerializer):
    class Meta:
        model = FIR
        fields = ['id', 'citizen', 'description', 'location', 'date', 'time', 'photos_or_videos', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

# class CitizenSerializer(serializers.ModelSerializer):
#     firs = FIRSerializer(many=True, read_only=True)

#     class Meta:
#         model = Citizen
#         fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'nationality', 'address', 'city', 'state', 'pin_code', 'phone_number', 'email', 'aadhaar_id', 'firs']
