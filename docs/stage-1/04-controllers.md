# 04 — Controllers

## Qué es

Un controller agrupa las rutas de un recurso (por ejemplo `/tasks`) y delega la lógica en providers. Es la capa que traduce HTTP a llamadas de negocio.

## Cómo lo resuelve NestJS

Una clase con `@Controller('tasks')` y métodos con `@Get(':id')`, `@Post()`. Las dependencias llegan por el constructor. Nest descubre las rutas leyendo la metadata de los decoradores.

## Cómo podría verse en Go

Go no tiene decoradores ni anotaciones, así que las rutas se declaran de forma explícita. Una propuesta:

```go
type TaskController struct {
    tasks *TaskService
}

func (c *TaskController) Routes(r gonext.Router) {
    r.Prefix("/tasks")
    r.Get("/{id}", c.Get)
    r.Post("", c.Create)
}
```

El framework llamaría a `Routes` al arrancar. Es más verboso que un decorador, pero se lee de arriba a abajo y no hay magia.

## Preguntas abiertas

- ¿Interfaz (`Routes(Router)`) o registro externo desde el módulo?
- ¿El controller es un provider más (resuelto por el contenedor DI) o algo aparte?
- ¿Dónde se define el prefijo: en el controller, en el módulo, o en los dos?
- ¿Se puede aplicar middleware a todo un controller?

## Para investigar

- Por qué Go no tiene anotaciones y qué alternativas se usan (struct tags, `go generate`).
- Cómo `huma` y `goa` declaran operaciones.
- Interfaces implícitas en Go: cómo detectar si un tipo implementa `Routes`.

## Definición de hecho

- Un controller puede declarar rutas con prefijo y recibir dependencias.
- El módulo registra sus controllers y las rutas quedan servidas.

## Notas

<!-- Completar a medida que se investiga -->
