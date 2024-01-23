# Generated by Django 5.0.1 on 2024-01-19 00:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testrealizado',
            name='asignatura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='examenes.asignatura'),
        ),
        migrations.AlterField(
            model_name='testrealizado',
            name='tema',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='examenes.tema'),
        ),
        migrations.CreateModel(
            name='RespuestaTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examenes.pregunta')),
                ('respuesta_seleccionada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examenes.opcionderespuesta')),
                ('test_realizado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examenes.testrealizado')),
            ],
            options={
                'unique_together': {('test_realizado', 'pregunta', 'respuesta_seleccionada')},
            },
        ),
    ]