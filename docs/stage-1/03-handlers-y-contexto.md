# 03 — Firma de handlers y contexto de request

## Qué es

Decidir qué recibe y qué devuelve una función que atiende una ruta. Es la parte de la API que el usuario más va a escribir, así que define cómo "se siente" el framework.

## Cómo lo resuelve NestJS

Los métodos del controller reciben parámetros decorados (`@Param('id')`, `@Body() dto`) y devuelven un valor que Nest serializa a JSON. Si lanzan una excepción, Nest la convierte en respuesta de error.

## Cómo podría verse en Go

Algunas opciones a comparar:

```go
// A) stdlib pura
func (c *TaskController) Get(w http.ResponseWriter, r *http.Request)

// B) contexto propio + error
func (c *TaskController) Get(ctx *gonext.Context) error

// C) genéricos: tipos de entrada y salida
func (c *TaskController) Get(ctx *gonext.Context, in GetTaskInput) (Task, error)
```

La opción B es la más común en frameworks Go (echo, fiber). Devolver `error` permite centralizar el manejo de errores (ver item 09).

## Preguntas abiertas

- ¿`gonext.Context` envuelve `http.ResponseWriter` y `*http.Request` o los expone tal cual?
- ¿Cómo se relaciona con `context.Context` de la stdlib (cancelación, deadlines)?
- ¿Se puede seguir usando un `http.HandlerFunc` común cuando haga falta?
- ¿Vale la pena la opción con genéricos en la Stage 1 o se deja para después?

## Para investigar

- Paquete `context` y el patrón `r.Context()`.
- Firma de handlers en echo (`echo.Context`), gin, fiber y huma.
- Por qué guardar `context.Context` dentro de un struct suele desaconsejarse.
- Genéricos en Go: límites (no hay métodos genéricos) y cómo afectan esta API.

## Definición de hecho

- Hay una firma de handler elegida con ejemplos.
- Se puede leer path params, query params y el body JSON desde el contexto.

## Notas

<!-- Completar a medida que se investiga -->
