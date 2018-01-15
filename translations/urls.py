from django.conf.urls import url
from translations import views

urlpatterns = [
    url(r'^search$', views.search, name='view_search'),
    url(r'^(?P<text>.+)$', views.result, name='view_result'),
]
