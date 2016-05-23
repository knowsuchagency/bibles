from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r"^verses/$", views.VerseList.as_view()),
    url(r"^verses/(?P<pk>[0-9]+)/$", views.VerseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

