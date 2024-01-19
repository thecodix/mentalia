from django.db import models

# Create your models here.
class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)

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
    preguntas_correctas = models.IntegerField()
    preguntas_falladas = models.IntegerField()
    preguntas_no_contestadas = models.IntegerField()
    total_preguntas = models.IntegerField()

    def obtener_preguntas_y_respuestas(self):
        return RespuestaTest.objects.filter(test_realizado=self).select_related('pregunta', 'respuesta_seleccionada')


class RespuestaTest(models.Model):
    test_realizado = models.ForeignKey(TestRealizado, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_seleccionada = models.ForeignKey(OpcionDeRespuesta, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['test_realizado', 'pregunta', 'respuesta_seleccionada']
