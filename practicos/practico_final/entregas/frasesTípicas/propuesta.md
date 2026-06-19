# Interpretación de lenguaje regional en LLMs
# Análisis de dependencia contextual mediante explicaciones post-hoc

## Integrantes
- Ivetta, Guido 
- Martinelli, Sofía

---

## Preguntas de investigación

1. ¿Qué partes del input contribuyen más a la respuesta del modelo al interpretar expresiones culturales o regionales?
2. ¿Los LLMs logran definir correctamente el slang estadounidense incluso sin contexto adicional, mientras que fallan sistemáticamente con regionalismos argentinos en la misma condición?
3. ¿El agregado del ejemplo de uso incrementa significativamente la accuracy del modelo en regionalismos argentinos, pero no así en slang estadounidense?

## Hipótesis

**H1 — Accuracy diferencial sin contexto:** Los LLMs alcanzarán una alta accuracy al definir slang estadounidense en la condición *sin contexto*, mientras que mostrarán una accuracy significativamente menor para regionalismos argentinos en la misma condición. Esto reflejaría la subrepresentación del español regional rioplatense/cordobés en los datos de entrenamiento respecto del slang estadounidense [4].

**H2 — Impacto del contexto:** El agregado del ejemplo de uso producirá una mejora en la accuracy para regionalismos argentinos, pero solo una mejora marginal (o nula) para el slang estadounidense, donde el modelo ya contaba con suficiente conocimiento interno.

**H3 — Atribución SHAP diferencial:** Las explicaciones post-hoc (SHAP [2, 3]) mostrarán que el token correspondiente al ejemplo de uso recibe un peso de atribución mayor en las expresiones argentinas que en el slang estadounidense, siendo coherente con la dependencia contextual observada en la accuracy. En la condición sin contexto, SHAP debería indicar que prácticamente toda la señal recae sobre la expresión misma.

## Datos

Se utilizará un dataset de frases regionales del español de Argentina y de slang del inglés estadounidense [1], compuesto por:
- expresión regional o slang
- definición
- ejemplo de uso

### Recolección y anotación

La recolección de datos del corpus de regionalismos argentinos fue realizada a través de la interfaz **EDIA** [5, 6, 7], con la participación de más de **800 ingresantes de FAMAF** (UNC), quienes contribuyeron con expresiones, definiciones y ejemplos propios de sus provincias.

Durante los meses de mayo, junio y julio de 2026, el dataset se amplía y enriquece con las contribuciones de más de **1.500 docentes de nivel secundario de la provincia de Córdoba**. Esta etapa de anotación masiva se desarrolla en el marco de un **curso de desarrollo profesional docente** oficialmente reconocido por el **Ministerio de Educación de la Provincia de Córdoba**, lo que garantiza cobertura geográfica y sociocultural amplia dentro de la provincia. Esta metodología de recolección comunitaria con docentes en ejercicio fue validada previamente en los proyectos HESEIA [5] y LACES [6], que comparten la misma plataforma e infraestructura de anotación.

Esta escala de participación posiciona al corpus como un recurso de anotación colaborativa a gran escala, con representatividad regional, lo que lo diferencia sustancialmente de datasets construidos de forma automática o con colaboradores homogéneos.

## Propuesta Experimental

El experimento evalúa cómo los LLMs interpretan expresiones regionales y cómo varía esta interpretación en función del contexto disponible. El objetivo no es evaluar directamente la calidad del texto generado, sino estudiar los mecanismos internos de decisión de los LLMs al generar interpretaciones de lenguaje no estándar, a través de explicaciones post-hoc sobre sus salidas.

Para cada expresión (regionalismos argentinos y slang estadounidense), se construyen dos condiciones experimentales:

### Sin contexto: 
```text
¿Qué significa la siguiente expresión?
Expresión: {frase}
Responde con una definición breve.
```

### Con contexto: 
```text
¿Qué significa la siguiente expresión?
Expresión: {frase}
Ejemplo de uso: {ejemplo}
Responde con una definición breve.
```

Los modelos generan una definición libre para cada input.

### Evaluación de accuracy

Las respuestas son evaluadas manualmente en un subconjunto del dataset, clasificándolas como *correcta*, *parcialmente correcta* o *incorrecta*. Este ground truth externo es factible de construir gracias a las definiciones y ejemplos anotados colaborativamente por nuestra gran cantidad de anotadores, lo que permite contar con múltiples validaciones por expresión. Se calculará la accuracy por condición (con/sin contexto) y por idioma (argentino/estadounidense), con el objetivo de verificar **H1** y **H2**: se espera observar alta accuracy para slang estadounidense en ambas condiciones, y baja accuracy para regionalismos argentinos en la condición sin contexto, con una recuperación notable al agregar el ejemplo de uso.

### Explicaciones post-hoc con SHAP

SHAP [2, 3] se aplica para cuantificar la contribución de cada segmento del input (la expresión y el ejemplo de uso) a la salida del modelo. El análisis se realiza por separado para cada condición y grupo lingüístico, permitiendo:

- **Atribución por componente:** determinar qué fracción del valor SHAP total corresponde al token de la expresión vs. al ejemplo de uso, en cada condición.
- **Contraste entre grupos:** comparar si el peso SHAP del ejemplo de uso es significativamente mayor en regionalismos argentinos que en slang estadounidense (verificación de **H3**).
- **Consistencia:** evaluar si los patrones de atribución son robustos entre distintos modelos evaluados.

La conjunción del análisis de accuracy y el análisis SHAP permite no solo medir *si* el modelo falla, sino también *por qué*: si la baja accuracy sin contexto en expresiones argentinas se corresponde con valores SHAP bajos en la expresión y altos en el ejemplo de uso cuando éste está disponible, la evidencia confirma una dependencia contextual estructural y no un error aleatorio.

Dado que los modelos evaluados generan definiciones en texto libre, es necesario transformar sus respuestas en un valor numérico para poder aplicar SHAP. Para cada expresión, el modelo genera una definición y luego se calcula su similitud semántica (coseno) respecto de la definición de referencia provista por el dataset. Este valor refleja cuán cercana es la respuesta generada a la interpretación esperada. SHAP se aplica sobre esta medida de similitud para estimar la contribución de cada componente del input (la expresión y el ejemplo de uso) al aumento o disminución de la calidad de la interpretación producida por el modelo.

## Plan de actividades

| Semana | Tarea |
|---|---|
| 1 | Preprocesamiento y filtrado de los datasets. Generación de respuestas de los modelos. Evaluación manual de respuestas. |
| 2 | Implementación del pipeline experimental para la obtención de explicaciones mediante SHAP. |
| 3 | Comparación entre modelos y contextos lingüísticos. Análisis preliminar de resultados. |
| 4 | Análisis final y discusión de resultados. Escritura y revisión del paper final. |

## Limitaciones

Como limitación, las diferencias observadas entre regionalismos argentinos y slang estadounidense podrían estar influenciadas no solo por factores lingüísticos, sino también por diferencias intrínsecas entre los datasets, tales como dificultad, ambigüedad o la calidad de las definiciones de referencia. Por lo tanto, los resultados deberán interpretarse teniendo en cuenta estas posibles diferencias entre datasets.

---

## Referencias

[1] MLBtrio. (2024). *GenZ Slang Dataset* [Dataset]. Hugging Face. https://huggingface.co/datasets/MLBtrio/genz-slang-dataset

[2] Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems*, 30, 4765–4774.

[3] Kokalj, E., Robnik-Šikonja, M., Lavrač, N., Kranjc, J., & Cestnik, B. (2021). BERT meets Shapley: Extending SHAP explanations to transformer-based classifiers. *Proceedings of the EACL 2021 Workshop on Explainability for Natural Language Processing (XAI-NLP)*, 1–7.

[4] Joshi, P., Santy, S., Budhiraja, A., Bali, K., & Choudhury, M. (2020). The state and fate of linguistic diversity and inclusion in the NLP world. *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020)*, 6282–6293.

[5] Ivetta, G., Gomez, M. J., Martinelli, S., Palombini, P., Echeveste, M. E., Mazzeo, N. C., Busaniche, B., & Benotti, L. (2025). HESEIA: A community-based dataset for evaluating social biases in large language models, co-designed in real school settings in Latin America. *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025)*, 25095–25117. https://doi.org/10.18653/v1/2025.emnlp-main.1275

[6] Ivetta, G., Palombini, P., Martinelli, S., Gomez, M. J., Echeveste, M. M., Dev, S., Prabhakaran, V., & Benotti, L. (2026). Adaptive Data Collection for Latin-American Community-sourced Evaluation of Stereotypes (LACES). *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026)* (to appear). arXiv:2510.24958. https://doi.org/10.48550/arXiv.2510.24958

[7] Maina, H., Alonso Alemany, L., Ivetta, G., Rajngewerc, M., Busaniche, B., & Benotti, L. (2024). Exploring stereotypes and biases in language technologies in Latin America. *Communications of the ACM*. https://doi.org/10.1145/3653322
