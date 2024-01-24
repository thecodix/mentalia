import json
import re

text = """
1. El desarrollo madurativo de la atención y la concentración necesario para facilitar el
proceso de aprendizaje y favorecer la activación de los bloques funcionales siguientes
(Luria 1973, 1980) tienes sus estructuras cerebrales en el córtex prefrontal. Falso,
córtex frontal
2. La neurogénesis hace referencia al moldeamiento de las dendritas para establecer
conexiones con otras neuronas. Falso, eso es la maduración cerebral, la neurogénesis
es la formación de las neuronas y del cerebro.
3. El eje y plano horizontal está relacionado con la bipedestación, mientras que el eje y
plano vertical medio se relaciona con la etapa de suelo. Falso, es al revés
4. Entre los programas de desarrollo de habilidades visuales de tres a seis años, se
proponen un conjunto de ejercicios y de juegos que favorecen el desarrollo
neurofuncional que tiene relación directa con las habilidades de aprender idiomas.
Falso, es programa de desarrollo auditivo
5. En la clase social deprivada, las familias están orientadas hacia el futuro y es más
habitual el castigo como medida de disciplina. Por el contrario, en las clases media y
alta existe una mayor preferencia por el presente y la disciplina está basada en
premios y castigos simbólicos. Falso, es al revés
6. El disfrute, frecuencia e intencionalidad de las conductas disruptivas son factores que
determinan la existencia de un trastorno clínico. Falso, es la edad no el disfrute
7. La clasificación de los trastornos del neurodesarrollo del DSM-V recoge el
diagnóstico del trastorno de asperger, el síndrome de Rett y el trastorno del espectro
autista. Falsa, el síndrome de Rett no sale.
8. Según la definición de las DDAA dada por Santiuste y González-Pérez (2005), se
hace una doble referencia curricular: primero a las disciplinas curriculares y después
al resto de áreas instrumentales. Falso, primariamente en el ámbito de las disciplinas
instrumentales básicas (lectura, matemáticas, escritura) y secundariamente en diversas
áreas curriculares (ciencias experimentales, sociales, segundo idioma…)
9. El síndrome psicopático se caracteriza por desinhibición conductual, producido por
una lesión en el córtex orbitofrontal. Verdadera
10. La activación duolateral simétrica, el control del núcleo medular alto y la activación
de los canales de relación con el exterior son característicos de la etapa
neonato-homolateral alterna. Verdadera
11. Las dificultades del aprendizaje están constituidas por un conjunto heterogéneo de
problemas cuyo origen es, probablemente, una disfunción del sistema nervioso
central. Verdadera
12. En la discalculia ideognóstica se observa una dificultad para hacer operaciones
mentales, principalmente. Verdadera
13. La discalculia lexical se caracteriza por la dificultad para leer símbolos matemáticos,
principalmente. Verdadera
14. Santiuste y González-Pérez (2005) indican que las pruebas pedagógicas estarían en el
tipo de evaluación formal de las DAM, ya que son similares a las de cualquier
profesor, pero están estandarizadas y cuentan con baremos poblacionales. Verdadera
15. Dado que una conducta determinada puede estar sustentada por múltiples sistemas
funcionales (equipotencialidad) los efectos de una misma lesión cerebral pueden ser
más devastadores en un niño que en un adulto. Verdadera
16. Existe mayor probabilidad de heredar la inteligencia de la madre, ya que muchas
capacidades cognitivas se ubican en el cromosoma X. Verdadera
17. El tendido supino es un signo característico de la contralateralidad. Falsa, de la
homogeneidad
18. En los trastornos del desarrollo, suponen problemas psicopatológicos las dificultades
de aprendizaje de la lectura, la escritura y las matemáticas. Falsa, eso son problemas
académicos, psicopatológicos son la ansiedad, la depresión o de conducta.
19. En términos psicolingüísticos la dislexia evolutiva se relaciona con una lesión que
afecta a determinados componentes del lenguaje, en función de la corteza cerebral
afectada.
20. A Helena le diagnosticaron dislexia fonológica a los 6 años, presentando problemas
principalmente de lectura de palabras irregulares y sujetas a reglas. Falsa,
21. La diferencia fundamental entre DDAA y trastornos del desarrollo es que este se
relaciona con una alteración o discapacidad en el plano biológico, mientras en las
DDAA se da en el plano orgánico. Falsa, es al revés.
22. Estudios con resonancia magnética funcional confirman dos circuitos distintos
implicados en la lectura: el ventral (fascículo fronto-occipital inferior) o giro
fusiforme, para la lectura de palabras conocidas y el superior (fascículo arqueado) o
giro angular, implicado en la lectura de palabras nuevas. Verdadera
23. El reconocimiento de la palabra constituye uno de los principales déficits de la
dislexia, implicando alteraciones en el acceso al procesamiento perceptivo. ????
24. Rivas y Fernández (2011) conceptualizan la dislexia como un trastorno del lenguaje
que se manifiesta con dificultad respecto al aprendizaje de la lectura y sus usos
generales, como, por ejemplo, en la escritura.
25. Cometer más errores en las palabras funcionales que en las de contenido es
característico de la dislexia léxica. Falsa
26. En el tipo de dislexia con dificultades en la ruta léxica, los errores de regularización
suponen lectura lenta, titubeo y tanteo de pronunciar la palabra esperando acertar.
Verdadera
27. Las conductas de desobediencia generan situaciones de conflicto en el aula, son
tendientes a desaparecer por sí mismas con la edad y, solo cuando llegan a ser muy
graves, reciben la denominación de trastorno negativista desafiante. Verdadera
28. Los errores derivacionales son característicos de la dislexia superficial. Falsa, de la
dislexia fonológica
29. El método analítico para el entrenamiento de la lectoescritura tiene como principal
crítica que retrasan la adquisición de los automatismos implícitos en los niveles
elementales. Verdadera
30. El concepto de pluripotencialidad supone que cuando un área resulta dañada, pueden
verse alteradas varias conductas, en dependencia de cuantos sean los sistemas de los
que el área en cuestión forma parte. Verdadera
31. La dificultad para extraer el significado de las palabras homófonas es característico de
la dislexia.
32. La técnica de lectura conjunta o en sombra, supone un ejemplo de intervención para la
dislexia del enfoque funcional de la psicología cognitiva, considerando el
procesamiento fonológico como su principal déficit.
33. Los métodos alfabéticos, fónicos y silábicos se engloban dentro de los métodos
sintéticos para el entrenamiento de la lectoescritura.
34. Las DDAA se manifiestan primariamente con problemas en el ámbito lingüístico y
con trastornos conductuales como principales factores afectados. Falsa, con defectos
de procesamiento en los principales factores cognitivos
35. El método sintético para el tratamiento de la lectoescritura se propone especialmente
para el aprendizaje de idiomas transparentes como el castellano. Verdadera
36. En el trastorno lectoescritor, según el modelo psicolingüístico, si las dificultades son
auditivas, la intervención sería utilizando el método sintético que minimizaría la
rotulación verbal de letras y palabras enteras. Falsa, analítica.
37. En el enfoque neuropsicológico de Bakker, para la intervención psicoeducativa de la
dislexia en el aula, propone que, en los casos que denomina dislexia P (perceptivos),
debe basarse en la estimulación del hemisferio cerebral izquierdo, por ejemplo,
presentando letras tridimensionales para que las palpen con la mano derecha.
Verdadera
38. La realización de dictados en clase es una técnica habitual y aconsejable para la
intervención y enseñanza de la ortografía. Falsa, no es aconsejable.
39. La dislexia visual se caracteriza por problemas en la identificación de las
características posicionales de las letras. Verdadera
40. Según el modelo de Seymour y MacGregor (1984), los procesadores semántico y
fonológico tienen lugar en el momento previo a la adquisición lectora, mientras que el
grafémico y el ortográfico tienen lugar durante la adquisición de la lectura. Verdadera
41. La lectura de palabras de alta y baja frecuencia igualadas en número es especialmente
relevante para la evaluación de la ruta léxica o visual. Falsa, no es relevante.
42. En el procedimiento de lecturas repetidas para el desarrollo de la fluidez lectora, tras
la primera lectura en voz alta del niño, se propone un objetivo de tiempo y exactitud a
alcanzar. La retroalimentación del tiempo y errores se da siempre tras cada intento y
hasta que se haya conseguido el objetivo. Falsa, evitar la corrección sistemática de los
errores.
43. En los métodos analíticos, el flujo de información discurre de arriba-abajo, facilitando
el dominio de las partes elementales antes que del conjunto. Falsa, parte de las
unidades globales del idioma para llegar al reconocimiento de los componentes
simples que las integran.
44. Solicitar al niño exagerar la pronunciación de un determinado sonido es una técnica
utilizada para corregir errores de rotación. Falsa, no es para rotación
45. La dislexia tiene una base biológica y genética, mientras que la disortografía supone
una dificultad de carácter evolutivo asociada, en muchos casos, al propio ritmo de
maduración y aprendizaje del niño. Verdadera
46. La escritura al dictado se relaciona con el área 37 de Brodmann. Verdadera
47. La disgrafía se refiere a un conjunto de errores de la escritura que afectan a la palabra
y no a su trazado o grafía. Falsa, afectan al trazado.
48. Según el DSM V (APA, 2013), algunas subhabilidades del trastorno específico del
aprendizaje que pueden estar alteradas en la escritura son: dificultades en las reglas de
puntuación, en la claridad y en la asociación de ideas. Falsa, asociación de ideas no.
49. Según Rivas y Fernández (2011), la sustitución de fonemas vocálicos y/o
consonánticos afines por el X y/o modo de articulación, como “sebtimo” por
“séptimo”, sería una característica de la disortografía relacionada con el contenido.
Falsa, lingüístico-perceptivos.
50. La alteración de la secuenciación fonemática del discurso, generando errores de
omisión-separación es característico de la disortografía dinámica. Falsa, disortografía
cinética.
51. El modelado sin modelos en vivo de tipo encubierto consiste en imaginar escenas
ansiógenas y, a continuación, representar mentalmente a un modelo poderoso para el
niño que lleva a cabo la conducta temida. Verdadera
52. Los ficheros cacográficos son un inventario de errores cometidos frecuentemente por
el alumno en el que al lado se pone la palabra correcta. Falsa, eso son los listados
cacográficos.
53. Dibujar en una cuadrícula la mitad que falta de un dibujo, supone una estrategia de
grafomotricidad-simetría incluida en las pautas de intervención psicoeducativa en el
aula para la disortografía. Falsa, para la disgrafía.
54. En matemáticas, las tareas de la memoria de trabajo como el mantenimiento de
resultados intermedios, la planificación, la ordenación temporal de componentes de
las tareas, la comprobación de resultados y la corrección de errores tienen su mayor
responsable cortical en el lóbulo frontal dorsolateral. Verdadera
55. El procesamiento de los números arábigos se realiza en ambos hemisferios de la
corteza occipito-temporal, mientras que los números verbales se procesan en el
hemisferio izquierdo. Verdadera
56. El déficit de las conexiones neuronales asociadas a la discalculia se encuentra
principalmente en el lóbulo occipital y sus conexiones funcionales con la corteza
prefrontal. Falsa, lóbulo parietal
57. Según Dehaene et al. (1999), la información numérica procesada por el sistema
cuantitativo no verbal está asociada al segmento horizontal del surco intraparietal
(HIPS), que se activa más cuando se realiza una estimación aproximada que cuando
se realiza un cálculo exacto. Verdadera
58. En las conclusiones de la serie de experimentos con bebés de cinco meses de Wynn
(1992) se sugiere que, al mirar más tiempo cuando aparecían los juguetes con un
resultado lógico, los bebés muestran poseer una capacidad innata para el
procesamiento numérico. Falsa, no lógico.
59. El aprendizaje de las matemáticas en las distintas etapas escolares (infantil, primaria y
secundaria) es interdependiente y jerárquico. Verdadera
60. Poner el énfasis en las actitudes e interés del alumno y en la dificultad propia de la
asignatura, supone una hipótesis etiológica evolutiva de las DAM. Falsa, educativa.
61. Al tener conexiones con el sistema límbico, las estructuras frontales también
intervienen en la regulación de la respuesta emocional, la motivación y la conducta
social. Verdadera
62. En caso de lesión en alguna de las áreas relacionadas con el segundo bloque funcional
propuesto por Luria, se observaría un fallo general de la entrada de información,
conduciendo a una alteración de los procesos de atención, vigilia y memoria. Falsa,
eso es el 1er bloque.
63. En el DSM V (APA, 2013) se hace una clara diferenciación entre la disgrafía y la
disortografía. Falsa, no las diferencia.
64. Colocar el mismo número de piezas en posiciones diferentes y preguntar al alumno en
qué dibujo hay más o menos elementos es una tarea para el entrenamiento de las
seriaciones. Falsa, tarea para la noción de conservación.
65. Respecto al bullying, investigaciones internacionales sugieren que los ataques se
producen en mayor medida en el desplazamiento a la escuela que en la propia escuela.
Falsa, los del centro son los más.
66. La posición sociométrica o estatus social se utiliza para evaluar la deprivación
sociocultural. Falsa, para evaluar el bullying.
67. El escaso conocimiento de los propios sentimientos facilita el diagnóstico de la
ansiedad por separación. Falsa, lo dificulta.
68. Relacionado con los déficits socioafectivos, los resultados han mostrado que los
sujetos expuestos al estrés durante la niñez y la adolescencia tenían menores
concentraciones de neurotransmisores en el hipocampo. Verdadera
69. El programa de Kendall para la intervención de la fobia escolar entrena al niño para
reconocer las respuestas físicas que se desencadenan ante sus emociones negativas y
para que reconozca las autoverbalizaciones asociadas a sentimientos negativos con el
consiguiente desarrollo de habilidades de solución de problemas para modificar esas
autoverbalizaciones. En una segunda fase, se ponen en práctica dichas habilidades
mediante una exposición gradual a situaciones ansiógenas, tanto imaginariamente
como en vivo. Verdadera
70. La dificultad para separar las secuencias gráficas pertenecientes a cada secuencia
gráfica mediante los espacios en blanco correspondientes son errores visoespaciales.
Falsa, son errores relacionados con el contenido.
71. La prueba PEREL (Maldonado et al, 1992) para evaluación del retraso en la lectura,
es aplicable a niños de 5 a 8 años. Falsa, de 7 a 9 años.
72. Entre las pruebas formales para la evaluación de la disortografía, la Prueba de
Escritura de Terrasa (1997) tiene aplicación también para niños de primer ciclo de
educación primaria. Verdadera
73. El giro angular izquierdo interviene principalmente en la estimación de resultados
aproximados. Falsa, es el surco intraparietal derecho.
74. Según el modelo neuropsicológico de la dislexia, la participación de las áreas
corticales de los lóbulos frontales y el plano temporal son clave para la correcta
percepción y funcionamiento cognitivo. Verdadera
75. Para realizar los procesos visuales, auditivos y táctiles, esenciales en la aplicación
de metodologías de aprendizaje de nuevos conocimientos basadas en la
sensorialidad, participan los lóbulos occipital, temporal y parietal, del bloque tercero
propuesto por Luria (1973, 1980) Falsa, bloque dos de Luria.
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
