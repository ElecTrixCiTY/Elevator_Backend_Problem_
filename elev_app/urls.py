from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElevatorViewSet, RequestViewSet

router = DefaultRouter()
router.register(r'elevators', ElevatorViewSet)
router.register(r'requests', RequestViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
