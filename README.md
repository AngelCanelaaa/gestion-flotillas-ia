# Gestión de Flotillas con IA — Monitoreo de Fatiga de Conductores

Sistema de gestión de flotillas de transporte basado en microservicios, que integra un servicio de inteligencia artificial de detección de fatiga para generar alertas en tiempo real a los administradores.

Proyecto de la materia **Desarrollo de Aplicaciones WEB** — Instituto Tecnológico de Jiquilpan.
Docente: Martínez González Leonardo.

## Equipo

| Integrante | Rol |
|---|---|
| Ángel de Jesús Canela Figueroa | Scrum Master (fijo) y Product Owner |
| Isamar Chávez Díaz | Development Team |
| Katia Paola Victoria Escalera | Development Team |

## Arquitectura

El sistema sigue una arquitectura de microservicios:

- **api-gateway** — Punto de entrada único, valida JWT y enruta peticiones.
- **identity-service** — Registro, login, emisión de JWT, roles y permisos (PostgreSQL).
- **business-service** — Lógica central del negocio: vehículos, choferes, rutas, viajes e incidentes (PostgreSQL + MongoDB), incluye el worker consumidor de eventos de Redis Streams.
- **ai-service** — Servicio de detección de fatiga del conductor (modelo MobileNetV2, reutilizado del proyecto de Visión por Computadora y Machine Learning), expuesto vía FastAPI.
- **Redis Streams** — Mensajería asíncrona entre `ai-service` y `business-service`.

El detalle completo del diseño (diagramas, modelo entidad-relación, modelo de documentos MongoDB y justificación de cada base de datos) está en [`docs/Documento_Vision_Entregable1.pdf`](docs/Documento_Vision_Entregable1.pdf).

## Cómo levantar el proyecto localmente

### Requisitos
- Python 3.11+
- PostgreSQL 16
- MongoDB (próximo sprint)

### business-service
```bash
cd business-service
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp ../.env.example ../.env   # y edita con tus credenciales locales
python manage.py migrate
python manage.py runserver
```

### Variables de entorno
Ver [`.env.example`](.env.example) en la raíz del proyecto para la lista completa de variables requeridas (PostgreSQL y MongoDB).

## Flujo de ramas

- `main` — rama estable, protegida; solo recibe cambios vía Pull Request.
- `develop` — rama de integración, donde se mergean las features antes de pasar a `main`.
- `feature/SCRUM-XX-nombre-corto` — una rama por historia de usuario, nombrada con la clave de JIRA correspondiente (ej. `feature/SCRUM-9-registrar-vehiculo`).

Flujo de trabajo: crear rama `feature/` desde `develop` → Pull Request hacia `develop` → `develop` se mergea a `main` al cerrar cada entrega.

## Gestión del proyecto

El backlog completo, épicas, historias de usuario y sprints se gestionan en JIRA (proyecto "Gestión de Flotillas con IA", tipo Scrum).

## Entregables del semestre

1. Fundamentos y planeación del proyecto
2. Construcción de microservicios (Core)
3. Seguridad y control de acceso
4. Comunicación asíncrona entre microservicios
5. Despliegue en la nube y cierre del proyecto
