from django.urls import path
from . import views

urlpatterns = [
    path('api/river-map/', views.get_river_map, name='get_river_map'),
]
