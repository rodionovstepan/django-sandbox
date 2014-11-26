from django.conf.urls import patterns, include, url
from viewer.views import px

urlpatterns = patterns('',
    url(r'^px/(\d+)/', px),
)