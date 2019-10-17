from rest_framework.routers import DefaultRouter
from .apiviews import MoisViewSet, ModuleViewSet, ChapitreViewSet, CoursViewSet, UsercourseViewSet


router = DefaultRouter()
router.register('mois', MoisViewSet, base_name='mois')
router.register('module', ModuleViewSet, base_name='module')
router.register('chapitre', ChapitreViewSet, base_name='chapitre')
router.register('cours', CoursViewSet, base_name='cours')
router.register('usercourse', UsercourseViewSet, base_name='usercourse')

urlpatterns = [
    # ...
]

urlpatterns += router.urls