from django.urls import path
import views

urlpatterns = [
    path('reviews/', views.respond, name='respond')
]
