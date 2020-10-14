from rest_framework import serializers
from .models import*

class RegisterSerializer(serializers.ModelSerializer):
   class Meta:
       model = Registration
       depth = 1 
       fields = ('__all__')