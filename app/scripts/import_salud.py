import json
import re

text = """
1. La psicología de la salud se realiza a través de una proceso multidisciplinar (Verdadero)
2. Las creencias personales no influyen directamente sobre la psicología de la salud (Falso)
3. La psicología de la salud tiene 3 áreas o dimensiones que se destacan: la salud, la enfermedad y los
cuidados de la salud (Verdadero)
4. No es necesario que los Psicólogos sanitarios tengan conocimientos médicos (Falso)
5. Según Matarazzo -1982-, la Psicología de la Salud pretende mantener y mejorar la salud, promover
actuaciones como el ejercicio físico (Verdadero)
6. Se recomienda el tratamiento llevado a cabo por un único terapeuta (Falso)
7. La medicina psicosomática propone que la conjunción cuerpo y mente origina las enfermedades
psicofísiologicas.(Verdadero)
8. No es tarea de la psicología de la salud mejorar la atención médica y las políticas de salud. (Falso)
9. El contexto y el ambiente son importantes en la conducta y en el organismo. (Verdadero)
10. Algunas actitudes disfuncionales que están relacionadas con el ámbito de la salud, prediciendo
enfermedades son: depender de lo que puedan decir los demás, ser incapaz de afrontar la soledad, ser
excesivamente perfeccionista, el egoísmo, los pensamientos distorsionados de todo o nada. (Verdadero)
11. Uno de los objetivos de la psicología de la salud es mantener y mejorar la salud (Verdadero)
12. La psicología de la salud no abarca un plano Holístico o integral (Falso). Sí lo abarca
13. La psicología de la salud se centra en los contextos (Falso). Se centra en los procesos mentales y en el
comportamiento.
14. En la observación los datos son analizados psicométricamente. (Verdadero)
15. La psicología médica pertenece al ámbito mecanicista, por lo que se centra más en los síntomas. (Verdadero)
16. El término “comorbilidad” hace referencia a la presencia de una sola condición crónica. (Falso)
17. Para detectar el origen de la situación de problema en terapia es conveniente trabajar en equipo más que
individual. (Verdadero)
18. La psicología médica es una ciencia mecanicista pero no se centra en los síntomas individuales de la
persona, sino en el problema general. (Falso)
19. Desde lo descriptivo se puede acceder a un plano causal o explicativo. (Verdadero)
20. La comorbilidad es una enfermedad (Falso) es una situación.
21. Uno de los objetivos de la psicologia de la salud es concienciar sobre los factores de riesgo que nos hacen
mas vulnerables a las enfermedades: (Verdadero)
22. La medicina psicosomatica se basa en la etiologia estrictamente fisica de las enfermedades:(Falso) (fisico y
mental)
23. La psicología es una ciencia que se basa plenamente en la observación:(Falso)
24. La psicologia de la salud emprende un camino interdisciplinar, interviene no solo la psicología, sino
también otras ciencias (sociales,médicas, educativas) implicadas en el proceso de cambio de la persona:
(Verdadero)
25. La observación tiene que estar avalada por una prueba fisica: (Verdadero)
26. La psicologia de la salud es una disciplina mecanicista muy centrada en los sintomas:(Falso)
27. El trabajo individual dificulta la tarea del psicologo de la salud (Verdadero).
28. Existen tres dimensiones en la psicología de la salud: la salud, la enfermedad y el afrontamiento de la
enfermedad.(Falso). (Y el Cuidado de la salud)
29. En Psicología de la Salud se puede considerar más fácil el trabajo en equipo. (Verdadero)
30. Uno de los comportamientos compartidos entre humanos y otros animales es el pensamiento.(Falso) (solo es
de humanos)
31. Los datos obtenidos en la observación posteriormente son analizados psicométricamente. (Verdadero)
32. La psicología de la salud es importante en dos dimensiones: en la salud y en los cuidados de la salud.(Falso)
(tres dimensiones, falta en la enfermedad)
33. La psicología de la salud pertenece a la psicología y se origina de diversos ámbitos y disciplinas como la
educación. (Verdadero)
34. La psicología médica emplea un ámbito holístico centrado en los síntomas subyacentes y en curar una
enfermedad.(Falso) (ámbito mecanicista)
35. La observación suele acompañarse de otros métodos como las pruebas biomédicas. (Verdadero)
36. En los primeros contactos con el paciente el terapeuta primero crea una hipótesis sobre las conductas
problema y después realiza una entrevista.(Falso) ( al revés)
37. La psicología de la salud se ayuda de otras ciencias para generar en el paciente el cambio necesario. (Verdadero)
38. Los psicólogos nunca deben usar pruebas bioquímicas o psicofisiológicas.(Falso)
39. Trabajar con un equipo a la hora de realizar el diagnóstico de un problema puede entorpecer la delimitación del problema.(Falso)
40. La medicina conductual trata de prevenir aquellas enfermedades y disfunciones corporales relacionadas con la mente. (Verdadero)
41. Trabajando de manera individual se delimita de mejor forma el problema del paciente que trabajando en equipo.(Falso)
42. La psicología de la salud recoge información sobre diversas disciplinas, como la medicina,la educación, la sociología. (Verdadero)
43. En la psicología de la salud se conocen con exactitud los factores de riesgo del desarrollo del ser humano. (Falso)
44. La medicina psicosomática despertó en los años 1930. (Verdadero)
45. La salud psicológica no se circunscribe solo a la ausencia de enfermedad, sino también a tener una
mentalidad positiva, abierta al cambio y un equilibrio en el bienestar. (Verdadero)
46. La psicología de la salud solo tiene importancia en una única dimensión: en la salud. (Falso) (en la salud, en
la enfermedad y en los cuidados de la salud)
47. Matarazzo -1982- establece cuatro objetivos básicos en psicología de la salud: mantener y mejorar la
salud mediante la promoción de comportamientos saludables, prevenir la enfermedad mediante la reducción de conductas de riesgo para la salud, mejorar la atención médica y las políticas de salud y tomar conciencia de los factores etiológicos de los problemas de salud: (Verdadero)
48. Un aspecto importante en la psicología de la salud es la humanización e individualización del trato con el paciente: (Verdadero)
49. La psicología de la salud sigue un camino interdisciplinar. (Verdadero)
50. En el caso en que los padres no estén juntos es posible evaluar al niño con el consentimiento de solo uno de ellos.(Falso)
51. La psicología de la salud no es una ciencia interdisciplinar en la que puedan intervenir otras esferas.(Falso)
52. La psicología de la salud es una esfera holística e integral mientras que la psicología médica es
mecanicista y centrada en los síntomas. (Verdadero)
53. La psicología de la salud pretende mantener y mejorar la salud, promover actuaciones como el ejercicio
físico y prevenir enfermedades enfatizando del mismo modo en la eficacia de sus tratamientos. (Verdadero)
54. La psicología de la salud obtiene resultados en base únicamente a observaciones que no tienen por qué
ser empíricas.(Falso)
55. La psicología de la salud puede abarcar procesos comportamentales como la conducta social, la conducta
de salud y el control de impulsos. (Verdadero)
56. La psicología es una ciencia que únicamente se basa en la observación, sin hacer alusión a análisis
estadísticos o psicométricos. (Falso)
57. Es difícil definir la conducta problema del paciente, y para ello se utilizan entrevistas y cuestionarios
basados en valoraciones psicométricas como personalidad, inteligencia o fenómenos conductuales. (Verdadero)
58. Para hacer una metodología empírica se parte de una observación empírica, de profesionales y que esté
avalada con alguna prueba física (Verdadero)
59. Los datos de una investigación son analizados psicométricamente, dejándolos a la improvisación y al
punto de vista del profesional. (Falso)
60. La definición de un problema se puede definir más fácilmente en solitario que con un equipo. (Falso)
61. La salud es la ausencia de enfermedad. (Falso)
62. Para mejorar en la psicología de la salud, y en la propia salud, es necesario tomar consciencia de los
aspectos etiológicos. (Verdadero)
63. La enfermedad de Crohn o el asma son claros ejemplos de enfermedades fisiológicas. (Falso)
64. El conductismo, otorgó a la psicología de la salud una perspectiva más interdisciplinar. (Verdadero)
65. Una vez establecida nuestra hipótesis, se recabará una información más profunda sin necesidad de un
consentimiento previo del paciente. (Falso)
66. Un ámbito importante donde se destaca la relación de la psicología con la salud sería nuestras propias
creencias. (Verdadero)
67. La psicología de la salud se interesa en acceder al plano explicativo de los fenómenos que se han
observado y analizado. (Verdadero)
68. La psicología quiere llegar a hacer un análisis estadístico, psicométrico y sistemático de datos que se
extraen de problemas que no siempre nos preocupan. (Falso) (problemas que sí preocupan).
69. Para la observación no solo es necesario tener buen ojo clínico (subjetivo),sino, también, tener pruebas
físicas (objetivo). (Verdadero)
70. La psicología con la salud están conectadas por las propias creencias. (Verdadero)
71. Tratar enfermedades es uno de los objetivos que persigue la Psicología de la Salud. (Falso), prevenir
enfermedades.
72. La dependencia emocional es considerado un factor de predicción de factores. (Verdadero).
73. La comorbilidad es una situación en la que prevalece más de una condición crónica en el individuo.
(Verdadero).
74. La psicología de la salud emprende un camino en conjunto icon otros profesionales, es un camino
multidisciplinar porque intervienen la psicología, ciencias médicas, sociales y educativas implicadas en
el proceso de cambio de la persona. (Verdadero).
75. La importancia de la psicología de la salud está dividida en dos dimensiones: salud y enfermedad. (Falso),
está dividida en tres dimensiones: salud, enfermedad y cuidados de la salud.
76. La psicología de la salud solo pertenece a la psicología, le quita importancia al organismo. (Falso) (No
pertenece únicamente al ámbito de la psicología, tampoco le quita importancia al organismo).
77. La psicología médica emplea un ámbito más holístico e integral. (Falso) (Es la psicología de la salud).
78. Actualmente está en duda la importancia del trato profesional a los pacientes o de tratar a los usuarios
con sumo cariño. (Verdadero)
79. El trabajo en solitario es beneficioso para identificar los problemas (Falso) (En equipo).
80. Los psicólogos de la salud necesitan tener conocimientos médicos de los órganos implicados en las
circunstancias de salud. (Verdadero)
81. La psicología es una ciencia que se ocupa sólamente del comportamiento humano. (Falso)
82. En psicología de la salud también se pueden tener en cuenta para contrastar información pruebas
bioquímicas o psicofisiológicas. (Verdadero)
83. Los psicólogos suelen utilizar pruebas bioquímicas o psicofisiológicas para complementar el registro de
los usuarios. (Verdadero)
84. En la dimensión de cuidados de la salud, la Psicología de la salud no tiene importancia. (Falso)
85. La psicología de la salud trabaja en un ámbito mecanicista, centrándose en curar una enfermedad. (Falso)
86. Prevenir enfermedades con tratamientos cada vez más avanzados no es objetivo de la Psicología de la
Salud. (Falso)
87. La ansiedad, el insomnio, la depresión o el aislamiento social, no son temas de los que se tenga que
encargar la psicología de la salud. (Falso)
88. La psicología abarca los siguientes procesos comportamentales: control de impulsos, conducta social y
conducta de salud. (Verdadero)
89. La medicina conductual trata de prevenir las enfermedades relacionadas con la mente. (Verdadero)
90. Las enfermedades psicofisiológicas se refieren a las disfunciones exclusivamente orgánicas. (Falso)
91. La psicología es una ciencia que se basa en la observación plenamente. (Falso) (es una ciencia empírica).
92. La psicología de la salud emplea un ámbito más integral sin quitarle importancia al organismo. (Verdadero)
93. Lapsicologíadelasaludconstadetresdimensioneslascualesserefierenalasalud,laenfermedadylos
cuidados de la salud. (Verdadero)
94. La psicología de la salud es una disciplina que se apoya en un ámbito mecanicista, centrado en síntomas
subyacentes y en sanar las enfermedades. (Falso) (Es psicología médica).
95. La psicología de la salud es originada por varias disciplinas (Verdadero)
96. Para fomentar el proceso de cambio en el paciente, es necesario trabajar de manera solitaria para
comprender y profundizar con mayor nivel en su problema (Falso)
97. Uno de los campos en psicología donde pueden existir mayor numero de limitaciones es en el
Pensamiento (Verdadero).
98. Mararazzo -1982- marcó algunos objetivos de la psicología de la salud como mantener y mejorar la salud,
promover actuaciones, prevenir la enfermedad con tratamientos especializados y la toma de conciencia
de los aspectos etiológicos de los problemas. (Verdadero)
99. Los psicólogos utilizamos pruebas bioquímicas o psicofisiologicas (Verdadero)
100. La psicología de la salud no se basa en valoraciones psicométricas (Falso) si se basa.
101. Uno de los supuestos desde los que parte la psicología de la salud es que la salud y la enfermedad son
únicamente cuestiones biológicas o médicas. (Falso)
102. La salud se define por el grado de cumplimiento de tres tipos de criterios: socioculturales, objetivos y
subjetivos. (Verdadero)
103. El principal valor de las medidas bioquímicas es su objetividad (Verdadero)
104. Las medidas fisiológicas juegan un papel importante únicamente en el diagnóstico. (Falso)
105. La entrevista es el instrumento más versátil para obtener información individual (Verdadero)
106. El formato de la entrevista tiene que ser estrictamente estructurado (Falso)
107. En las medidas psicofisiológicas su valor clave es el de objetividad (Verdadero)
108. La observación directa es la técnica de evaluación preferida en psicología de la salud y suele ser de dos
tipos: en contextos hospitalarios y ambulatorios. (Verdadero)
109. En la fase de auto-registro, el evaluador es el que realiza la toma de datos pertinente. (Falso)
110. Algunas de las medidas fisiológicas son respuestas del sistema somático, del SNA y del SNC. (Verdadero) 
111. Las Creencias de la propia persona acerca de su Estado de salud, es una de los aspectos que tiene que
tener en cuenta un Psicólogo/a de la Salud. (Verdadero)
112. En la Psicología de la Salud, destacamos tres dimensiones: la salud, la enfermedad y cuidados de la salud. (Verdadero)
113. El pensamiento se considera uno de nuestros comportamientos humanos. (Verdadero)
114. La Psicología de la Salud pretende promover actuaciones como el ejercicio físico. (Verdadero)
115. Algunos factores que pueden estar prediciendo enfermedades podrían ser la idea de dependencia hacia
los demás. (Verdadero)
116. La actividad física pobre, el tabaco, el abuso del alcohol y una mala alimentación condicionan una esfera
de estrés crónico. (Verdadero)
117. El trabajo individual hace nuestra tarea como Psicólogos de la Salud más fácil, en comparación con el
trabajo ‘en equipo’. (Falso)
118. La psicología es una ciencia que se basa únicamente en la observación. (Falso)
119. Dentro de la psicología de la salud solo se aprecia la figura del psicólogo. (Falso) (interdisciplinar, otras
profesiones dentro de la ciencia)
120. La Psicología de la Salud se caracteriza por su trabajo en solitario. (Falso)
121. La Psicología positiva es una disciplina centrada en hallar los síntomas subyacentes de cara a sanar una
enfermedad. (Falso)
122. Según Matarazzo, la psicología de la salud tiene como único objetivo la evaluación y el diagnóstico de
la salud y enfermedad. (Falso)
123. La psicología de la salud trata de explicar cómo algunas personas afrontan una enfermedad con mayor o
menor éxito que otras. (Verdadero)
124. La psicología médica pertenece a un ámbito holístico, centrado en los síntomas subyacentes y en sanar
la enfermedad. (Falso) (mecanicista)
125. La psicología de la salud emplea un ámbito holístico, sin darle importancia al organismo. (Falso) (sin quitarle
importancia)
126. La psicología de la salud pretende mantener y mejorar la salud, promover actuaciones saludables como
el ejercicio físico. (Verdadero)
127. El concepto de salud se circunscribe únicamente a la ausencia de enfermedad o de un diagnóstico. (Falso) 
128. La Psicología de la Salud es fundamental en tres dimensiones: en la salud, en la enfermedad y en los
cuidados de la salud. (Verdadero)
129. La Psicología de la Salud es una ciencia interdisciplinar en la que intervienen ciencias médicas, sociales
y educativas que están implicadas en el proceso de cambio personal. (Verdadero)
130. La dependencia hacia otras personas, no ser capaz de afrontar la soledad, el perfeccionismo excesivo, el
egoísmo y los pensamientos distorsionados de todo o nada son actitudes disfuncionales que aumentan el
riesgo de padecer enfermedades. (Verdadero)
131. Las ideas y creencias se ven relacionadas con la salud. (Verdadero)
132. La psicología se basa en la observación plenamente. (Falso) (ciencia empírica)
133. La psicología de la salud no se considera una ciencia interdisciplinar. (Falso)
134. Prevenir la enfermedad y tener tratamientos más adecuados fue uno de los objetivos propuestos por
Matarazzo. (Verdadero)
135. La psicología es una ciencia basada en la observación solamente (Falso).
136. La conducta de salud es un proceso comportamental (Verdadero).
137. El ambiente no tiene importancia en el organismo (Falso).
138. La psicología es asistemática (Falso).
139. Las emociones no influyen en la conducta (Falso)
140. La salud no se circunscribe únicamente a la ausencia de una enfermedad (Falso)
141. La psicología de la salud tiene importancia en la salud, las enfermedad y en las adicciones (Falso) 
142. Según el psicoanálisis todas la enfermedades tienen origen orgánico (Falso)
143. Los psicólogos de la salud no necesitan conocimientos médicos de los órganos ya que trabajan con la
conducta (Falso)
144. La psicología de la salud es una ciencia exacta y capaz de predecir el comportamiento.(Falso).
145. Las emociones, tanto positivas como negativas, influyen determinantemente en la conducta del
individuo. (Verdadero)
146. A la hora de hacer un diagnóstico, es mejor hacerlo en solitario que trabajar interdisciplinarmente. (Falso) 
147. La psicología de la salud es importante en tres dimensiones: la Salud, la enfermedad y los cuidados de la
salud. (Verdadero)
148. La psicología de la salud, no solo se debe a la psicología, sino que se origina desde muchos ámbitos y
disciplinas. (Verdadero)
149. La psicología de la salud no emplea un ámbito más holístico e integral y le quita importancia al organismo. (Falso)
150. La psicología médica es una disciplina organicista, centrada en los síntomas y en curar una enfermedad. (Falso)
151. La medicina conductual y la psicología de la salud nacen desde el ámbito de la educación, la conducta y el aprendizaje. (Verdadero)
152. La psicología de la salud pretende mantener y mejorar la salud promoviendo el ejercicio físico, entre otras cosas. (Verdadero)
153. No es necesario tomar conciencia de los aspectos etiológicos, que son aquellos factores en los que las personas pueden tener más riesgo o se encuentre en una situación donde tenga más vulnerabilidad para tener un problema. (Falso)
154. Una de las conexiones que tiene la psicología de la salud con respecto a la enfermedad son las propias creencias con las que cuenta el individuo. (Verdadero)
155. La psicología de la Salud es importante en 3 dimensiones: en la Salud, en la enfermedad y en la percepción de la enfermedad. (Falso) (en los cuidados de la Salud)
156. La psicología de la Salud pertenece únicamente al ámbito de la psicología. (Falso) (también pertenece al área de educación, sociología, etc.)
157. La Psicología de la Salud es interdisciplinar, cuenta con diferentes ciencias y profesionales. (Verdadero)
158. La psicología médica es una disciplina mecanicista, mientras que la psicología de la Salud se mueve en
una disciplina más holística. (Verdadero)
159. La salud es únicamente ausencia de enfermedad. (Falso) (prosperidad, apertura al cambio, equilibrio en el
bienestar, redes de apoyo)
160. Un psicólogo de la Salud no necesita tener conocimientos médicos ya que únicamente se centra en el
ámbito cognitivo. (Falso) (sí los necesita)
161. Las enfermedades psicofisiológicas consisten en la participación activa de factores psicológicos en
enfermedades orgánicas. (Verdadero)
162. La medicina conductual trata tanto del tratamiento como la prevención de enfermedades o disfunciones
corporales. (Verdadero)
163. Un factor que puede predecir la enfermedad es la dependencia a lo que piensan los demás de nosotros. (Verdadero)
164. No se necesita el consentimiento de los padres siendo menor de 18 años para realizar una recogida de
datos del cliente. (Falso)
165. La Psicología de la Salud es interdisciplinar. (Verdadero)
166. En la Psicología de la Salud se implican las ciencias médicas, sociales y educativas junto con la
Psicología para realizar un proceso de cambio. (Verdadero)
167. La psicología es una ciencia que sólo se ocupa del comportamiento humano. (Falso)
168. La psicología médica tiene un ámbito holístico. (Falso)
169. La psicología de la salud pretende mantener y mejorar la salud, prevenir la enfermedad y tener
tratamientos acertados y especializados. (Verdadero)
170. La psicología de la salud es capaz de predecir el comportamiento e identificar los factores de riesgo. (Falso) 
171. La dependencia hacia los demás es una variable causal que puede predecir una enfermedad. (Verdadero) 
172. Existe comorbilidad cuando prevalece más de una condición crónica en el individuo. (Verdadero)
173. El hecho de ser perfeccionista es una variable causal que puede predecir una enfermedad. (Verdadero)
174. La psicología es una ciencia que se ocupa del comportamiento humano y animal y de los procesos
mentales. (Verdadero)
175. La psicología intenta mantener y descuidar las capacidades cognitivas superiores como el lenguaje, la
memoria, la atención o la percepción. (Falso)
176. La observación se basa en el empirismo, partiéndose de una observación con un buen ojo clínico y que
esté avalada con alguna prueba física que tenga que ver con el contraste un poco más objetivo, como
pruebas bioquímicas o psicofisiológicas. (Verdadero)
177. En un sentido más objetivo, el concepto de salud se limita únicamente a la ausencia de enfermedad. (Falso) 
178. La psicología de la salud es importante en la salud, en la enfermedad y en los cuidados de la salud. (Verdadero) 
179. La psicología de la salud solamente pertenece a la psicología. (Falso)
180. La psicología de la salud pretende mantener y mejorar la salud y promover actuaciones como el ejercicio
físico. (Verdadero)
181. Uno de los objetivos de Matarazzo es prevenir la enfermedad y tener unos tratamientos cada vez más
acertados y más especializados. (Verdadero)
182. Uno de los objetivos menos importantes de Matarazzo es tomar conciencia de los aspectos etiológicos. (Falso)
183. Un aspecto importante en psicología de la salud es la comorbilidad, es decir, cuando prevalece más de una condición crónica en el individuo. (Verdadero)
184. Existen dificultades para definir el problema por el que se acude a consulta. (Verdadero)
185. La psicología está conectada a la salud a partir de nuestras propias creencias, sobre qué pensamos de
nuestra salud o en qué consiste. (Verdadero)
186. La psicología de la salud no emplea un ámbito holístico, ni integral. (Falso)
187. La psicología sólo hace uso de la observación. (Falso)
188. La psicología de la salud no se basa en valoraciones psicométricas. (Falso)
189. Es común que en la psicología de la salud trabajen en equipo profesionales de diferentes disciplinas. (Verdadero)
190. El trato terapeútico no tiene relevancia para el paciente. (Falso)
191. La psicología clínica de la salud está más centrada en la existencia de síntomas, con un enfoque
mecanicista. (Falso)
192. La relación entre la ansiedad y síntomas como la taquicardia sería un ejemplo de enfermedad
psicosomática. (Verdadero)
193. El hecho de experimentar somatizaciones hace que se promueva el desarrollo de buenos hábitos, como
el deporte. (Verdadero).
194. Se advierten situaciones problemas sobre todo en el ámbito de la pareja y en la crianza de los hijos. (Verdadero)
195. Es importante que la psicología de la salud tome una metodología válida y fiable. (Verdadero)
196. La psicología de la salud se circunscribe sólo a la ausencia de enfermedad. (Falso)
197. La importancia de la psicología de la salud se puede resumir en tres ámbitos: salud, enfermedad y
cuidados. (Verdadero)
"""



lineas = re.split(r'\n(?=\d+\.)', text.strip())

# Diccionario para almacenar las preguntas y los contenidos entre paréntesis
preguntas_y_contenidos = {}

for linea in lineas:
    # Extraer la pregunta y el contenido entre paréntesis
    match = re.match(r'\d+\.\s(.*?)(\((.*?)\))', linea.replace('\n', ' '), re.S)
    if match:
        # Agregar al diccionario
        preguntas_y_contenidos[match.group(1).strip()] = match.group(3).strip()

# Mostrar resultados
print("Preguntas y contenido entre paréntesis:")
# for pregunta, contenido in preguntas_y_contenidos.items():
#     print(f"Pregunta: '{pregunta}', Contenido entre paréntesis: '{contenido}'")







data = []
#
#
# def regex_questions(texto):
#     questions_by_tema = []
#     for tema in texto:
#         # Split the text into individual questions
#         questions = re.split(r'\n', tema)
#         print(questions[:3])
#         questions_by_tema.append(questions)
#     return questions_by_tema
#
#
#
def read_questions(questions_by_tema, question_pk, response_pk, tema):
    for question, valor in questions_by_tema.items():
        texto = question.replace('\n', ' ')
        if len(texto) < 2:
            continue
        question_data = {
            "model": "examenes.pregunta",
            "pk": question_pk,
            "fields": {
                "tema": tema,  # ID del tema al que pertenecen las preguntas
                "texto": texto
            }
        }
        data.append(question_data)

        for option_text in ("Verdadero", "Falso"):
            response_data = {
                "model": "examenes.opcionderespuesta",
                "pk": response_pk,
                "fields": {
                    "pregunta": question_pk,
                    "texto": str.capitalize(f'{option_text}'),
                    "es_correcta": valor == option_text
                }
            }
            data.append(response_data)
            response_pk += 1

        question_pk += 1

    return data, response_pk, question_pk
#
#
def export_questions(q_data):
    # Output the JSON to a file
    with open('q_salud.json', 'w') as f:
        json.dump(q_data, f, ensure_ascii=False, indent=4)
#
#
# qs = regex_questions(text)
#
# # Start the question IDs from 89 as requested
question_pk = 180
response_pk = 463
# # Datos iniciales para Curso y Tema
# temas_pk = [2, 9, 10, 11, 12]
#
tema1_salud = 14
question_pk = 440
response_pk = 983

print(f"total preguntas: {len(preguntas_y_contenidos)}")
print(list(preguntas_y_contenidos.keys())[-5:])

read_questions(preguntas_y_contenidos, question_pk, response_pk, tema1_salud)


# # muestra = json.dumps(data[:10], indent=2)
# # print(muestra)

print(f"exportadas: {len(data)/3}")

export_questions(data)
