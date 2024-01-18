from django.contrib import admin

# Register your models here.
from .models import Asignatura, Tema, Pregunta, OpcionDeRespuesta, TestRealizado

# admin.site.register(Asignatura)
# admin.site.register(Tema)
# admin.site.register(Pregunta)
# admin.site.register(OpcionDeRespuesta)
admin.site.register(TestRealizado)


@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'asignatura')


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('abreviar_texto', 'tema', 'id')

    def abreviar_texto(self, obj):
        return obj.texto[:50]  # Muestra los primeros 50 caracteres
    abreviar_texto.short_description = 'Texto de la Pregunta'


@admin.register(OpcionDeRespuesta)
class OpcionDeRespuestaAdmin(admin.ModelAdmin):
    list_display = ('asignatura', 'tema', 'pregunta', 'texto', 'correcta')

    def asignatura(self, obj):
        return obj.pregunta.tema.asignatura.nombre

    def tema(self, obj):
        return obj.pregunta.tema.nombre

    def pregunta(self, obj):
        return f"{obj.pregunta.id}: {obj.pregunta.texto[:15]}"

    def correcta(self, obj):
        return f"{obj.es_correcta}"