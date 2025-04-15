from django.urls import path
from home.views import inicio

urlpatterns = [
    path('', inicio, name = 'inicio')
]