# 06 — Módulos (imports / exports)

## Qué es

Un módulo agrupa controllers y providers de una misma área (`tasks`, `users`) y define qué expone hacia afuera. Es lo que da límites claros a la aplicación a medida que crece.

## Cómo lo resuelve NestJS

`@Module({ imports, controllers, providers, exports })`. Un módulo solo puede usar providers propios o exportados por módulos que importa. Hay un `AppModule` raíz desde el que Nest recorre el árbol.

## Cómo podría verse en Go

Un struct de configuración en vez de un decorador:

```go
var TasksModule = gonext.Module{
    Name:        "tasks",
    Imports:     []gonext.Module{DatabaseModule},
    Providers:   []any{NewTaskRepository, NewTaskService},
    Controllers: []any{NewTaskController},
    Exports:     []any{(*TaskService)(nil)},
}
```

El framework recorre el árbol desde el módulo raíz, arma un contenedor por módulo (o uno global con reglas de visibilidad) y verifica que nadie use algo no exportado.

## Preguntas abiertas

- ¿Valor (`gonext.Module{...}`) o función (`func TasksModule() gonext.Module`)?
- ¿Cómo se identifican los exports: por tipo, por constructor?
- ¿Un contenedor por módulo o uno global que valida visibilidad?
- ¿Se permiten módulos globales (como `@Global()` en Nest)?
- ¿Cómo encajan los módulos con los paquetes Go? ¿Un módulo por paquete?

## Para investigar

- Documentación de Modules en NestJS: shared modules, global modules, dynamic modules.
- `fx.Module` y `fx.Private` en uber-go/fx.
- Cómo los paquetes Go ya ofrecen encapsulamiento (mayúsculas/minúsculas) y si se solapa con los exports.

## Definición de hecho

- Una app con dos módulos donde uno usa un provider exportado por el otro.
- Error al arrancar si se usa un provider no exportado, con test.

## Notas

<!-- Completar a medida que se investiga -->
