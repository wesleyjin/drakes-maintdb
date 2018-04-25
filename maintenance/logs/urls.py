from django.urls import path

from . import views

#logs app
app_name = 'logs'
urlpatterns = [
    # /maintenance/
    # TODO: edit below to use HOMEPAGE view
    path('', views.index, name='index'),
    path('logs/', views.LogListView.as_view(), name='logs'),
    # path('logs/<int: pk>', views.LogDetailView.as_view(), name='log_detail'),
    path('service/', views.ServiceListView.as_view(), name='services'),
    # path('service/<int: pk>', views.ServiceDetailView.as_view(), name='service_detail'),
]
