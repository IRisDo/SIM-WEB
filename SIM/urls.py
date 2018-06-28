from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sim_list, name='sim_list'),
    url(r'^payment/(?P<pk>\d+)/$', views.payment, name = 'payment'),
    url(r'^payment/(?P<pk>\d+)/payment_submit$', views.payment_submit, name = 'payment_submit'),
]