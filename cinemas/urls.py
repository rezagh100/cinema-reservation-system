from rest_framework.routers import DefaultRouter
from .views import CinemaViewSet, HallViewSet, SeatViewSet


router = DefaultRouter()

router.register("cinemas",CinemaViewSet)
router.register("halls",HallViewSet)
router.register("seats",SeatViewSet)

urlpatterns = router.urls
