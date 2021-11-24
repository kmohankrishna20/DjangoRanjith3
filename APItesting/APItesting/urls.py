from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from APIapp import views

urlpatterns = [
    path('APIapp/',include('APIapp.urls')),
    path('admin/', admin.site.urls),
]