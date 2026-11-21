# 07 — Bootstrap y ciclo de vida de la aplicación

## Qué es

El punto de entrada: crear la app a partir del módulo raíz, arrancar el servidor HTTP y apagarlo de forma ordenada. Incluye los "hooks" para que un provider pueda inicializarse (abrir una conexión) o cerrarse (liberarla).

## Cómo lo resuelve NestJS

`NestFactory.create(AppModule)` y luego `app.listen(3000)`. Los providers pueden implementar `OnModuleInit`, `OnApplicationBootstrap`, `OnModuleDestroy`, `OnApplicationShutdown`.

## Cómo podría verse en Go

```go
func main() {
    app, err := gonext.New(AppModule)
    if err != nil {
        log.Fatal(err)
    }
    if err := app.Listen(":8080"); err != nil {
        log.Fatal(err)
    }
}
```

`Listen` podría manejar internamente el graceful shutdown con `signal.NotifyContext` y `http.Server.Shutdown`. Los hooks podrían ser interfaces opcionales:

```go
type OnStart interface{ OnStart(ctx context.Context) error }
type OnStop  interface{ OnStop(ctx context.Context) error }
```

## Preguntas abiertas

- ¿`New` devuelve error o hace panic si el grafo es inválido?
- ¿En qué orden se llaman los hooks? (los de cierre en orden inverso)
- ¿Timeout configurable para el shutdown?
- ¿Se expone el `*http.Server` para configurarlo (timeouts, TLS)?

## Para investigar

- `http.Server.Shutdown` y `http.ErrServerClosed`.
- `os/signal` y `signal.NotifyContext`.
- Timeouts de `http.Server` (`ReadHeaderTimeout`, etc.) y por qué importan.
- Lifecycle hooks en uber-go/fx (`fx.Lifecycle`, `OnStart`/`OnStop`).

## Definición de hecho

- `gonext.New` + `Listen` levantan una app real.
- Ctrl+C cierra el servidor esperando requests en curso y llama los hooks de cierre.

## Notas

<!-- Completar a medida que se investiga -->
