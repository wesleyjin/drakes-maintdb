from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	# /equipment/locations
    path('locations/', views.plant_locations, name='plant_locations'),
    # /equipment/BH1/
    path('<str:location_id>/', views.location, name = 'location'),
    # /equipment/bh1/kettle1/
    path('<str:location_id>/<int:equipment_id>/', views.info, name = 'info')
]