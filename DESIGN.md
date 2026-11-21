---
name: GoNext
description: Framework web para Go; su identidad visual es una sesión de terminal dibujada sobre una grilla de celdas.
colors:
  graphite: "#16181d"
  graphite-edge: "#2b2f37"
  graphite-seam: "#2a2e35"
  graphite-cell: "#1e2127"
  bone-ink: "#e6e1d6"
  comment-gray: "#868e9b"
  go-cyan: "#00add8"
  status-amber: "#e0a84f"
  paper: "#f6f4ef"
  paper-edge: "#d9d4c8"
  paper-seam: "#e0dbd0"
  paper-cell: "#ebe7de"
  carbon-ink: "#1d2026"
  comment-slate: "#5b6270"
  go-cyan-deep: "#006f91"
  status-amber-deep: "#8a560a"
typography:
  body:
    fontFamily: "Martian Mono, ui-monospace, Menlo, Consolas, monospace"
    fontSize: "14.2857px"
    fontWeight: 400
    lineHeight: "22px"
    letterSpacing: "normal"
    fontVariation: "'wdth' 100"
  title:
    fontFamily: "Martian Mono, ui-monospace, Menlo, Consolas, monospace"
    fontSize: "14.2857px"
    fontWeight: 700
    lineHeight: "22px"
    letterSpacing: "normal"
    fontVariation: "'wdth' 100"
rounded:
  none: "0px"
  frame: "10px"
spacing:
  cell: "10px"
  row: "22px"
  margin: "40px"
  node: "12px"
components:
  frame-dark:
    backgroundColor: "{colors.graphite}"
    textColor: "{colors.bone-ink}"
    rounded: "{rounded.frame}"
  frame-light:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.carbon-ink}"
    rounded: "{rounded.frame}"
  wordmark-cell:
    backgroundColor: "{colors.bone-ink}"
    rounded: "{rounded.none}"
    width: "18px"
    height: "20px"
  wordmark-cell-go:
    backgroundColor: "{colors.go-cyan}"
    rounded: "{rounded.none}"
    width: "18px"
    height: "20px"
  wordmark-cell-ghost:
    backgroundColor: "{colors.graphite-cell}"
    rounded: "{rounded.none}"
    width: "18px"
    height: "20px"
  node-framework:
    backgroundColor: "{colors.graphite}"
    rounded: "{rounded.none}"
    size: "{spacing.node}"
  node-own:
    backgroundColor: "{colors.bone-ink}"
    rounded: "{rounded.none}"
    size: "{spacing.node}"
  cursor:
    backgroundColor: "{colors.go-cyan}"
    rounded: "{rounded.none}"
    width: "{spacing.cell}"
    height: "16px"
  status-label:
    textColor: "{colors.status-amber}"
    typography: "{typography.title}"
---

# Design System: GoNext

## Overview

**Creative North Star: "La sesión de terminal"**

GoNext se presenta como una terminal que trabaja: un prompt que instala, un árbol de archivos, un log de arranque que resuelve módulos y mapea rutas, un cursor que queda parpadeando. Todo lo que se dibuja (wordmark, uniones del árbol, nodos del ciclo de vida, cursor) es geometría sobre una grilla de celdas de 10 × 22 px, la misma unidad que ocupa un carácter monoespaciado. No hay ilustración, íconos ni gradientes: la imagen es el texto y las celdas.

La densidad es la de una consola: una sola talla tipográfica, filas a 22 px, columnas a 10 px, márgenes de 4 columnas. La jerarquía se construye con peso (400/700) y con rol de color, no con tamaños; la única excepción de escala es el wordmark, que está hecho de celdas sólidas y no de tipografía. El color tiene semántica estricta: el cian pertenece a Go y a lo ejecutable, el ámbar al estado, el gris al comentario.

Cada pieza existe en dos materiales, grafito y papel, que se sirven según `prefers-color-scheme`, y en dos anchos (960 px y 480 px). El movimiento es una sola firma: la sesión se escribe una vez, en orden, y queda el cursor; con `prefers-reduced-motion` todo aparece quieto y completo.

**Key Characteristics:**
- Grilla de celdas 10 × 22 px como unidad de todo: texto, wordmark, márgenes y nodos.
- Una sola fuente (Martian Mono, embebida), una sola talla; jerarquía por peso y color.
- Color semántico: cian = Go y lo ejecutable, ámbar = estado, gris = comentario, tinta = contenido.
- Formas dibujadas, nunca glifos: uniones de árbol, nodos y cursor son trazos y rectángulos.
- Dos materiales (grafito / papel) y dos anchos (960 / 480) por cada pieza.

## Colors

Dos materiales neutros cálidos con tres voces de rol: tinta para el contenido, cian Go para lo ejecutable y ámbar para el estado.

### Primary
- **Cian Go** (go-cyan en grafito, go-cyan-deep en papel): comandos (`go get`, `go run`), métodos HTTP, rutas, parámetros como `{id}`, la mitad GO del wordmark y el cursor. Nunca decorativo y nunca para estado.

### Secondary
- **Ámbar de estado** (status-amber en grafito, status-amber-deep en papel): todo lo que dice "en qué estado está esto": "API en diseño", "diseño propuesto", "etapa 2", "resuelto", códigos de respuesta (`200`, `403`) y la rama de rechazo del guard.

### Neutral
- **Grafito** (graphite) / **Papel** (paper): fondo del marco en cada tema.
- **Tinta hueso** (bone-ink) / **Tinta carbón** (carbon-ink): texto de contenido, píxeles del wordmark que no son GO, nodos "tu código" y contorno de nodos.
- **Gris de comentario** (comment-gray) / **Pizarra de comentario** (comment-slate): comentarios `# ...`, el prompt `$`, el prefijo `gonext` del log, flechas, tipos de la columna derecha, trazos del árbol y del eje.
- **Borde** (graphite-edge / paper-edge): contorno de 1 px del marco.
- **Costura** (graphite-seam / paper-seam): divisores de 1 px que separan barra de título, cuerpo y pie.
- **Celda fantasma** (graphite-cell / paper-cell): celdas apagadas del wordmark; muestran la grilla sin competir con el texto.

### Named Rules
**The Go Owns Cyan Rule.** El cian marca solo lo que pertenece a Go o se ejecuta: comandos, métodos, rutas, la mitad GO del wordmark y el cursor. Si no se puede tipear o ejecutar, no es cian.

**The Amber Is State Rule.** El ámbar marca estado (propuesto, etapa 2, resuelto, código HTTP, rechazo). Nunca se usa para énfasis general.

**The Two Materials Rule.** Cada color de rol existe en par grafito/papel y cada par supera 5:1 contra su fondo; un color nuevo entra con su par o no entra.

## Typography

**Body Font:** Martian Mono (con ui-monospace, Menlo, Consolas, monospace)

**Character:** Una monoespaciada técnica, de avance 0.7 em, instanciada en wdth 100 y en dos pesos, recortada a ASCII más los acentos del español y embebida como woff2 en cada SVG para que GitHub la muestre igual en cualquier equipo.

### Hierarchy
- **Title** (700, 14.2857 px, 22 px): nombres de etapa del ciclo de vida, directorios del árbol, comandos, la primera frase del tagline, valores clave como `:8080` y etiquetas de estado.
- **Body** (400, 14.2857 px, 22 px): todo lo demás: log, descripciones, comentarios, tipos.

### Named Rules
**The One Size Rule.** El texto tiene una sola talla, calibrada para que un carácter mida exactamente una celda (10 px). La jerarquía sale del peso y del rol de color; la escala grande pertenece solo al wordmark de celdas.

**The Wordmark Is Cells Rule.** GONEXT se compone con píxeles de una matriz 5 × 7 por letra sobre celdas fantasma, nunca con una fuente display.

## Layout

Todo se posiciona en coordenadas de la grilla: columna × 10 px, fila × 22 px, con la línea base 15 px dentro de la fila. Los marcos anchos miden 96 columnas (960 px) y los angostos 48 (480 px), ambos con margen izquierdo de 4 columnas (40 px). Los bloques se separan con medias filas o fracciones de fila (1.2, 1.5, 1.8), no con espaciados libres.

El banner se ordena como una ventana de terminal: barra de título (ruta a la izquierda, estado a la derecha), costura, prompt, wordmark, tagline, costura, cuerpo y pie con comentario. En ancho, el cuerpo se parte en dos columnas (árbol desde la columna 4, log desde la 36) separadas por una costura vertical en la columna 33; en angosto se apilan.

El ciclo de vida es un único eje vertical: nodos sobre la columna del eje, nombre de etapa a 3 columnas, descripción a 17 y el tipo alineado a la derecha del margen. En angosto el nombre y la descripción se apilan en dos filas y la columna de tipos desaparece.

El README elige la variante con `<picture>`: `max-width: 600px` sirve la angosta y `prefers-color-scheme: dark` el grafito.

## Elevation & Depth

Sistema plano. No hay sombras ni capas tonales superpuestas: la profundidad se expresa con costuras de 1 px, el borde de 1 px del marco y el contraste entre celda fantasma y fondo.

**The Flat Terminal Rule.** Nada flota. Las separaciones son costuras sobre la grilla, nunca sombras.

## Shapes

Rectángulos rectos en todas partes; la única curva es el radio del marco exterior (rounded.frame), que lo lee como ventana. Píxeles del wordmark, nodos y cursor son cuadrados o rectángulos sin radio. Los trazos se dibujan a 1 px (costuras, uniones del árbol), 1.5 px (rama de error, discontinua 3 3) y 2 px (eje y contorno de nodos). Lo que todavía no existe se dibuja discontinuo (2 2), lo que es error discontinuo y en ámbar.

## Components

### Marco de terminal
- **Forma:** rectángulo con radio de ventana (rounded.frame) y borde de 1 px en el color de borde del tema.
- **Interior:** barra de título de una fila con ruta en gris a la izquierda y estado en ámbar bold a la derecha, costuras horizontales entre zonas y un pie con un comentario `#`.

### Wordmark de celdas
- **Construcción:** cada letra es una matriz 5 × 7. En ancho cada píxel ocupa 2 × 1 celdas; en angosto 1 × 0.5. Entre letras quedan 2 columnas. Cada píxel deja 1 px de aire por lado.
- **Color:** G y O en cian, NEXT en tinta, celdas apagadas en celda fantasma.
- **Movimiento:** las celdas caen 3 px y aparecen fila por fila (0.35 s, cubic-bezier(.16,1,.3,1)).

### Línea de sesión
- **Estructura:** segmentos de texto con rol: `$` y prefijos en gris, comando en cian bold, argumentos en tinta, resultados de estado en ámbar, flechas `→` en gris.
- **Cursor:** bloque cian de 1 celda de ancho por 16 px de alto, en su propia fila, parpadea cada 1.1 s una vez terminada la sesión.

### Árbol de archivos
- **Estructura:** sangría de 3 columnas por nivel; directorios en bold.
- **Uniones:** trazos de 1 px en gris dibujados como paths, nunca caracteres de caja.

### Nodo del ciclo de vida
- **Framework:** cuadrado de 12 px, relleno de fondo, contorno de tinta de 2 px.
- **Tu código:** mismo cuadrado relleno de tinta.
- **Más adelante:** contorno gris discontinuo (2 2), acompañado de la etiqueta ámbar "etapa 2".
- **Leyenda:** usa los mismos nodos dibujados que el eje.

### Rama de rechazo
- Línea horizontal ámbar discontinua (1.5 px, 3 3) que sale del eje bajo el guard, seguida del código en ámbar bold y la explicación en gris.

## Do's and Don'ts

### Do:
- **Do** posicionar todo en múltiplos de la celda (10 px) y la fila (22 px), con margen de 4 columnas.
- **Do** reservar el cian para comandos, métodos HTTP, rutas, la mitad GO del wordmark y el cursor.
- **Do** marcar con ámbar todo lo propuesto, pendiente o de estado ("API en diseño", "diseño propuesto", "etapa 2").
- **Do** dibujar uniones, nodos, ejes y cursor como trazos y rectángulos SVG.
- **Do** entregar cada pieza en grafito y papel, y en 960 px y 480 px, servidas con `<picture>`.
- **Do** embeber Martian Mono como woff2 recortado en cada SVG y respetar `prefers-reduced-motion` mostrando todo quieto y completo.
- **Do** escribir la sesión una sola vez y en orden; el único movimiento que se repite es el parpadeo del cursor.

### Don't:
- **Don't** usar íconos, emojis ni glifos decorativos; los nodos y uniones se dibujan.
- **Don't** usar caracteres de dibujo de caja (`├──`) dentro de los SVG; las uniones son paths.
- **Don't** agregar tallas tipográficas: la escala grande es solo el wordmark de celdas.
- **Don't** usar gradientes, sombras ni logos centrados con fila de badges.
- **Don't** usar cian o ámbar como acento decorativo fuera de sus roles.
- **Don't** repetir animaciones en bucle fuera del cursor.
