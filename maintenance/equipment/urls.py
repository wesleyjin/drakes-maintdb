from django.urls import path

from . import views

urlpatterns = [
	# /equipment/
    path('', views.index, name='index'),
    # /equipment/bh1/
    path('<str:location_id>/', views.location, name = 'location'),
    # /equipment/kettle1/
    path('<int:equipment_id>/', views.info, name = 'info')
]