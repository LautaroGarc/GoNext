# 13 — Ejemplo de referencia y README

## Qué es

Una app de ejemplo chica pero real que use todo lo de la Stage 1, y un README que muestre cómo se usa GoNext. Es lo primero que ve quien llega al repo, y también la prueba de que las piezas encajan entre sí.

## Cómo lo resuelve NestJS

La documentación oficial arranca con un "First steps" que genera un proyecto con `AppModule`, `AppController` y `AppService`, y luego crece con un CRUD de ejemplo (`cats`).

## Cómo podría verse en Go

Un CRUD de tareas en `examples/basic-api/` con:

- `AppModule` que importa `TasksModule` y un `ConfigModule` (o provider de config).
- `TaskController`, `TaskService`, `TaskRepository` (en memoria para no sumar dependencias).
- Tests usando las utilidades del item 12.

El README muestra el fragmento mínimo (módulo + controller + `main`) y enlaza al ejemplo completo. Mientras algo no esté implementado, se marca como **propuesto**.

## Preguntas abiertas

- ¿Repositorio en memoria o SQLite? (en memoria mantiene el ejemplo sin dependencias)
- ¿Un solo ejemplo o varios chicos (hola mundo, CRUD, multi-módulo)?
- ¿El ejemplo tiene su propio `go.mod`? (relación con item 01)
- ¿Qué secciones necesita el README para la Stage 1? (instalación, ejemplo, estado, roadmap)

## Para investigar

- READMEs de frameworks Go: `chi`, `echo`, `fx`, `huma`. Qué muestran primero.
- Tests de ejemplo (`func ExampleXxx`) en Go: documentación que además se ejecuta.
- `pkg.go.dev`: cómo se ve la documentación generada a partir de los comentarios.

## Definición de hecho

- `go run ./examples/basic-api` levanta la API y `go test ./...` pasa.
- El README refleja la API real y enlaza a este roadmap.

## Notas

<!-- Completar a medida que se investiga -->
