from rest_framework.routers import DefaultRouter
from .views import ShowtimeViewSet

router = DefaultRouter()

router.register("showtimes",ShowtimeViewSet)

urlpatterns = router.urls
