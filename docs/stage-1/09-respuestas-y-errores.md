# 09 — Respuestas y manejo de errores

## Qué es

Cómo un handler devuelve datos (JSON, status code, headers) y cómo un error de negocio se convierte en una respuesta HTTP consistente. Sin esto, cada handler termina armando sus propias respuestas de error a mano.

## Cómo lo resuelve NestJS

El valor devuelto se serializa a JSON. Los errores se lanzan como excepciones (`NotFoundException`, `BadRequestException`) y un "exception filter" global las convierte en respuestas con un formato estándar.

## Cómo podría verse en Go

Go no tiene excepciones: los errores son valores. Si el handler devuelve `error` (ver item 03), el framework puede tener un único punto que decide la respuesta:

```go
var ErrTaskNotFound = gonext.NewHTTPError(http.StatusNotFound, "task not found")

func (c *TaskController) Get(ctx *gonext.Context) error {
    task, err := c.tasks.Find(ctx.Param("id"))
    if err != nil {
        return err
    }
    return ctx.JSON(http.StatusOK, task)
}
```

Con `errors.As` el handler central detecta si el error trae un status HTTP; si no, responde 500 sin filtrar detalles internos.

## Preguntas abiertas

- ¿Formato del cuerpo de error? ¿Seguir RFC 9457 (Problem Details)?
- ¿Cómo mapea un error de dominio (`task.ErrNotFound`) a HTTP sin que el dominio dependa del framework?
- ¿El usuario puede reemplazar el error handler global?
- ¿Helpers incluidos: `JSON`, `NoContent`, `Text`?

## Para investigar

- `errors.Is`, `errors.As` y wrapping con `%w`.
- RFC 9457 — Problem Details for HTTP APIs.
- `HTTPErrorHandler` en echo.
- `encoding/json`: `Encoder`, manejo de errores al escribir y `Content-Type`.

## Definición de hecho

- Los handlers devuelven `error` y existe un error handler central.
- Formato de error documentado; los errores desconocidos responden 500 sin exponer detalles.

## Notas

<!-- Completar a medida que se investiga -->
