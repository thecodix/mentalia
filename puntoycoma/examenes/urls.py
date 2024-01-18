from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('submit_test/', views.submit_test, name='submit_test'),
    # Aquí puedes añadir más URLs para tus vistas
]
