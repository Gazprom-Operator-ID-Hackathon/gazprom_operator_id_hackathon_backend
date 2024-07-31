from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from api.v1.employees.views import (
    EmploymentTypeViewSet, PositionViewSet, GradeViewSet, 
    EmployeeViewSet, SkillViewSet, ProductViewSet, 
    ProjectViewSet, ContactViewSet, EmailViewSet, PhoneViewSet
)

# Настройка для drf_yasg
schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="API документация",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Настройка маршрутов для ViewSet
router = DefaultRouter()
router.register(r'employment-types', EmploymentTypeViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'products', ProductViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'emails', EmailViewSet)
router.register(r'phones', PhoneViewSet)

# Основные маршруты
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/', include(router.urls)),
]