# 01 — Estructura del repositorio y del módulo Go

## Qué es

Decidir cómo se organiza el código del framework dentro del repo: qué paquetes existen, qué es API pública y qué es interno, y dónde viven los ejemplos. Es la base sobre la que se apoya todo lo demás, y cambiarla después es caro porque rompe los imports de quien use el framework.

## Cómo lo resuelve NestJS

NestJS publica varios paquetes npm (`@nestjs/core`, `@nestjs/common`, `@nestjs/platform-express`...). `common` tiene los decoradores y tipos que usa el usuario; `core` tiene la maquinaria interna (el contenedor, el scanner de módulos).

## Cómo podría verse en Go

Un solo módulo (`github.com/LautaroGarc/GoNext`) con pocos paquetes:

```
gonext/            # API pública: App, Module, Controller, Context...
internal/          # detalles que el usuario no debería importar
examples/basic-api # ejemplo de referencia
docs/
```

En Go, lo que está bajo `internal/` no se puede importar desde fuera del módulo: es la forma idiomática de separar API pública de implementación.

## Preguntas abiertas

- ¿Un paquete raíz único (`gonext`) o varios (`gonext/http`, `gonext/di`)?
- ¿El paquete raíz va en la raíz del repo o en un subdirectorio?
- ¿Los ejemplos son parte del mismo módulo o cada uno tiene su `go.mod`?
- ¿Cómo se llama el paquete al importarlo? (`gonext.New()` vs `next.New()`)

## Para investigar

- Cómo funciona `internal/` en Go y por qué existe.
- Layout de proyectos conocidos: `chi`, `echo`, `gin`, `fx`.
- Go workspaces (`go work`) para tener ejemplos con su propio `go.mod`.
- Versionado semántico de módulos Go y qué implica una v2 (`/v2` en el path).
- Artículo "Organizing a Go module" en go.dev.

## Definición de hecho

- Hay un layout decidido y documentado (este mismo archivo).
- `go build ./...` y `go vet ./...` pasan con los paquetes vacíos creados.

## Notas

<!-- Completar a medida que se investiga -->
