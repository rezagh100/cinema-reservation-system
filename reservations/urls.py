from rest_framework.routers import DefaultRouter
from .views import ReservationViewSet

router = DefaultRouter()

router.register("reservations",ReservationViewSet)

urlpatterns = router.urls
