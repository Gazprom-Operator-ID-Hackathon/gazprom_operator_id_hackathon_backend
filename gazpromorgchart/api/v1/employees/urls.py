from rest_framework.routers import DefaultRouter
from api.v1.employees.views import (
    EmploymentTypeViewSet, PositionViewSet, GradeViewSet, 
    EmployeeViewSet, SkillViewSet, ProductViewSet, 
    ProjectViewSet, ContactViewSet, EmailViewSet, PhoneViewSet
)

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

urlpatterns = router.urls