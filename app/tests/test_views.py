# pylint: disable=redefined-outer-name, unused-argument
import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from examenes.models import (
    Asignatura,
    Carrera,
    Curso,
    OpcionDeRespuesta,
    Pregunta,
    Tema,
    TestRealizado,
)


@pytest.fixture
def test_user():
    """Create and return a test user."""
    user = get_user_model()
    return user.objects.create_user(username='testuser', password='12345')

@pytest.fixture
def test_client():
    """Create and return a Django test client."""
    return Client()


@pytest.fixture
def client_authenticated(test_user, test_client):
    test_client.force_login(test_user)
    return test_client, test_user


@pytest.fixture
def carrera(db):
    return Carrera.objects.create(nombre="Psicología")


@pytest.fixture
def curso(carrera):
    curso = Curso.objects.create(nombre="Cuarto", carrera=carrera)
    return curso


@pytest.fixture
def asignatura(curso):
    asignatura = Asignatura.objects.create(nombre="Dificultades", curso=curso)
    return asignatura

@pytest.fixture
def tema(asignatura):
    tema = Tema.objects.create(nombre="Tema 1 - EID", asignatura=asignatura)
    return tema


@pytest.fixture
def questions(tema):
    questions = []
    for i in range(1, 4):
        question = Pregunta.objects.create(texto=f"Pregunta {i} ¿Es verdadero o falso?", tema=tema)
        OpcionDeRespuesta.objects.create(pregunta=question, texto="Verdadero", es_correcta=True)
        OpcionDeRespuesta.objects.create(pregunta=question, texto="Falso", es_correcta=False)
        questions.append(question)
    return questions


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
    #assert 'cursos' in response.context
    #assert 'asignaturas' in response.context
    #assert 'temas' in response.context
    #assert 'numero_preguntas_opciones' in response.context
    # TODO create tests for all views


@pytest.mark.django_db
def test_single_question_correct(client_authenticated, questions):
    client, user = client_authenticated
    question1 = questions[0]
    correct_answer_id = question1.opcionderespuesta_set.get(es_correcta=True).id

    response = client.post(
        reverse('submit_test'),
        {'pregunta_' + str(question1.id): correct_answer_id}
    )

    # Validaciones
    assert response.status_code == 200
    test_realizado = TestRealizado.objects.get(usuario=user)
    assert test_realizado.preguntas_correctas == 1
    assert test_realizado.preguntas_falladas == 0
    assert test_realizado.preguntas_no_contestadas == 0


@pytest.mark.django_db
def test_three_questions_mixed_responses(client_authenticated, questions):
    client, user = client_authenticated
    question1, question2, question3 = questions

    correct_answer_id = question1.opcionderespuesta_set.get(es_correcta=True).id
    incorrect_answer_id = question2.opcionderespuesta_set.get(es_correcta=False).id

    response = client.post(reverse('submit_test'), {
        'pregunta_' + str(question1.id): correct_answer_id,
        'pregunta_' + str(question2.id): incorrect_answer_id,
        'pregunta_' + str(question3.id): 'no_contestada'
    })

    # Validaciones
    assert response.status_code == 200
    test_realizado = TestRealizado.objects.get(usuario=user)
    assert test_realizado.preguntas_correctas == 1
    assert test_realizado.preguntas_falladas == 1
    assert test_realizado.preguntas_no_contestadas == 1
