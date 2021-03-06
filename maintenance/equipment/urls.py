from django.urls import path

from . import views

app_name = 'equipment'
urlpatterns = [
    # /equipment/
    path('', views.EquipmentListView.as_view(), name='list'),

    # /equipment/locations
    path('locations/', views.LocationListView.as_view(), name='location_list'),

    # /equipment/BH1/
    path('<str:location_id>/', views.location, name='location'),

    # /equipment/BH2/90/
    path('<str:location_id>/<int:pk>/', views.EquipmentView.as_view(), name='info')

    # path('base/', views.base, name='base'),
]
