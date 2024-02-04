import json
import re

text = ["""
Tener un coeficiente intelectual normal-alto es una característica de la dificultad del aprendizaje. VERDADERO
El volteo del suelo es un signo característico de la contralateralidad. FALSO (Homolateralidad).
Cada contacto corporal, cada movimiento y cada emoción se convierten en una actividad eléctrica, pero no química, que propicia el avance del impulso genético modificando la configuración del cerebro. FALSO (también química).
Uno de los bloques funcionales para explicar el funcionamiento cerebral es la activación de la corteza cerebral. FALSO (falta óptima).
El desarrollo madurativo de la atención y la concentración necesario para facilitar el proceso de aprendizaje y favorecer la activación de los bloques funcionales siguientes (Luria, 1973,1980) tienen sus estructuras cerebrales en el córtex frontal. FALSO (activación óptima de la corteza cerebral).
Uno de los bloques funcionales para explicar el funcionamiento cerebral es la activación óptima de la corteza cerebral. VERDADERO
La activación óptima de la corteza cerebral se encarga de realizar los procesos perceptivos visuales, auditivas y táctiles. FALSO (de eso se encarga el bloque 2→INPUT)
Uno de los tres bloques funcionales que propone Luria para explicar el funcionamiento cerebral es el input, o entrada de información por los sentidos y su elaboración. VERDADERO
El bloque tercero propuesto por Luria se corresponde con las áreas terciarias, que no tienen una modalidad sensorial propia, sino supramodal. VERDADERO
Para realizar los procesos visuales, auditivos y táctiles, esenciales en la aplicación de metodología de aprendizaje de nuevos conocimientos basadas en la sensorialidad, participan los lóbulos occipital, temporal y parietal, del bloque tercero propuesto por Luria (1973, 1980). FALSO (bloque dos)
Las áreas secundarias y terciarias tienen una modalidad sensorial propia y son supramodales. FALSO
Según el modelo de Luria, las áreas terciarias son supramodales. VERDADERO
En el modelo de Luria, los bloques segundo y tercero se organizan jerárquicamente en áreas primarias, secundarias y terciarias. VERDADERO
Los bloques de Luria segundo y tercero son supramodales. FALSO (las áreas terciarias de los bloque tercero).
En los tres bloques de Luria hay un desarrollo funcional progresivo desde las áreas terciarias a las secundarias hasta las primarias. FALSO (desde las primarias a las secundarias y de éstas a las terciarias).
Hay un desarrollo funcional regresivo de las áreas primarias a las secundarias y a las terciarias. FALSO (progresivo).
La estabilidad de la actividad voluntaria y la perseveración de la conducta, son procesados por los lóbulos frontales según Luria (1973, 1980). VERDADERO
El tercer bloque funcional explicado por Luria recibe información del exterior. FALSO (bloque dos).
Luria concebía los lóbulos parietales responsables de la inhibición a estímulos irrelevantes la perseveración de la conducta, la direccionalidad y selectividad de procesos, la estabilidad de la actividad voluntaria, la capacidad para concentrarse y, el control y la regulación interna del lenguaje. FALSO (son los lóbulos frontales).
Una de las responsabilidades de los lóbulos frontales, según Luria, es la estabilidad de la actividad voluntaria. VERDADERO
El síndrome desinhibido o psicopático tiene lugar en el córtex orbitofrontal. VERDADERO
El síndrome desinhibido o psicopático se caracteriza por una reducción de las conductas espontáneas. FALSO (apático)
La principal característica del síndrome psicopático es la existencia de un déficit en las condiciones ejecutivas como la indiferencia y pobreza afectiva. FALSO (las condiciones ejecutivas las altera el síndrome disejecutivo)
Los bloques primero y segundo se organizan en áreas primarias y secundarias. FALSO (sólo en el bloque segundo)
El desarrollo del SN se relaciona con el ambiente y es independiente a la genética. FALSO
En el desarrollo del SN, los dos momentos clave son la neurogénesis y la maduración cerebral. VERDADERO
La monopedestación ocurre entre los 18 y 24 meses. FALSO (entre los 24 y los 36 meses)
El inicio de la monopedestación se da entre los 24 -36 meses de edad. VERDADERO
En la etapa neonato-homolateral de reptado contralateral se produce la maduración de la vía piramidal. FALSO (neonato contralateral, de 0 a 3)
En la etapa neonato-homolateral de reptado contralateral se produce la maduración de la vía piramidal. FALSO (neonato contralateral)
En la etapa neonato-homolateral alterna no hay control ni equilibrio. FALSO (si hay)
En la etapa del desarrollo neonato-homolateral alterna, se da un control de la línea media del cuerpo. VERDADERO
En la etapa neonato-contralateral de reptado contralateral se da un control del núcleo medular alto. FALSO (es del bajo)
En las fases/etapas del desarrollo neonato -homolateral alterna se da un control de la línea media del cuerpo, el niño aprende a discriminar izquierda y derecha entre los 5 y 7 años y se va orientando mejor a nivel motriz, vivencial y cognitivo. FALSO (sucede en la etapa entre 0-3 años)
En la etapa neonato-homolateral alterna la cabeza es el punto superior del eje referencial y empieza a haber simetría y equilibrio en el polo superior. VERDADERO
En la etapa neonato homolateral alterna se da una maduración de la vía piramidal y una fusión interhemisférica. FALSO (es en la etapa contralateral)
La relación entre los dos hemicuerpos tiene lugar en la etapa neonatal contralateral de reptado contralateral. VERDADERO
El niño aprende a discriminar la derecha y la izquierda entre los 2 y los 3 años y se va orientando mejor a nivel motriz, vivencial y cognitivo, siendo la capacidad simbólica la que le posibilita trabajar mentalmente. FALSO (Entre los 4 y 5)
La capacidad simbólica es la característica más específica del ser humano, es lo que posibilita trabajar mentalmente, realizar presentaciones mentales, imaginar, fantasear, y aprender conceptos, el lenguaje y otra serie de habilidades abstractas importantes para la vida cotidiana. VERDADERO
Entre los programas de desarrollo sensoriales y motores de 3 a 6 años, se proponen los circuitos neuromotores como conjunto de ejercicios y juegos que favorecen el desarrollo neurofuncional de la percepción auditiva. FALSO
Entre los programas de desarrollo de habilidades visuales de 3 a 6 años, se proponen un conjunto de ejercicios y de juegos que favorecen el desarrollo neurofuncional, que tiene relación directa con las habilidades de aprender idiomas. FALSO (auditivo)
En el desarrollo corporal y especial, el eje y plano vertical medio se da entre los 18 y 24 meses. VERDADERO
A partir de los 7 años, se amplía la organización del lenguaje hablado y la fonación perfecta. VERDADERO
Saltos con pies juntos es homolateral. FALSO (contralateral)
El patrón homolateral se refiere al movimiento simultáneo y coordinado de brazo y pierna del mismo lado. VERDADERO
Los cambios cerebrales más representativos en la adolescencia corresponden a procesos de mielinización y cambios de estructura del tronco encefálico. FALSO (no hay cambios en el tronco encefálico)
Los cambios cerebrales más representativos en la adolescencia corresponden a procesos de mielinización y cambios en estructuras del estriado ventral, cuerpo calloso y glándula pineal, así como también en el aumento y maduración del cerebelo y la corteza frontal. FALSO (corteza pre-frontal)
Un cambio importante en la adolescencia, es el aumento de mielinización y maduración de la corteza prefrontal. VERDADERO
Los cambios cerebrales más representativos en la adolescencia corresponden a procesos de mielinización, cambios en el estriado ventral, el cuerpo calloso, y la glándula pineal y en el aumento y maduración del cerebro de la corteza prefrontal. VERDADERO
El metaconocimiento es una habilidad de pensamiento en la adolescencia y es necesario para pensar y para aprender bien; saber el cómo se aprende y el para que incorporar el proceso al aprendizaje de los contenido de estudio. VERDADERO
La diferencia fundamental entre DDAA y trastorno del desarrollo, es que este se relaciona con una alteración, o incapacidad en el plano orgánico, mientras en las DDAA se da en el plano biológico. VERDADERO
En el trastorno del desarrollo, suponen problemas personales la violencia entre compañeros. VERDADERO
En los trastornos del desarrollo, suponen problemas psicopatológicos las dificultades de aprendizaje, la lectura, la escritura y matemáticas. FALSO (los problemas psicopatológicos incluyen la ansiedad, la depresión y problemas de conductas)
Las dificultades del aprendizaje se manifiestan primariamente en problemas en el ámbito físico y dificultades del procesamiento en los principales ámbitos cognitivos. FALSO
Entre las características definitorias de los trastornos del desarrollo está la cronicidad de las dificultades. VERDADERO
La afección secundaria tiene lugar en las áreas curriculares. VERDADERO
Las DDAA se definen como aquellas dificultades de aprendizaje que están constituidas por un conjunto heterogéneo de problemas cuyo origen probablemente es, una disfunción del SNP. FALSO (Es una disfunción del SNC)
Los DDAA son un grupo heterogéneo de trastornos que responden a diferentes alteraciones del SNC y que manifiestan mediante múltiples variables y cognitivas diferentes según los sujetos. VERDADERO
En las DDAA no es posible establecer un perfil único que explique las dificultades conductuales. VERDADERO
En la definición de las DDAA dada por Santiuste y González-Pérez se destaca que éstas no son las causas, sino los efectos de problemas de personalidad, sociales y culturales. FALSO (no son efectos, sino causas)
Según la definición de DDAA dada por Santiute y González-Pérez, ésta contempla factores neurológicos y biológicos, pero no genéticos. FALSO (los tres)
Las DDAA se manifiestan secundariamente con problemas en diversas áreas curriculares (CC. Experimentales, CC. Sociales, segundo idioma, escritura). FALSO (la escritura corresponde a las primarias)
Tener un CI normal o alto supone una de las características definitorias de las DDAA. VERDADERO
Las dificultades del aprendizaje se relacionan con una alteración en el plano orgánico. FALSO (son de carácter evolutivo, los trastornos si son alteraciones en el plano orgánico)
El reptado circular es un signo de la homolateridad. VERDADERO
Una dificultad en el aprendizaje se caracteriza por su transitoriedad con manifestaciones evolutivas en un ámbito. VERDADERO
En la clasificación de trastorno específico del aprendizaje, la especificación de la severidad contempla la gravedad leve, moderada y severa. VERDADERO
Las dificultades de aprendizaje se manifiestan primariamente en el ámbito lingüístico. VERDADERO
En el desarrollo de 3 a 6 años los aspectos más importantes son el desarrollo del lenguaje y la capacidad gráfica, el perfeccionismo del movimiento y las emociones y los aspectos que va desarrollando el sistema límbico. FALSO (no es aspectos es afectos)
""",
"""
La ruta léxica sigue el circuito ventral, donde interviene el giro fusiforme para la lectura de palabras conocidas. VERDADERO
La exploración psicolingüística identifica a los niños que hacen un uso mayoritario de la ruta léxica cuando solo son capaces de leer palabras conocidas, por lo que sería una dislexia fonológica. VERDADERO
Según el modelo dual de lectura, la ruta léxica no puede identificar las pseudopalabras, pero sí las palabras más frecuentes, regulares e irregulares. VERDADERO
En la ruta léxica puede identificar palabras frecuentes, pero no pseudopalabras. VERDADERO
La ruta subléxica se encuentra en el giro fusiforme y la ruta léxica es la del fascículo fronto occipital inferior. FALSO (subléxica se encuentra en el giro angular)
La ruta léxica sigue el circuito ventral e interviene el giro fusiforme para la lectura de palabras conocidas. VERDADERO
Estudios con RMF confirman circuitos distintos implicados en la lectura, el ventral fascículo fronto occipital inferior o giro fusiforme para la lectura de palabras conocidas y el superior fascículo arqueado o giro angular implicado en la lectura de palabras nuevas. VERDADERO
En la dislexia fonológica se usa principalmente la ruta indirecta. FALSO (es en la dislexia visual)
En la dislexia morfémica, la lectura de pseudopalabras es peor que la de palabras. FALSO (es en la dislexia fonológica)
En el tipo de dislexia con dificultades en la ruta indirecta, los errores de regularización suponen lecturas lentas, titubeo y tanteo de pronunciar la palabra esperando acertar. FALSO (son las dificultades en la ruta directa)
Las áreas que se codifican en el trastorno específico del aprendizaje del DSM V son dislexia, disgrafía y dispraxias. FALSA (discalculia)
Estudios con RMF evidencian la existencia de un doble circuito o Modelo de Doble Flujo, en el procesamiento del lenguaje: el ventral (comprensión) y en dorsal (acción motora) VERDADERO
Para una percepción y funcionamiento cognitivo correcto es clave la participación de las áreas corticales de los lóbulos temporales y el plano occipital. FALSO (lóbulo frontal y plano temporal)
En la etiología de la dislexia, el modelo neuropsicológico propone que ésta implica necesariamente alguna dificultad neurológica. FALSO
En la etiología de la dislexia, el modelo neuropsicológico propone que esta no implica necesariamente alguna dificultad neurológica. VERDADERO
En la etiología de la dislexia, desde el modelo psicolingüístico se propone como funcionamiento para la adquisición de la lectura que se pronuncie la palabra una vez se aprenda el proceso semántico, por la conexión existente entre este y el procesador fonológico. VERDADERO
La etiología de la dislexia, desde el modelo psicolingüístico, propone como funcionamiento de adquisición de la lectura que, se pronuncia la palabra, una vez se accede al procesador semántico, por la conexión existente entre este, y el procesador fonológico. VERDADERO
En el tipo de dislexia con dificultades de la ruta léxica, los errores de regulación suponen lectura lenta, titubeo y tanteo de pronunciar la palabra esperando acertar. VERDADERO
En el tipo de dislexia con dificultades en la ruta indirecta, los errores de regularización suponen lecturas lentas, titubeo y tanteo de pronunciar la palabra esperando acertar. FALSO (es la directa dislexia fonológica)
La dislexia implica un retraso específico psicolingüístico, por estar afectados los procesos que intervienen en el procesamiento léxico. VERDADERO
Desde la psicolingüística, el enfoque más relevante para explicar la dislexia es el cognitivo porque se centra en identificar los estadios del procesamiento lingüístico deficitarios que causan el problema lector y, también, para la elaboración del tratamiento reeducador. VERDADERO
La técnica de lectura conjunta o en sombra, supone un ejemplo de intervención para la dislexia del enfoque funcional de la psicología cognitiva, considerando al procesamiento fonológico como su principal déficit. VERDADERO
Las pruebas normativas de la evaluación de la dislexia es evaluar las habilidades específicas. FALSO (habilidades generales)
La historia evolutiva, educativa, médica y social del niño son el análisis necesario para la evaluación de la dislexia. VERDADERO
Para la evaluación formal de la lectoescritura, entre las pruebas orientadas a criterio están las neuropsicológicas. FALSO (psicolingüística, las normativas son las de evaluación neuropsicológica)
La evaluación formal de la dislexia se realiza con pruebas normativas y pruebas orientadas a criterio. VERDADERO
Estudios con RMF confirman dos circuitos distintos implicados en la lectura: el circuito superior situado en el fascículo arqueado, implicado en la lectura de palabras nuevas, y el ventral franco -occipital anterior, para la lectura de palabras conocidas. FALSO (fronto occipital inferior)
Estudios con RMF confirman dos circuitos distintos implicados en la lectura: el ventral (fascículo frontooccipital inferior) o giro fusiforme, para la lectura de palabras conocidas y, el superior (fascículo arqueado) o giro angular, implicado en la lectura de palabras nuevas. VERDADERO
En la dislexia morfémica, la lectura de pseudopalabras es peor que la de palabras. VERDADERO
La prueba PEREL (Maldonado et al, 1992), para evaluación del retraso en la lectura, es aplicable de 5 a 8 años. FALSO (de 7 a 9 años)
La prueba de Comprensión Lectora de Lázaro se aplica a partir de los 8 años. VERDADERO
La batería de evaluación de los procesos lectores PROLEC -R, se aplica desde los 6 a los 12 años, tiene un enfoque conductual y además de evaluar los procesos léxicos y sintácticos también identifica los semánticos. FALSO (el enfoque es cognitivo)
Para evaluar la consciencia fonológica se usa la escala de Conners. FALSO (Yakuba)
Para la evaluación de la conciencia fonológica, se suelen emplear tareas concretas que miden habilidades metalingüísticas de carácter fonológico, como segmentación, asociación fonética, y una prueba formal para ello es la de Yakuba. VERDADERO
Para evaluar la conciencia fonológica se utilizan tareas concretas que miden habilidades metalingüísticas de carácter fonológico. VERDADERO
El enfoque neuropsicológico de Bakker, para la intervención psicoeducativa, indica que para la dislexia P hay que estimular el hemisferio izquierdo. VERDADERO
En el enfoque neuropsicológico de Bakker, para la intervención psicoeducativa de la dislexia en el aula, propone que, en los casos que denomina dislexia P, debe tratarse en la estimulación del hemisferio izquierdo, por ejemplo, presentando letras tridimensionales para que palpen con la mano derecha. VERDADERO
En el enfoque de Bakker, para la dislexia L se ponen palabras en el hemicampo izquierdo. VERDADERO (HEMISFERIO DERECHO)
El enfoque neuropsicológico de Bakker, para la intervención psicoeducativa de la dislexia en el aula, propone que ésta debe basarse en la estimulación del hemisferio izquierdo en los casos que se denominan dislexia lingüística. FALSO (perceptiva)
El método sintético para el entrenamiento de la lectoescritura se propone especialmente para el aprendizaje de idiomas transparentes como el castellano. VERDADERO
El método analítico para el entrenamiento de la lectoescritura (Sampascal, 2011), tiene como principal crítica que retrasan la adquisición de automatismos implícitos en los niveles elementales. VERDADERO
Los profesores han de ofrecer, al alumno con dificultades lectoescritoras, atención lo más personalizada posible para que disponga de estrategias compensatorias. VERDADERO
El modelo de Seymour y McGregor implica la adquisición de la lectura con tres procesadores parcialmente solapados y cuatro estadios. FALSO (tres estadios y cuatro procesadores)
El Modelo de Seymour y McGregor: 3 estadios parcialmente solapados y 4 procesadores. VERDADERO
El procesador de estadio logográfico encargado del reconocimiento de las características visuales de las palabras es el fonológico. FALSO (semántico).
El procesador ortográfico requiere la conversión de las características visuales de las letras en identidades abstractas. VERDADERO
El desarrollo madurativo de la atención y la concentración hace referencia a la formación reticular. VERDADERO
""",
"""
Según Ribas y Fernández, la disortografía supone errores sistemáticos y reiterados en la ortografía y escritura, clasificados en errores lingüísticos perceptivos, fisioespaciales relacionados con el contenido. FALSO (visoespacial)
Las causas de la disortografía son perceptivas, intelectuales, lingüísticas, afectivo emocionales y pedagógicas. VERDADERO
La escritura del dictado se relaciona con el área 37 de Brodman. VERDADERO
La escritura a mano se relaciona con el área 6 de Brodmann. VERDADERO
El área de Brodmann 39 se relaciona con significado y ortografía. VERDADERO
El área 46 de Brodmann es el procesamiento sintáctico. FALSO (área 47)
Según el DSM V (APA, 2013), algunas subhabilidades del trastorno específico del aprendizaje que pueden estar alteradas en la escritura son: dificultades en las reglas de puntuación, en la claridad y en la asociación de ideas. FALSO (no son dificultades en la asociación de ideas)
Entre las subhabilidades del trastorno específico del aprendizaje que pueden estar alteradas en la escritura, según el DSM-V, están las dificultades en el tamaño, letra, claridad, organización y comprensión escrita. FALSO
En la etiología de la disortografía, una causa lingüística sería dispedagogías, porque al articular mal un fonema, se repite interiormente mal y se pronunciará y escribirá también mal. FALSO
En la etiología de la disortografía, una causa intelectual serían las dificultades en su articulación, porque al articular mal un fonema, se repite mal interiormente, y se pronunciará y se escribirá mal. FALSO (sería una causa lingüística)
Los errores disortográficos se centran en la dificultad para transmitir el código lingüístico hablado o escrito mediante las letras o grafemas correspondientes, respetando la asociación correcta grafema-fonema. VERDADERO
La disgrafía es un conjunto de errores que afecta a la palabra. FALSO (a su trazado)
Según Rivas y Fernandez (2011), la disortografía supone errores sistemáticos y reiterados en la escritura u la ortografía clasificables en errores lingüísticos perceptivos, visoespaciales y visoauditivos, relacionados con el contenido referido a las reglas de ortografía. VERDADERO
Según Ramírez (2000), entre las pautas de intervención psicoeducativas en el aula para la enseñanza de la ortografía, no son aconsejables las técnicas habituales de dictado, ni las copias repetidas de una palabra. VERDADERO
Según Ramírez, entre las pautas de intervención psicoeducativa en el aula para la enseñanza de la ortografía, son útiles técnicas habituales como el dictado, la copia y las listas de palabras. FALSO (estas empeoran)
Como herramientas recomendadas para la recuperación de la disortografía en el aula, los ficheros cacográficos suponen la elaboración de tarjetas que por delante contienen la palabra bien escrita, y por detrás, está incompleta. VERDADERO
Como herramienta recomendada para la recuperación de la disortografía en el aula, los listados monográficos, servirán de base para realizar memorizaciones, dictado, formación de frases, clasificaciones, formaciones de familias léxicas, etc. FALSO (cacográficos)
El DSM-V no diferencia disortografía de disgrafía. VERDADERO
Los fallos pedagógicos pueden verse reforzados por las dispedagogías. VERDADERO
La disgrafía tiene una base biológica y genética, mientras que la disortografía supone una dificultad de carácter evolutivo, asociada, en muchos casos, al propio ritmo de maduración y aprendizaje del niño. FALSO (la dislexia tiene una base biológica y genética)
La dislexia tiene una base biológica y genética, mientras que la disortografía supone una dificultad de carácter evolutivo. VERDADERO
La disortografía cultural se refiere a la dificultad para el aprendizaje de las reglas ortográficas, mayúsculas después de puntos. VERDADERO
Entre las pruebas formales para la evaluación de la disortografía, la Prueba de Escritura de Terrasa (1997) tiene aplicación también para niños de primer ciclo de educación primaria. VERDADERO
Una prueba de la evaluación de la disortografía es la prueba de escritura de Terrasa. VERDADERO
Los listados cacográficos son un inventario de errores cometidos en el que al lado se pone la palabra correcta y se repite algunas veces. FALSO (no se repite algunas veces)
Entre las características de la disortografía relacionadas con el contenido, de Rivas y Fernández, estaría la unión y separación de sílabas pertenecientes a dos palabras. VERDADERO
Dislexia presenta también disortografía, pero un niño con disortografía no necesariamente es un disléxico, ya que la disortografía no afecta a la lectura. VERDADERO
Según Rivas y Fernández la sustitución de fonemas vocálicos y/o consonánticos afines por el punto y/o modo de articulación, como ... por séptimo, sería una característica de la disortografía relacionada con el contenido. FALSO (perceptivo-cinética)
""",
"""
La incapacidad para escribir pseudopalabras es de discalculia. FALSO
La discalculia se define como aquellas dificultades caracterizadas por problemas en el procesamiento de la información numérica, el aprendizaje de acciones aritméticas y la ejecución correcta y fluida del cálculo matemático. VERDADERO
Según Dehaene et al (1999), la información numérica procesada por el sistema cuantitativo no verbal está asociada al segmento horizontal del surco intraparietal (HIPS), que se activa más cuando se realiza una estimación aproximada que, cuando se realiza un cálculo exacto. VERDADERO
A nivel cerebral, el giro angular izquierdo interviene en la resolución de hechos matemáticos, procesamiento numérico y cálculo que requieren procesamiento verbal, representación espacial y resolución de tareas aritméticas complejas. FALSO (aunque falta numérica)
A nivel cerebral, el giro angular izquierdo interviene en la resolución de hechos matemáticos, procesamiento numérico y cálculo que requiere procesamiento verbal, procesamiento numérico espacial y resolución de tareas aritméticas complejas. VERDADERO
En las multiplicaciones se activa la corteza occipito-temporal. FALSO (giro angular izquierdo).
El sistema parietal posterior superior se encarga de tareas de memoria de trabajo. FALSO (es la dorsolateral)
La corteza occipito-temporal se encarga del procesamiento de números. VERDADERO
La corteza cingulada se dedica a la toma de decisiones. VERDADERO
En cuanto a las DAM, en los cálculos aproximados se observa una mayor activación de las áreas cerebrales involucradas en el lenguaje, mientras que en el cálculo exacto se activa más el lóbulo parietal de los dos hemisferios. FALSO (al revés)
La discalculia se define como aquellas dificultades caracterizadas por problemas en el procesamiento de la información numérica, el aprendizaje de acciones aritméticas y la ejecución correcta y fluida del cálculo matemático. VERDADERO
Antes de iniciarse el cálculo escrito deben adquirirse los conceptos de suma, resta, multiplicación y división junto con los conocimientos simbólicos que indican. VERDADERO
Los cálculos aproximados se observan en áreas cerebrales involucradas en el lenguaje. FALSO (lóbulos parietales de ambos hemisferios, pero con predominancia del derecho).
En la aproximación, aunque se activan los dos hemisferios cerebrales, existe una cierta dominancia del derecho. VERDADERO
La estimación consiste en la capacidad para estimar el resultado de un problema antes de resolverlo. VERDADERO
Como factores críticos se pueden encontrar creencias, inteligencia emocional y métodos del profesor. VERDADERO
En las conclusiones de la serie de experimentos con bebés de cinco meses (Wynn, 1992) se sugiere que, al mirar más tiempo cuando aparecían los juguetes con el resultado lógico, los bebés muestran poseer una capacidad innata para el procesamiento numérico. FALSO (resultado no lógico)
Uno de los criterios para el diagnóstico de las DAM es que el rendimiento académico de los sujetos en matemáticas los sitúe por debajo de lo esperado por su edad cronológica, aun teniendo un CI entre 75 y 120 y un déficit sensorial, visual, auditivo y motor. FALSO (sin déficit, y con escolaridad correcta)
Uno de los criterios para el diagnóstico de las DAM, es que el rendimiento académico del sujeto en matemáticas lo sitúe por debajo de lo esperado por su edad cronológica, aun teniendo un CI entre 65 -120 y ningún déficit sensorial, visual, auditivo y/o motórico. FALSO (75)
La hipótesis evolutiva de las DAM pone el énfasis en la dificultad propia de la asignatura y de su enseñanza, en la forma de intervenir para dar respuesta a la diversidad de aptitudes y actitudes e interés del alumno. FALSO (educativa)
Poner el énfasis en las actitudes e interés del alumno y en la dificultad propia de la asignatura, supone una hipótesis etiológica evolutiva de las DAM. FALSO (educativa)
La etiología de las DAM, en lo evolutivo, se daría por un déficit de estimulación en las primeras etapas del desarrollo. VERDADERO
En cuanto a las DAM, en los cálculos aproximados se observa una mayor activación de las áreas cerebrales involucradas en el lenguaje, mientras que en el cálculo exacto se activa más el lóbulo parietal de los dos hemisferios. FALSO (al revés)
La prueba de aritmética y la de memoria auditiva inmediata (dígitos) de la Escala de Weschler (2012), WISC -IV, es para administrar a niños de 6 a 16 años. VERDADERO
Entre las pruebas psicológicas para la evaluación de las DAM, estaría la batería de Luria que evalúa los trastornos psicológicos a partir de 9 años con una prueba aritmética con dos subtests. FALSO (a partir de 7 años)
Entre las pruebas psicológicas para la evaluación de las DAM estaría la batería de Luria-DNI, que evalúa los trastornos neuropsicológicos a partir de los 7 años e incluye una prueba aritmética con 2 subtest (escritura numérica y operaciones aritméticas). VERDADERO
Comprender correctamente que un sistema de numeración está formado por grupos de iguales unidades que dan lugar a unidades de orden superior, es uno de los indicadores útiles para profesores de educación infantil en la detección de DAM. FALSO (no comprender).
En mates, las tareas de la memoria de trabajo como el mantenimiento de resultados intermedios, la planificación, la ordenación temporal de componentes de las tareas, la comprobación de resultados y corrección de errores, tienen su mayor responsable cortical en el lóbulo frontal dorsolateral. VERDADERO
Con alumnos con DAM, las pautas de intervención se centran fundamentalmente en la prevención y desarrollo de una metodología contextual. FALSO (cognitiva)
En los alumnos con DAM, las pautas de intervención se centran fundamentalmente en la prevención y desarrollo de una metodología cognitiva y contextual. FALSO (no se emplea metodología contextual).
Para realizar los procesos visuales, auditivos y táctiles participan los lóbulos occipitales, parietal del bloque tercero propuesto por Luria. FALSO
En la representación de los números arábigos, se activa un sistema superior posterior parietal relacionado con la atención. VERDADERO
Las matemáticas requieren funciones psicológicas como: capacidad de concentración, atención dividida, planificación, memoria de trabajo y memoria visual. FALSO (neuropsicológicas).
Según Carrillo, las dificultades en las matemáticas se entienden por, entre otras, la formalidad de los contenidos y la utilización de un lenguaje funcional muy distinto al natural. FALSO (funcionalidad)
Una de las funciones neuropsicológicas que requieren las matemáticas es la atención dividida. VERDADERO
El DSM-V indica las dificultades en las matemáticas dentro del trastorno específico del aprendizaje. VERDADERO
La inteligencia de Gardner cinético-corporal es la habilidad para resolver problemas utilizando el cuerpo. VERDADERO
Santiuste y González Pérez indican que las pruebas pedagógicas estarían en el tipo de evaluación formal de las DAM, ya que son similares a las de cualquier profesor, pero están estandarizadas y cuentan con baremos poblacionales. VERDADERO
Respecto a las habilidades metacognitivas, Miranda destaca que las de atención y predicción podrían diferenciar a los estudiantes con DAM de los sin DAM. FALSO (predicción y evaluación)
El aprendizaje de las mates en educación secundaria incluye desarrollar la solución flexible de problemas. VERDADERO
""",
"""
El cerebro del niño no es una página en blanco, sino un circuito integrado determinado y controlado por genes. FALSO (no es ninguno de los dos casos)
Cada contacto corporal, cada movimiento y cada emoción se convierten en una actividad eléctrica, pero no química, que propicia el avance del impulso genético modificando la configuración del cerebro. FALSO (también química)
El desarrollo del cerebro es producto de las sucesivas divisiones celulares y del equilibrio entre los genes. FALSO (es producto de la mezcla entre genes y entorno)
La ansiedad se define como una respuesta anormal y no adaptativa ante amenazas reales o imaginarias que prepara al organismo para reaccionar ante una situación de peligro. FALSO (normal y adaptativa)
La ansiedad se define como una respuesta normal y adaptativa ante amenazas reales o imaginarias más o menos difusas, que preparan al organismo para reaccionar ante una situación de peligro. VERDADERO
Las fuentes de información utilizadas para la evaluación de la ansiedad de separación suelen ser los padres y los profesores. FALSO (son los padres y el propio niño)
La ansiedad de separación es más frecuente en niñas que en niños y en niveles socioeconómicos bajos, siendo la edad media de 7 años. FALSO (edad media 9 años)
Para la evolución de la ansiedad de separación se cuenta con el STAIC de Sandin, que permite detectar además otros cuadros clínicos comórbidos como depresión, terrores nocturnos, etc. FALSO (ADIS -IV de Sandín, el STAIC es de Spielberg)
Uno de los instrumentos de evaluación de la ansiedad de separación de niños de 4 a 16 años es el CBCL de Achenbach y Edelbrock (1983), con versiones para cumplimentar por los padres y para profesores. VERDADERO
El modelado con modelos en vivo puede ser de tipo simbólico y/o encubierto. FALSO (sin modelos in vivo)
En el modelo simbólico, el niño observa en persona cómo otros niños disfrutan de estímulos a los que él tiene miedo. FALSO (a través de videos y películas)
El modelado con modelos en vivo se realiza progresivamente con las conductas no ansiógenas. FALSO (con las ansiógenas)
La ansiedad ante la separación de los padres es el único factor relacionado con la fobia escolar. FALSO (no es el único, están la escolaridad y los sucesos vitales negativos)
La fobia escolar solo depende de factores ligados a la escolaridad. FALSO (también depende de la ansiedad por la separación familiar y sucesos vitales negativos)
Entre las características clínicas de la fobia escolar están las taquicardias, trastornos del sueño, náuseas, etc. VERDADERO
La fobia escolar suele aparecer cuando ya llevan varios años en el mismo colegio. FALSO (cambio de ciclo o de escuela)
La fobia escolar es un rechazo para ir al colegio por algún tipo de miedo que está relacionado con la escolaridad, los sucesos vitales negativos y/o la ansiedad por la separación de los padres. VERDADERO
La fobia escolar es un tipo específico de ansiedad infantil que tiende a ocurrir o bien entre los 3 y 4 años, o entre los 11 y 12, especialmente, cuando se produce un cambio de ciclo o de escuela. VERDADERO
En la fobia escolar, como características cognitivas está la anticipación de las consecuencias negativas. VERDADERO
La etiología de la fobia escolar puede estar en cualquier experiencia desagradable vivida por el niño en la escuela, o por temor a la separación de la familia. VERDADERO
La ansiedad tiene sentimientos de inseguridad, de adaptación y de culpabilidad. FALSO (inadaptación)
En la evaluación de fobia escolar se utilizan los inventarios de miedo de Pelechano. VERDADERO
El rechazo a ir al colegio está relacionado, entre otros factores, con el miedo al maestro, ruptura de la unión familiar y enfermedad prolongada. VERDADERO
La ansiedad se emite ante estímulos específicos. FALSO (miedos)
La causa principal de la depresión en el niño es o bien por falta de disciplina o por disciplina excesivamente rígida. FALSO (no sentirse querido)
El CDI de Kovacs es un instrumento de evaluación de las dificultades relacionadas con la ansiedad. FALSO (depresión)
Una de las características de la depresión infantil y adolescente es la de sentirse culpables por hablar de la muerte o del suicidio. FALSO
El CDI es el inventario de ansiedad infantil de Kovacs que se emplea en la evaluación de la fobia escolar. FALSO (depresión)
Para evaluar la depresión, es el inventario de CDS, 8 y 16 años, solo colectiva. FALSO (escala)
La atención más adecuada de niños y adolescentes con trastornos depresivos es multimodal, teniendo en cuenta los tres aspectos de intervención: farmacológica, psicológica y relacional-ambiental. VERDADERO
Dentro de la depresión, la intervención más adecuada es unimodal. FALSO (Multimodal)
El objetivo principal de la intervención educativa en la depresión es acortar el periodo de tiempo que dura el trastorno y reducir las consecuencias negativas. VERDADERO
La deprivación cultural es un conjunto de experiencias adecuadas y apropiadas de carácter interpersonal, ambiental, social, educacional y sociocultural. FALSO (es la falta de experiencias adecuadas)
En relación con las DDAA, la deprivación sociocultural hace referencia a detectar en el ámbito escolar, necesidades educativas especiales asociadas a factores de salud e higiene, familiares, económicos y socioculturales, por ser los que obstaculizan el normal desarrollo cognitivo, físico y emocional del niño. VERDADERO
La deprivación sociocultural es la falta o escasez de experiencias adecuadas y apropiadas de carácter interpersonal, ambiental, social, educacional y sociocultural. FALSO (Deprivación cultural)
La deprivación sociocultural crea necesidades educativas especiales asociadas a factores de salud e higiene, familiares, económicos y/o socioculturales. FALSO
La clase social deprivada utiliza, indistintamente, el código lingüístico elaborado y el restringido. FALSO (la clase social baja no tiene acceso al código elaborado y se centra en el restringido)
La clase social deprivada tiene dificultades en el acceso al código lingüístico elaborado y no se limita al uso del código restringido. FALSO (sí se limita)
La calidad de la comunicación entre madre e hijo difiere entre las distintas clases sociales. VERDADERO
Entre los factores socioculturales relacionados con el rendimiento escolar está el nivel socioeconómico y CI, indicando que la desventaja intelectual de alumnos de ambientes socioeconómicos deprivados comienza en la etapa adolescente debido a la escasez de experiencias necesarias previas para el desarrollo óptimo de aptitudes lingüísticas y cognsocitivas. FALSO (empiezan en las etapas preescolares)
Una medida de actuación de la normativa española para la atención de estudiantes inmigrantes es la creación de planes de compensación educativa. VERDADERO
Ramírez y Justicia señalan que los problemas de convivencia más frecuentes en los centros escolares son, en mayor grado, las conductas agresivas hacia los profesores y las conductas exhibicionista y groseras. FALSO (en menor grado)
Los factores que marcan la existencia de un trastorno clínico son la edad, la intensidad de las conductas y el nivel económico. FALSO (edad, frecuencia e intensidad)
Las conductas disruptivas en el aula son acciones de baja intensidad que un alumno o grupo de alumnos protagonizan y que impiden el normal desarrollo de la clase. VERDADERO
Los equipos de orientación del centro no son los encargados de tomar medidas para eliminar las conductas disruptivas que se dan en el centro, son los profesores. FALSO
Mantener el contacto visual, usar los nombres propios y emplear el “nosotros” supone unas pautas de intervención psicoeducativa en el aula. VERDADERO
La crisis de la terquedad es a los 2 años y medio. VERDADERO
Las conductas agresivas tienden a disminuir hacia los 4-5 años. VERDADERO
Para una evaluación formal de conductas agresivas es necesario una entrevista, observación y pasar cuestionarios a padres y profesores. VERDADERO
Las estrategias de intervención sobre conductas de desobediencia y agresividad en el aula son de tipo conductual u operante que implican medidas de reforzamiento positivo (posibilidad de escape de consecuencias aversivas) y de reforzamiento negativo (eliminar Cdta inadecuadas), entre otras. FALSO (positivo y negativo al revés).
Las estrategias de intervención sobre conductas de desobediencia y agresividad en el aula son de tipo conductual y operante que implican medidas de reforzamiento positivo (posibilidad de escape de consecuencias aversivas) y de reforzamiento negativo (eliminar conductas inadecuadas) entre otras. FALSO (Positivo = premiar conductas adecuadas, y negativo, escape de consecuencias aversivas)
El desequilibrio de fuerzas entre adversarios que se da en el bullying se debe únicamente a razones físicas. FALSO (psicológicas y número de adversarios).
En referencia a las características del bullying, el desequilibrio de poder entre adversarios puede deberse a razones físicas, entre otras. VERDADERO
El bullying o acoso escolar implica sólo las agresiones dentro de la escuela. FALSO
Tres características básicas del bullying son la intencionalidad del agresor, el desequilibrio
de poder y la estabilidad en el tiempo. VERDADERO
Los resultados de múltiples investigaciones internacionales sobre el bullying, muestran que los alumnos que son agredidos en el camino de ida y vuelta al colegio, también lo son en el propio centro. VERDADERO
Olweus añade una cuarta característica básica del bullying que cuenta con gran consenso entre autores, y es que el agresor disfruta con el sufrimiento ajeno, es decir, no hay justificación alguna. FALSO (no hay consenso entre autores)
Las tres características básicas del bullying son intencionalidad del agresor, estabilidad en el tiempo y disfrutar con el sufrimiento ajeno. FALSO (disfrutar en la cuarta añadida por Olweus)
En el bullying, los programas de intervención en la escuela deben implicar la disminución del control de los espacios de la escuela. FALSO (deben implicar el aumento)
El nivel social-cultural de la familia representa un factor decisivo en la inadaptación del niño a la escuela. VERDADERO
Una de las actuaciones más relevantes en alumnos emigrantes es la generalización de los procesos de enseñanza. FALSO (Es la personalización)
Los diferentes patrones afectivos y de transmisión de la información madre-padre/hijos no tiene repercusión en el desarrollo global del sujeto. FALSO (sí tiene repercusión)
En cuanto a las DAM, en los cálculos aproximados se observa una mayor activación de las áreas cerebrales involucradas en el lenguaje, mientras que en el cálculo exacto se activa más el lóbulo parietal de los dos hemisferios. FALSO (es al revés)
Las conductas disociales graves (robos con enfrentamiento o destrozos), no siempre serán consideradas objeto de intervención desde el primer momento. FALSO (Siempre)
El EPQ-J sirve como instrumento para evaluar la ansiedad de separación en niños. VERDADERO
Las estrategias de evaluación formal (de conflicto y agresión en el aula) incluyen la intervención, la observación en situaciones naturales y/o artificiales y cuestionarios para padres y profesores. FALSO (no es la intervención, es la entrevista)
Actualmente, los estudios indican correlación significativa directa entre la ocupación paterna y el CI de los niños, únicamente. FALSO (es anteriormente, no actualmente)
Los trastornos de conducta y depresión suponen psicopatologías asociadas a trastornos del desarrollo. VERDADERO
La inmigración constituye uno de los actuales fenómenos sociales, culturales y económicos de mayor trascendencia. VERDADERO
Dentro de los desórdenes de ansiedad en la edad escolar, destacan como más representativos los trastornos de ansiedad generalizada y la fobia escolar. FALSO (ansiedad ante la separación).
En las clases media alta existe una mayor preferencia hacia el futuro, son más capaces de posponer premios y castigos simbólicos. VERDADERO
En general, la intervención con mayor apoyo empírico en el tratamiento de la fobia escolar es la de corte cognitivo -conductual que incluye técnicas de relajación, imágenes visuales, declaraciones autoafirmativas y autoinstrucciones, identificación de cogniciones erróneas y sustitución por pensamientos adaptativos. VERDADERO
La ansiedad es más frecuente en niños que en niñas. FALSO (es más frecuente en niñas)
Muchas capacidades cognitivas se encuentran en el cromosoma Y, por lo que hay mayor probabilidad de heredar la inteligencia del padre. FALSO (en el cromosoma X de la madre)
Estudios genéticos recientes han revelado que muchas capacidades cognitivas se ubican en el cromosoma Y. FALSO (Cromosoma X)
"""
]

data = []


def regex_questions(texto):
    questions_by_tema = []
    for tema in texto:
        # Split the text into individual questions
        questions = re.split(r'\n', tema)
        print(questions[:3])
        questions_by_tema.append(questions)
    return questions_by_tema



def read_questions(questions_by_tema, question_pk, response_pk, tema):
    for question in questions_by_tema:
        texto = question.replace('\n', ' ')
        if len(texto) < 2:
            continue
        texto = texto[:texto.find('VERDADERO')]
        texto = texto[:texto.find('FALSO')]
        question_data = {
            "model": "examenes.pregunta",
            "pk": question_pk,
            "fields": {
                "tema": tema,  # ID del tema al que pertenecen las preguntas
                "texto": texto
            }
        }
        data.append(question_data)

        for option_text in ("VERDADERO", "FALSO"):
            response_data = {
                "model": "examenes.opcionderespuesta",
                "pk": response_pk,
                "fields": {
                    "pregunta": question_pk,
                    "texto": str.capitalize(f'{option_text}'),
                    "es_correcta": option_text in question
                }
            }
            data.append(response_data)
            response_pk += 1

        question_pk += 1

    return data, response_pk, question_pk

def export_questions(q_data):
    # Output the JSON to a file
    with open('q_eidda_extended.json', 'w') as f:
        json.dump(q_data, f, ensure_ascii=False, indent=4)


qs = regex_questions(text)

# Start the question IDs from 89 as requested
question_pk = 180
response_pk = 463
# Datos iniciales para Curso y Tema
temas_pk = [2, 9, 10, 11, 12]

for idx, q_by_tema in enumerate(qs):
    data, question_pk, response_pk = read_questions(q_by_tema, question_pk, response_pk, temas_pk[idx])


# muestra = json.dumps(data[:10], indent=2)
# print(muestra)
export_questions(data)