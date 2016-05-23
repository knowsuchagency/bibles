from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'verses', views.VerseViewSet)
urlpatterns = router.urls
