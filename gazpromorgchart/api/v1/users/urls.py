from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, UserMeView, UserDetailView, ProjectsViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='user')
router.register(r'projects', ProjectsViewSet, basename='project')
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/me', UserMeView.as_view(), name='user-me'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail'),
]