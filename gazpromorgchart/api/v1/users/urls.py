from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, UserMeView, UserDetailView

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('user/me/', UserMeView.as_view(), name='user-me'),
    path('user/<int:id>/', UserDetailView.as_view(), name='user-detail'),
]