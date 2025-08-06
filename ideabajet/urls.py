from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('lokasi', views.lokasi, name='lokasi'),
    path('lokasi/delete/<int:lid>/', views.delete_lokasi, name='delete_lokasi'),
    path('aset', views.aset, name='aset'),
    path('aset/delete/<int:asetid>/', views.delete_aset, name='delete_aset'),
    path('e1', views.e1, name='e1'),
    path('e1/delete/<int:e1id>/', views.delete_e1, name='delete_e1'),
    path('e2', views.e2, name='e2'),
    path('e2/delete/<int:e2id>/', views.delete_e2, name='delete_e2'),
    path('e3', views.e3, name='e3'),
    path('e3/delete/<int:e3id>/', views.delete_e3, name='delete_e3'),
    path('e4', views.e4, name='e4'),
    path('e4/delete/<int:e4id>/', views.delete_e4, name='delete_e4'),
    path('e5', views.e5, name='e5'),
    path('e5/delete/<int:e5id>/', views.delete_e5, name='delete_e5'),
    path('e6', views.e6, name='e6'),
    path('e6/delete/<int:e6id>/', views.delete_e6, name='delete_e6'),
    path('e7', views.e7, name='e7'),
    path('e7/delete/<int:e7id>/', views.delete_e7, name='delete_e7'),
    path('e8', views.e8, name='e8'),
    path('e8/delete/<int:e8id>/', views.delete_e8, name='delete_e8'),
]