from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'verses',
                views.VerseViewSet,
                base_name='verse'
                )

urlpatterns = router.urls
