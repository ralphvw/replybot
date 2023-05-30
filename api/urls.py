from django.urls import path
from .views import respond

urlpatterns = [
    path('reviews/', respond, name='respond')
]
