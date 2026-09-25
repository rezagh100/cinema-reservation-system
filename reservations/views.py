from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer
from .services import ReservationService
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404

class ReservationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        seat = serializer.validated_data['seat']
        showtime = serializer.validated_data['showtime']
        user = self.request.user
        service = ReservationService()
        service.create_reservation(seat=seat, showtime=showtime, user=user)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        reservation = get_object_or_404(Reservation, pk=pk)
        service = ReservationService()
        service.cancel_reservation(reservation=reservation,user=request.user)
        return Response({'message':'Reservation cancelled successfully'},status=status.HTTP_200_OK)
        