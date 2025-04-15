from django import path
from home.views import inicio

urlpatterns = [
    path('', inicio, Name = 'inicio')
]