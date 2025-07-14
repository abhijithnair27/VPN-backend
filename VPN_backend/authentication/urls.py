from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignupView



urlpatterns = [
    # path('create-citizen/', CreateCitizenView.as_view(), name='create-citizen'),
    path('signup/', SignupView.as_view(), name='signup'),
    
]