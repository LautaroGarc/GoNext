# 11 — Logging

## Qué es

Cómo el framework y la app registran lo que pasa: arranque, rutas registradas, requests, errores. También cómo un provider obtiene un logger.

## Cómo lo resuelve NestJS

Un `Logger` incluido, con contexto por clase (`new Logger(TasksService.name)`), reemplazable por uno propio.

## Cómo podría verse en Go

Desde Go 1.21 existe `log/slog` en la stdlib: logging estructurado con niveles y handlers (texto o JSON). Encaja con el principio "la stdlib primero":

```go
func NewTaskService(log *slog.Logger) *TaskService {
    return &TaskService{log: log.With("component", "tasks")}
}
```

El framework podría registrar un `*slog.Logger` como provider por defecto, que el usuario reemplaza si quiere.

## Preguntas abiertas

- ¿`*slog.Logger` directo o una interfaz propia?
- ¿Qué loguea el framework por defecto al arrancar? (rutas, módulos)
- ¿Middleware de log de requests incluido? (relación con item 08)
- ¿Cómo se agrega el request ID a todos los logs de una request?

## Para investigar

- Paquete `log/slog`: `Logger`, `Handler`, `With`, `Group`, `TextHandler`, `JSONHandler`.
- Artículo "Structured Logging with slog" en el blog de Go.
- `slog` con `context.Context` (`InfoContext`) y handlers que leen valores del contexto.

## Definición de hecho

- El framework usa `slog` internamente y expone un logger inyectable.
- El usuario puede pasar su propio `*slog.Logger` al crear la app.

## Notas

<!-- Completar a medida que se investiga -->
