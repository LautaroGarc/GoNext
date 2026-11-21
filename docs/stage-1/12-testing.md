# 12 — Utilidades de testing

## Qué es

Herramientas para que el usuario testee su app GoNext fácilmente: levantar un módulo en un test, reemplazar un provider por un fake y hacer requests sin abrir un puerto real. También cubre cómo se testea el framework en sí.

## Cómo lo resuelve NestJS

`Test.createTestingModule({...})` con `.overrideProvider(X).useValue(mock)`, y luego `supertest` para hacer requests contra la app.

## Cómo podría verse en Go

La stdlib ya trae `net/http/httptest`. GoNext podría sumar un helper para construir la app con overrides:

```go
func TestGetTask(t *testing.T) {
    app := gonext.NewTest(t, TasksModule,
        gonext.Override[*TaskRepository](fakeRepo),
    )
    rec := httptest.NewRecorder()
    app.ServeHTTP(rec, httptest.NewRequest("GET", "/tasks/1", nil))
    // assert rec.Code, rec.Body...
}
```

Si la app implementa `http.Handler`, testearla con `httptest` es directo.

## Preguntas abiertas

- ¿La app implementa `http.Handler` (`ServeHTTP`)?
- ¿Cómo se identifica qué provider reemplazar? (por tipo, igual que en DI)
- ¿Un paquete aparte (`gonext/gonexttest`) para no mezclar helpers de test con la API?
- ¿Librería de asserts o solo la stdlib `testing`?

## Para investigar

- `net/http/httptest`: `NewRecorder`, `NewRequest`, `NewServer`.
- Table-driven tests en Go.
- `t.Cleanup`, `t.Helper`, `t.Parallel`.
- Convención de paquetes `xxxtest` en la stdlib (`httptest`, `iotest`, `fstest`).

## Definición de hecho

- Se puede testear un controller con un provider reemplazado, sin abrir puertos.
- El framework tiene tests para router, DI, módulos y errores; `go test ./...` pasa.

## Notas

<!-- Completar a medida que se investiga -->
