from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("admin/", admin.site.urls),

    path("cinema/", include("cinemas.urls")),
    path("showtime/", include("showtimes.urls")),
    path("reservation/", include("reservations.urls")),
    path("movie/", include("movies.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
