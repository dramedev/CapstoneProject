from django.urls import path, include
from rest_framework import routers
from .views import MenuViewSet, BookingViewSet


router = routers.DefaultRouter()

router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


