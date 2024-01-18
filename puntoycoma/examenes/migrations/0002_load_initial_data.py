import json

from django.db import migrations

def cargar_datos(apps, schema_editor):
    with open('datos_examenes_completo.json', 'r') as file:
        data = json.load(file)

    # Obtener los modelos
    Asignatura = apps.get_model('examenes', 'Asignatura')
    Tema = apps.get_model('examenes', 'Tema')
    Pregunta = apps.get_model('examenes', 'Pregunta')
    OpcionDeRespuesta = apps.get_model('examenes', 'OpcionDeRespuesta')

    # Diccionarios para almacenar las instancias creadas
    asignaturas = {}
    temas = {}
    preguntas = {}

    for entry in data:
        if entry['model'] == 'examenes.asignatura':
            asignatura = Asignatura.objects.create(**entry['fields'])
            asignaturas[entry['pk']] = asignatura

        elif entry['model'] == 'examenes.tema':
            fields = entry['fields']
            fields['asignatura'] = asignaturas[fields['asignatura']]
            tema = Tema.objects.create(**fields)
            temas[entry['pk']] = tema

        elif entry['model'] == 'examenes.pregunta':
            fields = entry['fields']
            fields['tema'] = temas[fields['tema']]
            pregunta = Pregunta.objects.create(**fields)
            preguntas[entry['pk']] = pregunta

        elif entry['model'] == 'examenes.opcionderespuesta':
            fields = entry['fields']
            fields['pregunta'] = preguntas[fields['pregunta']]
            OpcionDeRespuesta.objects.create(**fields)

class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_datos),
    ]
