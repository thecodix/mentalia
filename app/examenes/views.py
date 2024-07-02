import random

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Asignatura, Carrera, Curso, Pregunta, Tema, TestRealizado, RespuestaTest, AsignaturaUsuario, \
    UserProfile, Seccion, ProgresoUsuario, Subseccion
from .services import process_test_submission, finalizar_test


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


def seleccionar_asignatura(request):
    perfil_usuario, created = UserProfile.objects.get_or_create(user=request.user)
    asignaturas_estudiadas = AsignaturaUsuario.objects.filter(usuario=perfil_usuario).values_list('asignatura', flat=True)
    asignaturas_para_desbloquear = Asignatura.objects.exclude(id__in=asignaturas_estudiadas)
    return render(request, 'examenes/seleccionar_asignatura.html', {'asignaturas': asignaturas_para_desbloquear})


def lista_asignaturas(request):
    estudios = AsignaturaUsuario.objects.filter(usuario__user=request.user)
    return render(request, 'examenes/lista_asignaturas.html', {'estudios': estudios})


def desbloquear_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    perfil_usuario, created = UserProfile.objects.get_or_create(user=request.user)

    ya_estudiando = AsignaturaUsuario.objects.filter(usuario=perfil_usuario, asignatura=asignatura).exists()
    if not ya_estudiando:
        AsignaturaUsuario.objects.create(usuario=perfil_usuario, asignatura=asignatura)
        messages.success(request, f'La asignatura {asignatura.nombre} se añadió con éxito')
    else:
        messages.info(request, f'Ya estás estudiando la asignatura {asignatura.nombre}')

    return redirect('lista_asignaturas')


def roadmap(request, asignatura_id):
    # Asumiendo que tienes un modelo Tema que está relacionado con Asignatura.
    temas = Tema.objects.filter(asignatura_id=asignatura_id).prefetch_related('secciones')
    for tema in temas:
        for seccion in tema.secciones.all():
            # Asumiendo que cada sección ya está relacionada con las subsecciones
            for subseccion in seccion.subseccion_set.all():
                progreso, creado = ProgresoUsuario.objects.get_or_create(
                    usuario=request.user.userprofile,
                    subseccion=subseccion
                )
                subseccion.progreso_usuario = progreso

    return render(request, 'examenes/roadmap.html', {'temas': temas})


def detalle_seccion(request, seccion_id):
    seccion = get_object_or_404(Seccion, id=seccion_id)
    subsecciones = seccion.subseccion_set.prefetch_related(
        'preguntas').all()  # Prefetch las preguntas para optimizar las consultas a la base de datos
    return render(request, 'examenes/detalle_seccion.html', {'seccion': seccion, 'subsecciones': subsecciones})


# Suponiendo que ya tienes una función que genera el contexto del test
def realizar_test_subseccion(request, subseccion_id):
    subseccion = get_object_or_404(Subseccion, id=subseccion_id)
    preguntas = subseccion.preguntas.filter(active=True)  # Asegúrate de que el modelo Pregunta tiene un campo 'active'

    context = {
        'subseccion': subseccion,
        'preguntas': preguntas,
        # Agrega cualquier otro contexto necesario para tu test
    }

    return render(request, 'examenes/test.html', context)


@login_required
def index(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        tipo = request.GET.get('tipo')
        seleccion = request.GET.get('seleccion')

        if tipo == 'carrera':
            cursos = Curso.objects.filter(carrera_id=seleccion).values('id', 'nombre')
            return JsonResponse({'cursos': list(cursos)})
        if tipo == 'curso':
            asignaturas = Asignatura.objects.filter(curso_id=seleccion).values('id', 'nombre')
            return JsonResponse({'asignaturas': list(asignaturas)})
        if tipo == 'asignatura':
            temas = Tema.objects.filter(asignatura_id=seleccion).values('id', 'nombre')
            return JsonResponse({'temas': list(temas)})

    carreras = Carrera.objects.all()
    numero_preguntas_opciones = [1, 5, 15, 20, 30]
    return render(
        request,
        'examenes/index.html',
        {
            'carreras': carreras,
            'numero_preguntas_opciones': numero_preguntas_opciones
        }
    )


@login_required
def get_temas(request):
    asignatura_id = request.GET.get('asignatura_id')
    if asignatura_id:
        temas = Tema.objects.filter(asignatura_id=asignatura_id).values('id', 'nombre')
        return JsonResponse(list(temas), safe=False)
    return JsonResponse([], safe=False)


@login_required
def get_asignaturas(request):
    curso_id = request.GET.get('curso_id')
    if curso_id:
        asignaturas = Asignatura.objects.filter(curso_id=curso_id).values('id', 'nombre')
        return JsonResponse(list(asignaturas), safe=False)
    return JsonResponse([], safe=False)


@login_required
def get_cursos(request):
    carrera_id = request.GET.get('carrera_id')
    if carrera_id:
        cursos = Curso.objects.filter(carrera_id=carrera_id).values('id', 'nombre')
        return JsonResponse(list(cursos), safe=False)
    return JsonResponse([], safe=False)


@login_required
def index2(request):
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

    tema_id = request.GET.get('tema')
    asignatura_id = request.GET.get('asignatura')
    temas_relacionados = Tema.objects.filter(asignatura_id=asignatura_id)

    preguntas = list(Pregunta.objects.filter(tema__in=temas_relacionados, active=True))

    if tema_id != 'todos':
        preguntas = list(Pregunta.objects.filter(tema_id=tema_id, active=True))

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
    finalizar_test(request, test_realizado)

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
    for test in tests_realizados:
        test.porcentaje_correctas = test.preguntas_correctas*100/max(test.total_preguntas, 1)
        test.porcentaje_falladas = test.preguntas_falladas*100/max(test.total_preguntas, 1)
        test.porcentaje_no_contestadas = test.preguntas_no_contestadas*100/max(test.total_preguntas, 1)
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

    temas = Tema.objects.filter(asignatura=user_test.asignatura)
    resultados = []

    for tema in temas:
        total_preguntas = RespuestaTest.objects.filter(test_realizado=user_test, pregunta__tema=tema).count()
        if total_preguntas == 0:
            continue
            #resultados.append({'tema': tema.nombre, 'aciertos': 0, 'fallos': 0, 'total': 0})
        aciertos = RespuestaTest.objects.filter(test_realizado=user_test, pregunta__tema=tema,
                                                respuesta_seleccionada__es_correcta=True).count()
        fallos = RespuestaTest.objects.filter(test_realizado=user_test, pregunta__tema=tema,
                                                respuesta_seleccionada__es_correcta=False).count()
        if not aciertos and not fallos:
            continue
        resultados.append({
            'tema': tema.nombre,
            'aciertos': aciertos*100/total_preguntas if total_preguntas else 0,
            'fallos': fallos*100/total_preguntas if total_preguntas else 0,
            'total': total_preguntas,
        })

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
        'resultados': resultados,
        'stats': stats,
    })


def custom_logout(request):
    logout(request)
    return redirect('thank_you')  # Nombre de la URL de la página de agradecimiento


def thank_you(request):
    return render(request, 'examenes/thank_you.html')
