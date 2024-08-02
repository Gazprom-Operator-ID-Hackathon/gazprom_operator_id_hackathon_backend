from rest_framework import viewsets, generics, status, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from core.users.models import Users
from .serializers import UsersSerializer, UsersLimitedSerializer, RegisterSerializer, UserSerializer

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для получения списка пользователей с ограниченным набором полей"""
    queryset = Users.objects.all()
    serializer_class = UsersLimitedSerializer
    operation_description = "Получение списка пользователей для формирования диаграммы"

class UserMeView(generics.RetrieveUpdateAPIView):
    """Вьюсет для получения и редактирования данных текущего пользователя"""
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    operation_description = "Получение и обновление данных текущего пользователя"

    def get_object(self):
        user = self.request.user
        try:
            users_profile = Users.objects.get(user=user)
        except Users.DoesNotExist:
            raise serializers.ValidationError("Профиль пользователя не найден.")
        return users_profile

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вьюсет для получения данных другого пользователя по ID и выполнения CRUD операций"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'pk'
    operation_description = "Получение, создание, обновление и удаление данных пользователя по ID"

class RegisterView(generics.CreateAPIView):
    """Вьюсет для регистрации нового пользователя"""
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'token': token.key
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class LoginView(ObtainAuthToken):
    """Вьюсет для аутентификации пользователя"""
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)