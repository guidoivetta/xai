# Prompt: PDF → Beamer Slides (Pandoc-Markdown)

Convierte los PDFs proporcionados en slides Beamer usando Markdown-Pandoc. Puedes proporcionar múltiples PDFs y generaré slides separadas para cada uno.

## Para cada PDF nuevo:

1. **Indica el número de PDF**: "PDF #1", "PDF #2", etc.
2. **Proporciona el documento**
3. **Recibirás slides independientes** con nombre sugerido del archivo

---

## Formato YAML (header):
```yaml
---
title: ""
title: "\\emoji{wtf} XAI: [Título del PDF]"
bibliography: references.bib

---
```

## Reglas esenciales:

**Estructura:**
- Separar slides con `---`
- Títulos de slides con `#` (nivel 1)
- Secciones: `# Nombre` seguido de `---`
- Subtítulos dentro de slide con `##`

**Imágenes:**
```markdown
<!-- \includegraphics[width=0.8\columnwidth]{imgs/nombre.png} -->
```

**Bloques:**
```latex
\begin{alertblock}{Título}
Contenido importante
\end{alertblock}

\begin{exampleblock}{Título}
Ejemplos
\end{exampleblock}
```

**Columnas:**
```latex
\begin{columns}
\begin{column}{0.5\textwidth}
Izquierda
\end{column}
\begin{column}{0.5\textwidth}
Derecha
\end{column}
\end{columns}
```

**Contenido:**
- Máximo 6-8 puntos por slide
- Una idea principal por slide
- Usa viñetas (`-`) y numeración (`1.`)
- `**negrita**`, `*cursiva*`, `` `código` ``
- Espaciado: `\vspace{1cm}`
- Tablas markdown estándar

## Estructura típica:
```markdown
---
[YAML header]
---

# Introducción

---

# Título Slide 1

Contenido...

---

# Sección Principal

---

# Título Slide 2

## Subtítulo

- Punto 1
- Punto 2

<!-- \includegraphics[width=0.7\columnwidth]{imgs/figura.png} -->

---

# Conclusión

---

\begin{center}
\Huge Thank You!
\end{center}
```

**CRÍTICO:**
- Todas las imágenes en `imgs/`
- Separar CADA slide con `---`
- Títulos con `#` (nivel 1)
- No alteres el contenido de las slides, que sean todas iguales.
- Mostrame el codigo en un visor de codigo markdown (artefacto)
- La primer slides tiene que ser exactamente:

    ```markdow
    ---

    # Disclaimer

    \input{../disclaimer.tex}

    ---
    ```