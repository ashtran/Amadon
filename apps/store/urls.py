from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon/buy$', views.process),
    url(r'^amadon/checkout$', views.cart),
    url(r'^amadon/s3cr3tcl3arp00pybutth0le$', views.secretclear),
]
