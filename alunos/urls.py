from alunos.views import AlunosViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AlunosViewSet)
urlpatterns = router.urls
