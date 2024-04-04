from django.urls import path
from csk.views import *
app_name='csk'
urlpatterns=[
    
    path('ruturaj/',ruturaj,name='ruturaj'),
    path('maahi/',maahi,name='maahi'),
]