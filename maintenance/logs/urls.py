from django.urls import path

from . import views

#logs app
app_name = 'maintenance'
urlpatterns = [
    # /maintenance/
    path('', views.index, name='index'),
]
