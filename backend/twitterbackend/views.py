from rest_framework import generics
from .serializers import MessageSerializers, RegDataSerializers, AuthDataSerializers
from .models import Message, RegData
from rest_framework.response import Response

class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializers

class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializers
    queryset = Message.objects.all().order_by('-id')

class RegistrationUser(generics.CreateAPIView):
    serializer_class = RegDataSerializers

class AuthenticationUser(generics.ListAPIView):
    serializer_class = AuthDataSerializers
    queryset = RegData.objects.all()

    def post(self, request):
        phone = request.data['phone']
        password = request.data['password']
        queryset = RegData.objects.filter(phone=phone, password=password)
        serializer = AuthDataSerializers(queryset, many=True)
        return Response(serializer.data)