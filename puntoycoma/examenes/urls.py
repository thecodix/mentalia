from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('submit_test/', views.submit_test, name='submit_test'),
    path('historico_tests/', views.historico_tests, name='historico_tests'),
    path('detalle_test/<int:test_id>/', views.detalle_test, name='detalle_test'),
]
