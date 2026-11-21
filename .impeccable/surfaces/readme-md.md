---
version: 1
slug: "readme-md"
primary_target: "README.md"
related_targets: []
---

# README de GitHub

Modo: Persuade. Superficie: README.md renderizado por GitHub (markdown + SVG en `assets/`, sin JS, variantes claro/oscuro vía `<picture>`).
Público: devs Go y devs que vienen de NestJS evaluando el repo. Acción: entender qué es GoNext, que está en desarrollo, y seguirlo/contribuir.
Restricciones: API mostrada = diseño propuesto, marcada como tal. Sin métricas, benchmarks ni releases inventados. Español.

## Direction contract

THESIS: El README es una sesión de terminal real de GoNext: crear, ver el árbol de módulos, levantar y ver una request mapearse. Rechaza el banner con logo centrado + gradiente + fila de badges + lista de features con emojis.
OWN-WORLD: Grafito #16181d / papel #f6f4ef, tinta #e6e1d6 / #1d2026; cian Go solo para comandos, métodos HTTP, rutas y la mitad GO del wordmark, ámbar para strings/estado "en desarrollo", gris de comentario. Martian Mono embebida. Todo alineado a una grilla de celdas 10×22. Wordmark GONEXT construido con celdas sólidas. Sin íconos ni emojis; jerarquía por tamaño y peso.
STORY: Ve en un vistazo módulo/controller/provider sobre net/http, entiende que es early-stage, lee el código propuesto, la tabla NestJS↔GoNext y el roadmap, y da estrella o contribuye.
FIRST VIEWPORT: Banner 960×565 (480×770 en la variante angosta): prompt `$ go get github.com/LautaroGarc/GoNext` (la CLI `gonext new` es etapa 2), wordmark en celdas, línea de tagline, árbol del proyecto a la izquierda y log de arranque a la derecha, comentario `# API en diseño`. Debajo: tagline en texto, navegación en texto plano, alerta de estado.
FORM: Sesión de terminal, posición 6 de 7 en la lista ordenada, seed 5b1bbd53. Firma: las líneas se escriben una vez en orden y queda un cursor parpadeando; con reduced-motion todo aparece quieto. Diagrama de ciclo de vida en un único eje vertical.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
