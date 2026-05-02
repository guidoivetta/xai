# 🎓 Práctico: Preparación y Dictado de una Clase

## 🎯 Objetivo

El objetivo de este práctico es que prepares y dictes una clase del curso XAI, siguiendo al menos el estilo y la calidad de las *lectures* ya presentadas.

Has seleccionado un par de papers académicos y un **prototipo de slides** generado a partir del material original del curso de Harvard. Tu tarea es **mejorar ese prototipo** hasta llevar las slides a un nivel comparable al de las lectures del curso (ver, por ejemplo,
https://github.com/leliel12/xai/tree/2026/slides/lecture11/slides.md).

[Podés ver aquí la asignación de temas](https://docs.google.com/spreadsheets/d/e/2PACX-1vSPAs_Tdn1nxw0LGIlhWDOMMj95nz6uqLFl4I6aSulpInwE0voiScitNpgOCSixz9MWDvK4lvZ9gh5m/pubhtml?gid=0&single=true).


---

## 📦 Entregables

- Slides finales en formato Markdown (archivo `slides.md`) junto con el PDF compilado.
- Las slides son en inglés.
- Dictado de la clase frente al curso (duración: <= 2:30).
- Se espera que el doctorando realice un fork del repositorio del curso y **antes** de la clase realice un [pull-request](https://github.blog/developer-skills/github/beginners-guide-to-github-creating-a-pull-request/) con los cambios de su *lecture*



---

## 🆘 ¿Qué pasa si no puedo compilar o no sé cómo hacer algo?

1. Tu responsable directo es el doctorando que dio la clase inmediatamente anterior.
2. Canal de #XAi Zulip.
3. Recordar que son doctorandos y buscarle la vuelta.

---

## 🗂️ Estructura esperada de las slides

Cada lecture del curso sigue una estructura de carpeta como esta:

```
slides/lectureXX/
├── slides.md        ← fuente Markdown/LaTeX
├── slides.pdf       ← PDF compilado
├── references.bib   ← referencias bibliográficas
└── imgs/            ← imágenes usadas en las slides
```

Las slides se escriben en **Markdown con LaTeX embebido** para fórmulas. Cada slide se separa con `---`. El encabezado del archivo tiene el siguiente formato YAML:

```markdown
---
title: "XAI Lecture XX"
subtitle: "Título de la clase"
bibliography: references.bib
---
```

Consulta `slides/lecture11/slides.md` como referencia de una slide prototípica: verás la estructura general, el uso de columnas (`\begin{columns}`), bloques (`\begin{block}`, `\begin{alertblock}`), fórmulas LaTeX, y figuras.

---

## ⚙️ Cómo compilar las slides: tutorial de `make.py`

Las slides se compilan con **Pandoc** usando el script `slides/make.py`. El script convierte el archivo `slides.md` en un PDF de presentación tipo Beamer.

### 📥 Instalación de dependencias

```bash
pip install watchdog sh
```

También necesitás tener **Pandoc** instalado con soporte para `pandoc-citeproc` (En Debian/Ubuntu/Mint lo instalé con `apt`).

### ▶️ Compilación única

Desde la carpeta `slides/`, ejecutá:

```bash
python make.py lectureXX/slides.md
```

Esto genera `lectureXX/slides.pdf`.

### 👁️ Modo watch (recompilación automática)

Para que el PDF se recompile automáticamente cada vez que guardás cambios en las slides, imágenes o bibliografía:

```bash
python make.py lectureXX/slides.md --watch
```

El modo watch detecta cambios en:

- `slides.md`
- `references.bib`
- la carpeta `imgs/` (adentro tiene un archivo `images.md` que lista las imágenes a conseguir: nombre de archivo, página del PDF original y descripción del contenido)
- los archivos compartidos `defaults.yaml` y `disclaimer.tex` (no tocar estos dos archivos)

Podés detenerlo con `Ctrl+C`.

### 🔤 Caracteres especiales

El script reemplaza automáticamente algunos caracteres Unicode por sus equivalentes LaTeX (por ejemplo, `λ` → `$\lambda$`), por lo que podés escribirlos directamente en el Markdown, pero recomiendo usar directamente latex `$\lambda$`

---

## 🧰 Herramientas de ayuda

En el repositorio se encuentran:

- Todos los slides de las clases anteriores: https://github.com/leliel12/xai/tree/2026/slides/
- Las slides originales del curso de Harvard: https://github.com/leliel12/xai/tree/2026/slides/original_pptx ([y sus versiones en PDF](https://github.com/leliel12/xai/tree/2026/slides/original_pdf))
- Las imágenes van a tener que sacarlas de las slides originales y probablemente
  editarlas un poco. Todas las imágenes del draft del slide son placeholders.


### 🤖 Prompt `slides_adapter.md`

Para ayudarte a entender los papers y mejorar las slides, tenés disponible el archivo [slides_adapter.md](slides_adapter.md). Este es un **prompt de sistema** diseñado para usar con un asistente de IA (como Claude).

Cargando ese prompt en una conversación junto con los PDFs de los papers y el prototipo de slides, podés:

- 💬 Hacer preguntas sobre conceptos, fórmulas e ideas de los papers.
- 📖 Pedir explicaciones en lenguaje llano de resultados técnicos.
- ✏️ Generar o mejorar slides directamente a partir de la discusión.
- 🔁 Iterar sobre el contenido hasta alcanzar el nivel de calidad esperado.

El prompt incluye instrucciones de estilo y formato para que las slides generadas sean consistentes con el resto del curso.

---

## 📊 Criterios de evaluación

- 📄 **Fidelidad al paper:** las slides reflejan correctamente los aportes, métodos y resultados.
- 🧠 **Calidad didáctica:** las ideas complejas están explicadas de forma clara y progresiva.
- 🎨 **Calidad visual:** las slides son limpias, bien estructuradas y consistentes con el estilo del curso.
- 🗣️ **Presentación oral:** el dictado es fluido, cubre los puntos clave y promueve la discusión.

Se dará una devolución en formato escrito de la clase.

⚠️ En caso de no estar a la altura, el docente podrá dar por terminada la clase, y solicitar un práctico extra al alumno al momento de rendir el final.
