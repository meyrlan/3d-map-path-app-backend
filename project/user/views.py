from rest_framework.generics import CreateAPIView
from user.models import User
from user.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
