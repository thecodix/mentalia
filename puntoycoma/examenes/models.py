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
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    preguntas_correctas = models.IntegerField()
    preguntas_totales = models.IntegerField()