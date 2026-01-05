from .views import EventsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', EventsView,basename='events')
urlpatterns = router.urls