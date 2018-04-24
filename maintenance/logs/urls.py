from django.urls import path

from . import views

#logs app
app_name = 'logs'
urlpatterns = [
    # /maintenance/
    path('', views.index, name='index'),
    path('logs/', views.index),
    path('services/', views.index)
]
