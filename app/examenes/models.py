from django.conf import settings
from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre


class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Tema(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return f"{self.tema.nombre} {self.id} - {self.texto[:30]}"

class OpcionDeRespuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.pregunta.id}) [{self.es_correcta}] - {self.texto[:25]}"


class TestRealizado(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    asignatura = models.ForeignKey('Asignatura', on_delete=models.SET_NULL, null=True)
    tema = models.ForeignKey('Tema', on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    preguntas_correctas = models.IntegerField()
    preguntas_falladas = models.IntegerField()
    preguntas_no_contestadas = models.IntegerField()
    total_preguntas = models.IntegerField()

    def obtener_preguntas_y_respuestas(self):
        return RespuestaTest.objects.filter(test_realizado=self).select_related('pregunta', 'respuesta_seleccionada')

    def obtener_detalle_test(self):
        # Obtener todas las respuestas asociadas a este test
        respuestas_test = self.respuestatest_set.select_related('pregunta', 'respuesta_seleccionada').all()

        detalle_test = []
        for respuesta in respuestas_test:
            pregunta = respuesta.pregunta
            opciones = pregunta.opcionderespuesta_set.all()
            respuesta_correcta = opciones.get(es_correcta=True)

            detalle_test.append({
                'pregunta': pregunta,
                'opciones': opciones,
                'seleccionada': respuesta.respuesta_seleccionada,
                'correcta': respuesta_correcta
            })
        stats = {
            'num_acertadas': self.preguntas_correctas,
            'num_falladas': self.preguntas_falladas,
            'num_no_contestadas': self.preguntas_no_contestadas,
            'total_preguntas': self.total_preguntas,
        }

        return detalle_test, stats

class RespuestaTest(models.Model):
    test_realizado = models.ForeignKey(TestRealizado, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_seleccionada = models.ForeignKey(OpcionDeRespuesta, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ['test_realizado', 'pregunta', 'respuesta_seleccionada']
