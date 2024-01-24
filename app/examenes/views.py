import random

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render

from .services import process_test_submission
from .models import (
    Asignatura,
    Carrera,
    Curso,
    OpcionDeRespuesta,
    Pregunta,
    RespuestaTest,
    Tema,
    TestRealizado,
)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirigir a la página principal tras el registro
    else:
        form = UserCreationForm()
    return render(request, 'examenes/register.html', {'form': form})


@login_required
def index(request):
    carreras = Carrera.objects.all()
    cursos = Curso.objects.all()
    asignaturas = Asignatura.objects.all()
    temas = Tema.objects.all()
    numero_preguntas_opciones = [1, 5, 15, 20, 30]
    return render(
        request,
        'examenes/index.html',
        {
            'carreras': carreras,
            'cursos': cursos,
            'asignaturas': asignaturas,
            'temas': temas,
            'numero_preguntas_opciones': numero_preguntas_opciones
        }
    )


@login_required
def test(request):
    numero_preguntas = request.GET.get('numero_preguntas') or '1'

    # Asumiendo que el tema se pasa como un parámetro GET
    tema_id = request.GET.get('tema')
    preguntas = list(Pregunta.objects.filter(tema_id=tema_id))
    preguntas_seleccionadas = random.sample(preguntas, min(len(preguntas), int(numero_preguntas)))
    return render(request, 'examenes/test.html', {'preguntas': preguntas_seleccionadas})


@login_required
def submit_test(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    test_realizado, preguntas_y_respuestas = process_test_submission(request.user, request.POST)

    context = {
        'preguntas_y_respuestas': preguntas_y_respuestas,
        'num_acertadas': test_realizado.preguntas_correctas,
        'num_falladas': test_realizado.preguntas_falladas,
        'num_no_contestadas': test_realizado.preguntas_no_contestadas,
        'total_preguntas': test_realizado.total_preguntas,
        'porcentaje_aciertos': (test_realizado.preguntas_correctas / test_realizado.total_preguntas) * 100,
    }
    # Crear y guardar un nuevo TestRealizado
    return render(request, 'examenes/resultado_test.html', context)


@staff_member_required
def preguntas_por_tema(request, tema_id):
    preguntas = Pregunta.objects.filter(tema_id=tema_id)
    return render(request, 'admin/preguntas_por_tema.html', {'preguntas': preguntas})


@login_required
def historico_tests(request):
    """Ordena los tests por fecha, mostrando primero los más recientes."""
    tests_realizados = TestRealizado.objects.filter(usuario=request.user).order_by('-fecha')
    return render(
        request,
        'examenes/historico_tests.html',
        {
            'tests_realizados': tests_realizados
        }
    )


@login_required
def detalle_test(request, test_id):
    user_test = get_object_or_404(TestRealizado, id=test_id)

    # Verificar si el test pertenece al usuario logueado
    if user_test.usuario != request.user:
        user_can_view = False
    else:
        user_can_view = True
    # Suponiendo que tienes una forma de obtener las preguntas y respuestas relacionadas con este test
    # preguntas_y_respuestas = test.obtener_preguntas_y_respuestas()
    detalles, stats = user_test.obtener_detalle_test()

    return render(request, 'examenes/detalle_test.html', {
        'user_can_view': user_can_view,
        'test': user_test,
        # 'preguntas_y_respuestas': preguntas_y_respuestas
        'detalle_test': detalles,
        'stats': stats,
    })


def custom_logout(request):
    logout(request)
    return redirect('thank_you')  # Nombre de la URL de la página de agradecimiento


def thank_you(request):
    return render(request, 'examenes/thank_you.html')
