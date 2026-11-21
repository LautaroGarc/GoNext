# 10 — Configuración

## Qué es

Cómo la app lee valores que cambian según el entorno: puerto, URL de la base de datos, nivel de log. Y cómo esos valores llegan a los providers que los necesitan.

## Cómo lo resuelve NestJS

`@nestjs/config` con un `ConfigModule` que carga variables de entorno (y archivos `.env`) y un `ConfigService` inyectable.

## Cómo podría verse en Go

La opción más simple: la configuración es un provider más. El usuario define su propio struct y un constructor que lo llena desde variables de entorno:

```go
type Config struct {
    Port        string
    DatabaseURL string
}

func LoadConfig() (*Config, error) { ... } // os.Getenv / os.LookupEnv

gonext.Provide(LoadConfig)
```

Así el framework no impone formato ni librería, y cualquier provider recibe `*Config` por DI.

## Preguntas abiertas

- ¿El framework ofrece un helper de configuración o solo documenta el patrón?
- ¿Soporte para archivos `.env` en la Stage 1? (implicaría una dependencia o un parser propio)
- ¿Validación de valores obligatorios al arrancar?
- ¿Cómo se configura el propio framework (puerto, timeouts)?

## Para investigar

- `os.Getenv` vs `os.LookupEnv`.
- The Twelve-Factor App — sección "Config".
- Librerías: `caarlos0/env`, `kelseyhightower/envconfig`, `spf13/viper` (y por qué viper puede ser demasiado).
- Struct tags y cómo leerlos con `reflect`.

## Definición de hecho

- Patrón de configuración decidido y usado en el ejemplo de referencia.
- La app falla al arrancar con un mensaje claro si falta un valor obligatorio.

## Notas

<!-- Completar a medida que se investiga -->
