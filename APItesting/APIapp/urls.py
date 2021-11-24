from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from APIapp import views

urlpatterns = [
    path('',views.EndPoints.index,name='index'),
    path('token/',views.EndPoints.token,name='token'),
    path('site/',views.EndPoints.get_site_from_dnac,name='get_site_from_dnac'),
    path('vlan/',views.EndPoints.get_vlan_from_dnac,name='get_vlan_from_dnac'),
    path('family/',views.EndPoints.get_device_family,name='get_device_family'),
    path('health/',views.EndPoints.get_site_health,name='get_site_health'),

]