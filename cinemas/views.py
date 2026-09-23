from rest_framework.viewsets import ModelViewSet
from .models import Cinema, Hall, Seat
from .serializers import CinemaSerializer, HallSerializer, SeatSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

class CinemaViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    
class HallViewSet(ModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    
class SeatViewSet(ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
 