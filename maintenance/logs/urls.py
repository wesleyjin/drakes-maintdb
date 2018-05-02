from django.urls import path
from django.conf.urls import url

from . import views

#logs app
app_name = 'logs'
urlpatterns = [
    # /maintenance/
    # TODO: edit below to use HOMEPAGE view
    path('', views.HomepageView.as_view(), name='index'),
    path('logs/', views.LogListView.as_view(), name='logs'),
    path('logs/<int:pk>', views.LogDetailView.as_view(), name='log_detail'),
    path('service/', views.ServiceListView.as_view(), name='services'),
    url(r'^service/page=(?P<page>\d+)', views.ServiceListView.as_view(), name='sp'),
    path('service/<int:pk>', views.ServiceDetailView.as_view(), name='service_detail')
]
