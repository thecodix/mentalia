# pylint: disable=redefined-outer-name
import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse


@pytest.fixture
def test_user():
    """Create and return a test user."""
    user = get_user_model()
    return user.objects.create_user(username='testuser', password='12345')

@pytest.fixture
def test_client():
    """Create and return a Django test client."""
    return Client()

@pytest.mark.django_db
def test_index_view(test_user, test_client):
    # Crea un usuario y haz login para cumplir con @login_required
    test_client.login(username=test_user.username, password='12345')
    url = reverse('index')  # Asegúrate de que 'index' es el nombre correcto de la URL de tu vista
    response = test_client.get(url)

    # Verifica que la respuesta es la esperada
    assert response.status_code == 200
    assert 'examenes/index.html' in [t.name for t in response.templates]
    assert 'carreras' in response.context
    assert 'cursos' in response.context
    assert 'asignaturas' in response.context
    assert 'temas' in response.context
    assert 'numero_preguntas_opciones' in response.context
