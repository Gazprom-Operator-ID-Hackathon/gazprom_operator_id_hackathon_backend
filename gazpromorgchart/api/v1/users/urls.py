from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, UserMeView, UserDetailView

router = DefaultRouter()
router.register(r'user', UsersViewSet)  # Изменено с 'users' на 'user'

urlpatterns = [
    path('', include(router.urls)),
    path('me/', UserMeView.as_view(), name='user-me'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Изменено с 'id' на 'pk'
]