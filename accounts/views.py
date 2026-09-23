from .serializers import RegisterSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterAPIView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            return Response({'message':'user registered successfully',
                             'username':user.username},status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )