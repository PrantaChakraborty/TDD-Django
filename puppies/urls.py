from rest_framework.routers import DefaultRouter

from .views import PuppyAPIViewSet

router = DefaultRouter()

router.register(r'', PuppyAPIViewSet, basename='puppies')

urlpatterns = router.urls
