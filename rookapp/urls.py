from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('spage',views.spage,name='spage')
]
