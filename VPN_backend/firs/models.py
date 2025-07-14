from django.db import models
from django.conf import settings
from citizen.models import Citizen

class FIR(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE, related_name='firs')
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    photos_or_videos = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"FIR by {self.citizen.first_name} {self.citizen.last_name} on {self.date}"
