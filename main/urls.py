from django.urls import path
from .views import index, execute , playground

urlpatterns = [
    path('', index),
    path('<id>/', playground),
    path('execute/', execute),
]
