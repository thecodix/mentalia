import json
import re

text = """
1. ¿Cuál es el ciclo de un proyecto?
a. Identificación, diseño, ejecución y seguimiento, evaluación (correcta)
b. Identificación, diseño, ejecución y evaluación, seguimiento 
c. Diseño, identificación, ejecución y seguimiento, evaluación

2. El proyecto de animación tiene como estrategias:
a. Ajuste, cambio de situación y devolución
b. Encargo, cambio de situación y devolución. (correcta)
c. Encargo, ajuste, cambio de situación y devolución.

3. El pronóstico puede ser:
a. Favorable o desfavorable
b. Muy favorable o poco favorable
c. Un continuo que va desde muy favorable a desfavorable. (correcta)

4. Cual NO es un objetivo de la evaluación:
a. Mejorar y perfeccionar el proyecto
b. Facilitar el proceso de toma de decisiones
c. Feedback con la población afectada (devolver información) (correcta)

5. La eficacia es:
a. El grado en el cual se alcanzan los objetivos y metas del proyecto en un tiempo determinado, independientemente de los costos que ello implique. (correcta)
b. El grado en el cual se alcanzan los objetivos y metas del proyecto en un tiempo determinado, teniendo en cuenta los costos que ello implique.
c. La relación existente entre los resultados reales y los objetivos planificados. 

6. La efectividad es:
a. La relación existente entre los resultados reales y los objetivos planificados, teniendo en cuenta los costos.
b. El grado en el cual se alcanzan los objetivos y metas del proyecto en un tiempo determinado, teniendo en cuenta los costos que ello implique.
c. La relación existente entre los resultados reales y los objetivos planificados. (correcta)

7. La viabilidad técnica es:
a. Posibilidad de llevar a cabo el proyecto reduciendo al máximo todos sus obstáculos y analizando si los destinatarios están dispuestos a asumir por ellos mismo los objetivos propuestos por el proyecto.
b. Conocer tanto cualitativa como cuantitativamente la idoneidad de los recursos. (correcta)
c. Conocer en que medida el contexto es favorable, indiferente o contrario al proyecto.

8. La evaluabilidad es:
a. Medida en la cual un proyecto puede ser evaluado, lo cual depende en buena parte hasta qué punto ha sido bien diseñado, así como de las posibles barreras que dificulten la evaluación. (correcta)
b. Es una cuestión que siempre responde a la misma pregunta ¿se dan las condiciones necesarias para que los logros del proyecto se mantengan indefinidamente en el futuro? 
c. Ninguna de las anteriores es correcta

9. La evaluación ex post:
a. Se lleva a cabo durante la ejecución del proyecto para detectar cualquier problema que pueda provocar un funcionamiento inadecuado del proyecto.
b. Evalúa la viabilidad del proyecto propuesto.
c. Analiza los resultados obtenidos al finalizar el proyecto. (correcta)

10. Una necesidad sentida puesta en acción mediante una solicitud es:
a. Necesidad expresada (correcta)
b. Necesidad normativa
c. Necesidad experimentada

11. Los enfoques teóricos del diagnóstico son:
a. La teoría de la necesidad y la teoría del riesgo
b. La teoría de la necesidad social, de la afección y del riesgo (correcta)
c. La teoría de la necesidad y la teoría de la carencia

12. Las estrategias de: encargo, ajuste, cambio de situación y devolución se presentan en:
a. Proyecto de sensibilización
b. Proyecto de animación sociocultural (correcta)
c. Proyecto de animación

13. En el diseño teórico de un proyecto de intervención psicosocial, siempre están presente:
a. El encargo y la devolución (correcta)
b. El ajuste y la devolución
c. El ajuste y el cambio de situación

14. Qué tipo de documentación es la que recoge todos los datos que la administración requiere para mantener el “contrato”:
a. Memoria (correcta)
b. Informe científico
c. Informativo o de sensibilización

15. Un pronóstico favorable es cuando:
a. Las personas que sufren la carencia tienen el problema, pero no lo reconocen
b. Las personas que sufren la carencia tienen el problema y lo reconocen (correcta)
c. Ninguna de las anteriores es correcta

16. Los resultados si dan menos de 1, el proyecto es:
a. Muy eficaz 
b. Poco eficaz
c. Ineficaz (correcta)
"""
# Datos iniciales para Asignatura y Tema
data = [
    # Cuarto curso es pk=2
    {
        "model": "examenes.asignatura",
        "pk": 3,
        "fields": {
            "curso": 2,
            "nombre": "Proyectos de Intervención Psicosocial"
        }
    },
    {
        "model": "examenes.tema",
        "pk": 3,
        "fields": {
            "nombre": "Tema 1 - PIPS",
            "asignatura": 3
        }
    }
]

# Split the text into individual questions
questions = re.split(r'\d+\.\s', text)
questions_json = []

# Start the question IDs from 89 as requested
question_pk = 164
response_pk = 468

for question in questions:
    if len(question) < 2:
        continue
    # Extraer la pregunta
    pregunta_regex = re.compile(r"^(.+?)(?=\sa\.\s)")
    pregunta = pregunta_regex.search(question).group(1)

    question_data = {
        "model": "examenes.pregunta",
        "pk": question_pk,
        "fields": {
            "tema": 3,
            "texto": pregunta
        }
    }
    data.append(question_data)

    # Extraer las opciones de respuesta
    opciones_regex = re.compile(r"\b([a-c])\.\s(.*?)(?=\n|$)", re.DOTALL)
    opciones = opciones_regex.findall(question)

    # Determinar cuál es la respuesta correcta
    for letra, opcion in opciones:
        es_correcta = False
        if "(correcta)" in opcion:
            es_correcta = True
            opcion = opcion.replace(" (correcta)", "")  # Limpiar la opción
        #print(f"Opción {letra}: {opcion}")
        response_data = {
            "model": "examenes.opcionderespuesta",
            "pk": response_pk,
            "fields": {
                "pregunta": question_pk,
                "texto": opcion,
                "es_correcta": es_correcta
            }
        }
        data.append(response_data)
        response_pk += 1

    question_pk += 1

# Output the JSON to a file
with open('questions_pips.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
