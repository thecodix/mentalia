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

    path('get_cursos/', views.get_cursos, name='get_cursos'),
    path('get_asignaturas/', views.get_asignaturas, name='get_asignaturas'),
    path('get_temas/', views.get_temas, name='get_temas'),
    path('lista_asignaturas/', views.lista_asignaturas, name='lista_asignaturas'),
    path('seleccionar_asignatura/', views.seleccionar_asignatura, name='seleccionar_asignatura'),
    path('asignatura/desbloquear/<int:asignatura_id>/', views.desbloquear_asignatura, name='desbloquear_asignatura'),

    path('roadmap/<int:asignatura_id>/', views.roadmap, name='roadmap'),
    path('seccion/<int:seccion_id>/', views.detalle_seccion, name='detalle_seccion'),
    path('subseccion/test/<int:subseccion_id>/', views.realizar_test_subseccion, name='realizar_test_subseccion')

]
