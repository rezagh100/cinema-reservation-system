from rest_framework.serializers import ValidationError


       
class ReservationService():
    
    def check_seat(self,):
            
        
        
        
class CheckSeatAndHall():
    def check_seat_with_hall(self,showtime,seat):
        if showtime.hall != seat.hall:
            raise ValidationError({'message':'این صندلی متعلق به سالن این سانس نیست'})
        
 
    