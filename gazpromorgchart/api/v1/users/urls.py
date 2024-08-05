from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, UserMeView, UserDetailView, ProjectsViewSet

router = DefaultRouter()

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/users/', UsersViewSet.as_view({'get': 'list'}), name='users-list'),
    path('api/v1/users/me', UserMeView.as_view(), name='user-me'),
    path('api/v1/users/<int:pk>', UserDetailView.as_view(), name='user-detail'),
    path('api/v1/projects/', ProjectsViewSet.as_view({'get': 'list'}), name='projects-list'),
]