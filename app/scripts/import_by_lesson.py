import json
import re

text = """
TEMA EIDDA 1		
Tener un coeficiente intelectual normal-alto es una característica de la dificultad del aprendizaje. VERDADERO
 						
El volteo del suelo es un signo característico de la contralateralidad. FALSO (Homolateralidad).
 						
Cada contacto corporal, cada movimiento y cada emoción se convierten en una actividad eléctrica, pero no química, que propicia el avance del impulso genético modificando la configuración del cerebro. FALSO (también química).
 						
 						

						
TEMA EIDDA 2
								
La ruta léxica sigue el circuito ventral, donde interviene el giro fusiforme para la lectura de palabras conocidas. VERDADERO
 						
La exploración psicolingüística identifica a los niños que hacen un uso mayoritario de la ruta léxica cuando solo son capaces de leer palabras conocidas, por lo que sería una dislexia fonológica. VERDADERO

"""
# Datos iniciales para Curso y Tema
data = [
    {
        "model": "examenes.curso",
        "pk": 2,
        "fields": {
            "nombre": "Cuarto",
            "carrera": 1
        }
    },
    {
        "model": "examenes.asignatura",
        "pk": 2,
        "fields": {
            "curso": 2,
            "nombre": "Evaluación e intervención en las dificultades"
        }
    },
    {
        "model": "examenes.tema",
        "pk": 2,
        "fields": {
            "nombre": "Tema 1 - EID",
            "asignatura": 2
        }
    }
]

# Split the text into individual questions
questions = re.split(r'\d+\.\s', text)
questions_json = []

# Start the question IDs from 89 as requested
question_pk = 89
response_pk = 318

for question in questions:
    texto = question.replace('\n', ' ')
    if len(texto) < 2:
        continue
    texto = texto[:texto.find('Verdader')]
    texto = texto[:texto.find('Fals')]
    question_data = {
        "model": "examenes.pregunta",
        "pk": question_pk,
        "fields": {
            "tema": 2,  # ID del tema al que pertenecen las preguntas
            "texto": texto
        }
    }
    data.append(question_data)

    for option_text in ("Verdader", "Fals"):
        response_data = {
            "model": "examenes.opcionderespuesta",
            "pk": response_pk,
            "fields": {
                "pregunta": question_pk,
                "texto": f'{option_text}o',
                "es_correcta": option_text in question
            }
        }
        data.append(response_data)
        response_pk += 1

    question_pk += 1

# Output the JSON to a file
with open('questions_eidda.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
