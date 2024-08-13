from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, UserMeView, UserDetailView, ProjectsViewSet, ITComponentViewSet, ProjectsView, RegisterView, MyTokenObtainPairView

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='user')
router.register(r'projects', ProjectsViewSet, basename='project')
router.register(r'itcomponents', ITComponentViewSet, basename='itcomponent')

urlpatterns = [
    path('', include(router.urls)),
    path('users/me', UserMeView.as_view(), name='user-me'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail'),
    path('projects', ProjectsView.as_view(), name='projects'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
