from django.conf.urls import url
from translations import views

urlpatterns = [
    # The order here is very imporant!!
    url(r'^k/srch$', views.search, name='view_search'),
    url(r'^(?P<text>.+)/$', views.result, name='view_result'),
]
