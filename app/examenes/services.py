# services.py
from .models import OpcionDeRespuesta, Pregunta, RespuestaTest, TestRealizado, UserProfile, AsignaturaUsuario

EXPERIENCIA = 20

def process_test_submission(user, post_data):
    test_realizado = TestRealizado(usuario=user)
    test_realizado.preguntas_correctas = 0
    test_realizado.preguntas_falladas = 0
    test_realizado.preguntas_no_contestadas = 0
    test_realizado.total_preguntas = 0
    test_realizado.save()
    # Initialize counters
    respuestas_correctas = 0
    respuestas_falladas = 0
    respuestas_no_contestadas = 0
    pregunta = None

    preguntas_y_respuestas = []

    for key, value in post_data.items():
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

    if pregunta:
        test_realizado.asignatura = pregunta.tema.asignatura
        test_realizado.tema = pregunta.tema
        test_realizado.preguntas_correctas = respuestas_correctas
        test_realizado.preguntas_falladas = respuestas_falladas
        test_realizado.preguntas_no_contestadas = respuestas_no_contestadas
        test_realizado.total_preguntas = respuestas_correctas + respuestas_falladas + respuestas_no_contestadas
    test_realizado.save()
    return test_realizado, preguntas_y_respuestas


def finalizar_test(request, test_realizado):
    asignatura_usuario = AsignaturaUsuario.objects.get(usuario__user=request.user, asignatura=test_realizado.asignatura)

    # Añadir puntos de experiencia a la asignatura específica
    if not asignatura_usuario.experiencia:
        asignatura_usuario.experiencia = 0
    asignatura_usuario.experiencia += EXPERIENCIA
    asignatura_usuario.save()

    # Añadir puntos a la experiencia total del usuario
    perfil_usuario = UserProfile.objects.get(user=request.user)
    perfil_usuario.experiencia_total += EXPERIENCIA
    perfil_usuario.save()


