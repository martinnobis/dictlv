from django.conf.urls import url
from translations import views

urlpatterns = [
    url(r'^(\d+)/$', views.home_page, name='home_page'),
]