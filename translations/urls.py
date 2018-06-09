"""URLS for the translation app."""

from django.conf.urls import url
from translations import views

urlpatterns = [
    url(r's/', views.search, name='search'),
    url(r'^(?P<term>[\w]+)', views.show_translation, name='show_translation'),
]
