from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'crm'
urlpatterns = [

    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
]
