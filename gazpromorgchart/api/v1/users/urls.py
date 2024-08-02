from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, UserMeView, UserDetailView, RegisterView, LoginView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UsersViewSet.as_view({'get': 'list'}), name='users-list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail'),
    path('users/me', UserMeView.as_view(), name='user-me'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]