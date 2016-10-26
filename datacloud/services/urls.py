from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'api$', views.api, name='api'),
    url(r'collect$', views.collect, name='collect')
]