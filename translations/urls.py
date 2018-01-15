from django.conf.urls import url
from translations import views

urlpatterns = [
    url(r'(?P<text>.+)$', views.result, name='result'),
    url('search', views.search, name='search'),
]
