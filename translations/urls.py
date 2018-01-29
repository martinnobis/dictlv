from django.conf.urls import url
from translations import views

urlpatterns = [
    url(r'srch/', views.search, name='view_search'),
    url(r'^(?P<term>[-\w]+)$', views.show_translation, name='show_translation'), 
]
