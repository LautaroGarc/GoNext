# 08 — Middleware

## Qué es

Código que se ejecuta antes y/o después de cada handler: logging de requests, recuperación de panics, CORS, request ID. Permite resolver cosas transversales sin repetirlas en cada ruta.

## Cómo lo resuelve NestJS

Middleware compatible con Express, configurado desde el módulo con `configure(consumer)`. Además tiene guards, interceptors y pipes, que son variantes especializadas (fuera de la Stage 1).

## Cómo podría verse en Go

El patrón estándar de la comunidad Go:

```go
type Middleware func(http.Handler) http.Handler
```

Si GoNext usa esta firma, cualquier middleware existente del ecosistema (de `chi`, `gorilla/handlers`, etc.) funciona sin adaptadores. Se podría aplicar en tres niveles: global, por módulo y por controller/ruta.

## Preguntas abiertas

- ¿Firma estándar `func(http.Handler) http.Handler` o una propia basada en `gonext.Context`?
- ¿En qué niveles se puede aplicar en la Stage 1?
- ¿Qué middleware viene incluido? (candidatos: recover, request ID, logger)
- ¿Orden de ejecución cuando se combinan niveles?

## Para investigar

- El patrón de middleware en Go y el encadenamiento de handlers.
- Middleware incluido en `chi` (`middleware.Recoverer`, `RequestID`, `Logger`).
- Cómo pasar valores por `context.WithValue` sin romper tipos (claves no exportadas).
- `http.ResponseWriter` envuelto para capturar el status code.

## Definición de hecho

- Middleware global y por controller funcionando, con tests del orden.
- Middleware de recover incluido: un panic devuelve 500 en vez de tirar el proceso.

## Notas

<!-- Completar a medida que se investiga -->
