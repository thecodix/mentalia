from django.contrib import admin

# Register your models here.
from .models import (
    Asignatura,
    Carrera,
    Curso,
    OpcionDeRespuesta,
    Pregunta,
    Tema,
    TestRealizado, AsignaturaUsuario, Seccion, Subseccion, ProgresoUsuario,
)

admin.site.register(TestRealizado)
admin.site.register(Carrera)
admin.site.register(Curso)
admin.site.register(ProgresoUsuario)


@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tema', 'asignatura', 'orden')


@admin.register(Subseccion)
class SubseccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'seccion', 'orden')


# @admin.register(ProgresoUsuario)
# class ProgresoUsuarioAdmin(admin.ModelAdmin):
#     list_display = ('usuario', 'subseccion', 'progreso')


@admin.register(AsignaturaUsuario)
class AsignaturaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('get_user_id', 'get_username', 'asignatura', 'experiencia')
    search_fields = ('usuario__username', 'asignatura__nombre')
    list_filter = ('asignatura',)

    def get_username(self, obj):
        return obj.usuario.user.username
    get_username.short_description = 'Nombre de Usuario'

    def get_user_id(self, obj):
        return obj.usuario.user.id
    get_user_id.short_description = 'ID de Usuario'

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'asignatura', 'id')


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('abreviar_texto',  'tema', 'subseccion', 'id', 'active')
    list_editable = ('active',)

    def abreviar_texto(self, obj):
        return obj.texto[:50]  # Muestra los primeros 50 caracteres
    abreviar_texto.short_description = 'Texto de la Pregunta'


@admin.register(OpcionDeRespuesta)
class OpcionDeRespuestaAdmin(admin.ModelAdmin):
    list_display = ('asignatura', 'tema', 'pregunta', 'id', 'texto', 'correcta')

    def asignatura(self, obj):
        return obj.pregunta.tema.asignatura.nombre

    def tema(self, obj):
        return obj.pregunta.tema.nombre

    def pregunta(self, obj):
        return f"{obj.pregunta.id}: {obj.pregunta.texto[:15]}"

    def correcta(self, obj):
        return f"{obj.es_correcta}"
