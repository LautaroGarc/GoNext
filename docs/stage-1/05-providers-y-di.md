# 05 — Providers e inyección de dependencias

## Qué es

Un provider es cualquier cosa que el framework construye y entrega a quien la necesite: servicios, repositorios, clientes. La inyección de dependencias (DI) es el mecanismo que decide en qué orden construirlos y a quién pasarle cada uno. Es el corazón de la idea "estilo NestJS".

## Cómo lo resuelve NestJS

Las clases marcadas con `@Injectable()` se registran en el módulo. Nest lee los tipos de los parámetros del constructor (vía metadata de TypeScript) y resuelve el grafo. Por defecto cada provider es un singleton dentro de la app.

## Cómo podría verse en Go

Usar funciones constructoras como unidad de registro, que es lo idiomático en Go:

```go
func NewTaskService(repo *TaskRepository) *TaskService { ... }

gonext.Provide(NewTaskService)
```

Dos grandes caminos para resolver el grafo:

- **En runtime con reflexión** (como `uber-go/dig` / `fx`): se inspeccionan los parámetros de la función.
- **En compilación con generación de código** (como `google/wire`): se genera el código de wiring.

Una tercera vía, más simple, es usar genéricos (`gonext.Provide[T]`) con resolución por tipo. El principio del producto pide "sin magia de reflexión pesada", así que esta decisión es clave.

## Preguntas abiertas

- ¿Reflexión, generación de código o genéricos? ¿Qué cantidad de reflexión es aceptable?
- ¿Se resuelve por tipo concreto, por interfaz o por nombre/token?
- ¿Qué pasa con dependencias circulares? ¿Error claro al arrancar?
- ¿Scopes además de singleton (por request)? Probablemente no en la Stage 1.
- ¿Cómo se reportan los errores: provider faltante, tipo duplicado?

## Para investigar

- Paquete `reflect`: `reflect.TypeOf`, `Type.NumIn`, `Value.Call`.
- `uber-go/dig` y `uber-go/fx`: API y cómo reportan errores.
- `google/wire`: el enfoque de generación de código.
- `samber/do`: DI basado en genéricos.
- Ordenamiento topológico y detección de ciclos en grafos.

## Definición de hecho

- Se pueden registrar constructores y el contenedor construye el grafo en orden.
- Errores claros para dependencia faltante y ciclos, con tests.

## Notas

<!-- Completar a medida que se investiga -->
