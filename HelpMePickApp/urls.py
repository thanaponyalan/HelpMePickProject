from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('activity/',views.act,name='activity'),
    path('getActivity/',views.getAct,name='getActivity')
]
