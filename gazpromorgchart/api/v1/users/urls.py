from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, UserMeView, UserDetailView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UsersViewSet.as_view({'get': 'list'}), name='users-list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail'),
    path('users/me', UserMeView.as_view(), name='user-me'),
]