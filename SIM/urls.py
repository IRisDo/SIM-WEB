from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sim_list, name='sim_list'),
]