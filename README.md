# Urban Grocers API Testing

Proyecto de automatización de pruebas para validar el funcionamiento
del endpoint de creación de kits de la API Urban Grocers.

El objetivo es verificar que la API procese correctamente las
solicitudes y aplique las reglas de validación establecidas
para el campo `name`.

## Tecnologías utilizadas

- Python 3.15
- Pytest 9.2.0
- Requests
- JSON
- API REST
- Pytest HTML Report

## Funcionalidades probadas

Endpoint:

`POST /api/v1/kits`

Se realizaron pruebas para validar:

- Creación de kits con nombres válidos.
- Validación de nombres vacíos.
- Validación de caracteres no permitidos.
- Validación de nombres que contienen números.
- Respuestas HTTP de la API.
- Contenido de las respuestas JSON.

## Casos de prueba

Se implementaron 9 pruebas automatizadas:

| Categoría | Casos |
|---|---:|
| Pruebas positivas | 4 |
| Pruebas negativas | 5 |
| Total | 9 |

## Resultados de ejecución

Última ejecución:

| Resultado | Cantidad |
|---|---:|
| PASSED | 4 |
| FAILED | 5 |
| Total | 9 |

Las pruebas positivas confirmaron que la API permite
crear kits con nombres válidos.

Las pruebas negativas identificaron un incumplimiento
en la validación del campo `name`: la API devuelve
HTTP 201 Created cuando se esperaba HTTP 400 Bad Request.

## Defecto identificado

**BUG-001: Validación incorrecta del nombre del kit.**

La API permite crear kits con nombres que incumplen
las reglas de validación documentadas.

El defecto se encuentra documentado en `BUG_REPORT.md`.

## Estructura del proyecto

```text
qa-project-Urban-Grocers-app-es/
│
├── configuration.py
├── data.py
├── sender_stand_request.py
├── create_kit_name_kit_test.py
├── conftest.py
├── BUG_REPORT.md
├── README.md
├── .gitignore
│
├── reports/
│   └── reporte_pruebas.html
│
└── .venv/