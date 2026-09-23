from rest_framework.serializers import ModelSerializer
from .models import User
from django.contrib.auth.models import Group

class RegisterSerializer(ModelSerializer):
    def create(self,validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        customer_group = Group.objects.get(name='Customer')
        user.groups.add(customer_group)
        return user
    
    class Meta:
        model = User
        fields = ['username', 'password', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
        
