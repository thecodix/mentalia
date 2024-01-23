from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('submit_test/', views.submit_test, name='submit_test'),
    path('historico_tests/', views.historico_tests, name='historico_tests'),
    path('detalle_test/<int:test_id>/', views.detalle_test, name='detalle_test'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),  # Añade las URLs de autenticación
    path('logout/', views.custom_logout, name='custom_logout'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
