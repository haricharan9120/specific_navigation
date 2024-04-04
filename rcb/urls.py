from django.urls import path
from rcb.views import *
app_name='rcb'
urlpatterns = [
    path('faf/',faf,name='faf'),
    path('cheeku/',cheeku,name='cheeku'),
]