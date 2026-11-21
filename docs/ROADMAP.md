# Roadmap de GoNext

Este roadmap ordena el trabajo en etapas. Cada item tiene su propio documento con la idea, las preguntas abiertas y qué investigar. Los documentos son puntos de partida: están pensados para que se expandan a medida que se investiga y se toman decisiones.

> Estado: todo lo descrito acá es **propuesto**. Ninguna API está implementada todavía.

## Stage 1 — Núcleo del framework

Objetivo: poder escribir una API chica organizada en módulos, controllers y providers, levantarla sobre `net/http` y testearla. Sin features avanzadas: lo mínimo para que la arquitectura se sienta como GoNext.

- [ ] [01 — Estructura del repositorio y del módulo Go](stage-1/01-estructura-del-proyecto.md)
- [ ] [02 — Router sobre `net/http`](stage-1/02-router.md)
- [ ] [03 — Firma de handlers y contexto de request](stage-1/03-handlers-y-contexto.md)
- [ ] [04 — Controllers](stage-1/04-controllers.md)
- [ ] [05 — Providers e inyección de dependencias](stage-1/05-providers-y-di.md)
- [ ] [06 — Módulos (imports / exports)](stage-1/06-modulos.md)
- [ ] [07 — Bootstrap y ciclo de vida de la aplicación](stage-1/07-bootstrap-y-ciclo-de-vida.md)
- [ ] [08 — Middleware](stage-1/08-middleware.md)
- [ ] [09 — Respuestas y manejo de errores](stage-1/09-respuestas-y-errores.md)
- [ ] [10 — Configuración](stage-1/10-configuracion.md)
- [ ] [11 — Logging](stage-1/11-logging.md)
- [ ] [12 — Utilidades de testing](stage-1/12-testing.md)
- [ ] [13 — Ejemplo de referencia y README](stage-1/13-ejemplo-y-readme.md)

### Criterio de cierre de la Stage 1

- Se puede crear una app con al menos dos módulos, donde uno usa un provider exportado por el otro.
- Las rutas se registran desde controllers y se sirven con `net/http`.
- Hay un ejemplo en `examples/` que compila, corre y tiene tests.
- El README muestra la API real (ya no propuesta) de todo lo anterior.

## Stage 2 — Ideas para después (sin detallar)

Se anotan para no perderlas; no se trabajan hasta cerrar la Stage 1.

- Validación declarativa de DTOs
- Guards / autorización
- Interceptors
- CLI para generar módulos
- Integración con bases de datos
- OpenAPI / documentación automática

## Cómo usar estos documentos

Cada documento de item sigue la misma estructura:

1. **Qué es** — la idea en dos o tres líneas.
2. **Cómo lo resuelve NestJS** — la referencia de inspiración.
3. **Cómo podría verse en Go** — un boceto, no una decisión.
4. **Preguntas abiertas** — lo que hay que decidir.
5. **Para investigar** — temas, paquetes y lecturas.
6. **Definición de hecho** — cuándo se tilda en el roadmap.
7. **Notas** — espacio libre para ir completando.
