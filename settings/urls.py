from django.urls import path
from .views import *

urlpatterns = [
    path('set_settings/', set_settings),
    path('get_settings/', get_settings),
]
