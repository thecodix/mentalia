import random

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render

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

    test_realizado = TestRealizado(usuario=request.user)
    test_realizado.preguntas_correctas = 0
    test_realizado.preguntas_falladas = 0
    test_realizado.preguntas_no_contestadas = 0
    test_realizado.total_preguntas = 0
    test_realizado.save()
    respuestas_correctas = 0
    respuestas_falladas = 0
    respuestas_no_contestadas = 0
    preguntas_y_respuestas = []
    pregunta = None

    for key, value in request.POST.items():
        if key.startswith('pregunta_'):
            pregunta_id = int(key.split('_')[1])
            pregunta = Pregunta.objects.get(id=pregunta_id)
            respuesta_correcta = pregunta.opcionderespuesta_set.get(es_correcta=True)
            respuesta_seleccionada_id = value if value.isdigit() else None
            respuesta_seleccionada = OpcionDeRespuesta.objects.get(
                id=respuesta_seleccionada_id) if respuesta_seleccionada_id else None
            if value == 'no_contestada':
                respuestas_no_contestadas += 1
                preguntas_y_respuestas.append({
                    'pregunta': pregunta,
                    'seleccionada': None,
                    'correcta': respuesta_correcta
                })
            else:
                respuesta_seleccionada = pregunta.opcionderespuesta_set.get(id=int(value))

                if respuesta_seleccionada == respuesta_correcta:
                    respuestas_correctas += 1
                else:
                    respuestas_falladas += 1

                preguntas_y_respuestas.append({
                    'pregunta': pregunta,
                    'seleccionada': respuesta_seleccionada,
                    'correcta': respuesta_correcta
                })

            RespuestaTest.objects.create(
                test_realizado=test_realizado,
                pregunta=pregunta,
                respuesta_seleccionada=respuesta_seleccionada
            )

    total_preguntas = respuestas_correctas + respuestas_falladas + respuestas_no_contestadas

    context = {
        'preguntas_y_respuestas': preguntas_y_respuestas,
        'num_acertadas': respuestas_correctas,
        'num_falladas': respuestas_falladas,
        'num_no_contestadas': respuestas_no_contestadas,
        'total_preguntas': total_preguntas,
        'porcentaje_aciertos': (respuestas_correctas / total_preguntas) * 100,
    }
    # Crear y guardar un nuevo TestRealizado
    if pregunta:
        test_realizado.asignatura = pregunta.tema.asignatura
        test_realizado.tema = pregunta.tema
        test_realizado.preguntas_correctas = respuestas_correctas
        test_realizado.preguntas_falladas = respuestas_falladas
        test_realizado.preguntas_no_contestadas = respuestas_no_contestadas
        test_realizado.total_preguntas = total_preguntas
        test_realizado.save()

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
