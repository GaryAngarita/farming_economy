from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_crops', views.process_crops),
    path('process_gold', views.process_gold),
    path('delete', views.delete)
]