# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.sub_view, name='url'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CitizenViewSet, CreateCitizenView

router = DefaultRouter()
router.register(r'citizen', CitizenViewSet)

urlpatterns = [
    path('create-citizen/', CreateCitizenView.as_view(), name='create-citizen'),
    path('', include(router.urls)),
]