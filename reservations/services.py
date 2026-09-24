from rest_framework.serializers import ValidationError
       
class ReservationService():
    
    def check_seat_hall(self,showtime,seat):
        if showtime.hall != seat.hall:
            raise ValidationError({'message':'این صندلی متعلق به سالن این سانس نیست'})
        
    def reserv_seat(self,seat,showtime):
        self.check_seat_hall(showtime,seat)
        
