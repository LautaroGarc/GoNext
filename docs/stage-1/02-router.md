# 02 — Router sobre `net/http`

## Qué es

El componente que asocia un método HTTP y una ruta (`GET /tasks/{id}`) con el código que la atiende. Es el punto donde GoNext se apoya directamente en la librería estándar.

## Cómo lo resuelve NestJS

NestJS no tiene router propio: delega en Express o Fastify a través de un "platform adapter". Los decoradores `@Get()`, `@Post()` solo guardan metadata; el core la lee y registra las rutas en el adapter.

## Cómo podría verse en Go

Desde Go 1.22, `http.ServeMux` soporta métodos y parámetros en el patrón:

```go
mux := http.NewServeMux()
mux.HandleFunc("GET /tasks/{id}", func(w http.ResponseWriter, r *http.Request) {
    id := r.PathValue("id")
    // ...
})
```

GoNext podría envolver `ServeMux` en vez de escribir un router propio: agregar prefijos por controller, grupos y middleware por ruta, pero dejando que la stdlib haga el matching.

## Preguntas abiertas

- ¿Alcanza `ServeMux` o hace falta algo que no ofrece (por ejemplo, regex en parámetros)?
- ¿Cómo se manejan los prefijos de ruta por controller y por módulo?
- ¿Qué pasa con rutas en conflicto? (`ServeMux` hace panic al registrar patrones ambiguos)
- ¿Se expone el `http.Handler` final para que el usuario lo monte donde quiera?

## Para investigar

- Notas de release de Go 1.22: "Enhanced routing patterns".
- Reglas de precedencia de patrones en `ServeMux` (el más específico gana).
- Cómo `chi` construye grupos y subrouters encima de `http.Handler`.
- Comportamiento de `405 Method Not Allowed` y `Allow` header en `ServeMux`.

## Definición de hecho

- Se pueden registrar rutas con método, parámetros y prefijo.
- Hay tests con `httptest` que cubren match, parámetros, 404 y 405.

## Notas

<!-- Completar a medida que se investiga -->
