from  rest_framework import serializers
from  twitterbackend.models import Message, RegData

class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class RegDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegData
        fields = '__all__'

class AuthDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegData
        fields = ('phone', 'password')
