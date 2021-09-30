from django.urls import path
from .views import FloorViewSet

app_name = 'app'
urlpatterns = [
    path('api/floors/', FloorViewSet, name='floor'),
]
