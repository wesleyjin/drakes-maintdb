from django.urls import path

from . import views

app_name = 'equipment'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	# /equipment/locations
    path('locations/', views.plant_locations, name='plant_locations'),
    # /equipment/BH1/
    path('<str:location_id>/', views.location, name = 'location'),
    # /equipment/bh1/kettle1/
    path('<str:location_id>/<int:pk>/', views.EquipmentView.as_view(), name = 'info')
]