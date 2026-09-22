from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("cinema/", include("cinemas.urls")),
    path("showtime/", include("showtimes.urls")),
    path("reservation/", include("reservations.urls")),
    path("movie/", include("movies.urls")),
]
