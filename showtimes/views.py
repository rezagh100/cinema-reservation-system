from rest_framework.viewsets import ModelViewSet
from .models import Showtime
from .serializers import ShowtimeSerializer


class ShowtimeViewSet(ModelViewSet):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer