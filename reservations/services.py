from rest_framework.serializers import ValidationError
from .models import Reservation


class ReservationService():
    def check_seat_availability(self, seat, showtime):
        if Reservation.objects.filter(seat=seat, showtime=showtime, status__in=[
            Reservation.StatusChoices.PENDING,
            Reservation.StatusChoices.CONFIRMED
        ]).exists():
            raise ValidationError('this seat alredy reserved')
        self.reserv_seat(seat=seat, showtime=showtime)

    def reserv_seat(self, seat, showtime):
        self.check_seat_hall(showtime, seat)

    def check_seat_hall(self, showtime, seat):
        if showtime.hall != seat.hall:
            raise ValidationError(
                {'message': 'این صندلی متعلق به سالن این سانس نیست'})

    def create_reservation(self, seat, showtime, user):
        self.check_seat_availability(seat=seat, showtime=showtime)
        Reservation.objects.create(seat=seat, showtime=showtime, user=user)

    def cancel_reservation(self, reservation,user):
        if reservation.user != user:
            raise ValidationError({'message':'invalid request'})
        
        if reservation.status in (Reservation.StatusChoices.CONFIRMED,Reservation.StatusChoices.CANCELLED):
            raise ValidationError("Reservation is already cancelled or cannot be cancelled")
        
        reservation.status = Reservation.StatusChoices.CANCELLED
        reservation.save()