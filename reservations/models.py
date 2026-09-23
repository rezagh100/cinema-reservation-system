from django.db import models
from django.conf import settings
from cinemas.models import Seat
from showtimes.models import Showtime


class Reservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
    showtime = models.ForeignKey(
        Showtime, on_delete=models.CASCADE, related_name='reservations')
    seat = models.ForeignKey(
        Seat, on_delete=models.CASCADE, related_name='reservations')
    created_at = models.DateTimeField(auto_now_add=True)

    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )

    def __str__(self):
        return f"Reservation for {self.user.username} - {self.showtime.movie.title} at {self.showtime.start_time}"
