from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, UserMeView, UserDetailView, ProjectsViewSet

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UsersViewSet.as_view({'get': 'list'}), name='users-list'),
    path('users/me', UserMeView.as_view(), name='user-me'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail'),
    path('projects/', ProjectsViewSet.as_view({'get': 'list'}), name='projects-list'),
]