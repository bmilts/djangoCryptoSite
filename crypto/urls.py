from django.urls import path
from . import views

urlpatterns = [
	   path('', views.home, name="home"), 
	   path('prices/', views.prices, name="prices"),
	   path('identity/', views.identity, name="identity"),
	   path('address/', views.address, name="address"),
]
