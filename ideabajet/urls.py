from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('lokasi', views.lokasi, name='lokasi'),
    path('lokasi/delete/<int:lid>/', views.delete_lokasi, name='delete_lokasi'),
    path('e1', views.e1, name='e1'),
    path('e1/delete/<int:e1id>/', views.delete_e1, name='delete_e1'),
    path('e2', views.e2, name='e2'),
    path('e2/delete/<int:e2id>/', views.delete_e2, name='delete_e2'),
    path('e3', views.e3, name='e3'),
    path('e3/delete/<int:e3id>/', views.delete_e3, name='delete_e3'),
    path('e4', views.e4, name='e4'),
    path('e4/delete/<int:e4id>/', views.delete_e4, name='delete_e4'),
]