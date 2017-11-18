from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'(?P<subcategoryid>[0-9]+)/stock/$', views.getstock, name='getstock'),
    url(r'^stockjson/',views.stockjson),
    url(r'^purchase/',views.purchase,name='purchase'),
    url(r'^processedproducts/',views.processedproducts),
    url(r'^profit/',views.profit,name='profit'),
    url(r'^test/',views.test),
]

