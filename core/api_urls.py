from rest_framework.routers import DefaultRouter

from .api_views import ProjectViewSet, SkillCategoryViewSet, CertificationViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="api-project")
router.register("skills", SkillCategoryViewSet, basename="api-skill-category")
router.register("certifications", CertificationViewSet, basename="api-certification")

urlpatterns = router.urls
