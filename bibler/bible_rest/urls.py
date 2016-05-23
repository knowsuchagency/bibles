from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r"^verses/$", views.verse_list),
    url(r"^verses/(?P<pk>[0-9]+)/$", views.verse_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

