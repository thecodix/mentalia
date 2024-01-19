import random

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Pregunta, Asignatura, Tema, TestRealizado, RespuestaTest


def index(request):
    asignaturas = Asignatura.objects.all()
    temas = Tema.objects.all()
    numero_preguntas_opciones = [1, 5, 15, 20, 30]
    return render(request, 'examenes/index.html', {'asignaturas': asignaturas, 'temas': temas, 'numero_preguntas_opciones': numero_preguntas_opciones})


def test(request):
    numero_preguntas = request.GET.get('numero_preguntas')
    # Asumiendo que el tema se pasa como un parámetro GET
    tema_id = request.GET.get('tema')
    preguntas = list(Pregunta.objects.filter(tema_id=tema_id))
    preguntas_seleccionadas = random.sample(preguntas, min(len(preguntas), int(numero_preguntas)))
    return render(request, 'examenes/test.html', {'preguntas': preguntas_seleccionadas})


def submit_test(request):
    if request.method == 'POST':
        test_realizado = TestRealizado()
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
                respuesta_seleccionada = None
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
    else:
        pass # Redirecciona o muestra un error si es necesario


@staff_member_required
def preguntas_por_tema(request, tema_id):
    preguntas = Pregunta.objects.filter(tema_id=tema_id)
    return render(request, 'admin/preguntas_por_tema.html', {'preguntas': preguntas})


def historico_tests(request):
    tests_realizados = TestRealizado.objects.all().order_by('-fecha')  # Ordena por fecha, los más recientes primero
    return render(request, 'examenes/historico_tests.html', {'tests_realizados': tests_realizados})


def detalle_test(request, test_id):
    test = get_object_or_404(TestRealizado, id=test_id)
    # Suponiendo que tienes una forma de obtener las preguntas y respuestas relacionadas con este test
    preguntas_y_respuestas = test.obtener_preguntas_y_respuestas()

    return render(request, 'examenes/detalle_test.html', {
        'test': test,
        'preguntas_y_respuestas': preguntas_y_respuestas
    })