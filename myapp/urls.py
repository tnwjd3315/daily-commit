from django.urls import path
from myapp import views

# routing
urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read)
]
