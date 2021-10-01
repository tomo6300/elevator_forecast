from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('api/floors/<int:pk>', views.floor, name='floor'),
]
