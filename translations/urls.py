"""URLS for the translation app."""

from django.conf.urls import url
from translations import views

urlpatterns = [
    url(r'srch/', views.search, name='view_search'),
    url(r'^(?P<language>(en|lv))/(?P<term>[\w]+)', views.show_translation, name='show_translation'),
]
