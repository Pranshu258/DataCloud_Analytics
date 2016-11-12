from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'geographic/$', views.geographic, name='geographic'),
    url(r'logout/$', views.logout_view, name='logout')
]