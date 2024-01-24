# tests/test_views.py
import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_index_view():
    # Crea un usuario y haz login para cumplir con @login_required
    user = User.objects.create_user(username='testuser', password='12345')
    client = Client()
    client.login(username='testuser', password='12345')

    url = reverse('index')  # Asegúrate de que 'index' es el nombre correcto de la URL de tu vista
    response = client.get(url)

    # Verifica que la respuesta es la esperada
    assert response.status_code == 200
    assert 'examenes/index.html' in [t.name for t in response.templates]
    assert 'carreras' in response.context
    assert 'cursos' in response.context
    assert 'asignaturas' in response.context
    assert 'temas' in response.context
    assert 'numero_preguntas_opciones' in response.context
