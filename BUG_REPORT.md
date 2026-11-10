# BUG REPORT
## Urban Grocers API Testing

**Proyecto:** Urban Grocers API  
**Módulo:** Creación de kits  
**Endpoint:** POST /api/v1/kits  
**ID del defecto:** BUG-001  
**Severidad:** Major  
**Prioridad:** High  
**Estado:** Open  
**Reportado por:** Freddy Ramirez  
**Tipo de prueba:** API Testing  

---

### 1. Título

La API permite crear kits con nombres que incumplen las reglas de validación.

### 2. Descripción

Al realizar solicitudes POST al endpoint `/api/v1/kits`,
la API permite crear kits utilizando nombres que contienen
caracteres no permitidos o que están vacíos.

De acuerdo con la documentación, el nombre debe contener
únicamente letras latinas, espacios y guiones.

Sin embargo, la API responde HTTP 201 Created ante
los cinco valores negativos probados.

### 3. Precondiciones

- Disponer de acceso a la API Urban Grocers.
- Crear un usuario mediante el endpoint correspondiente.
- Obtener un authToken válido.
- Utilizar el token para realizar la solicitud de creación del kit.

### 4. Pasos para reproducir

1. Crear un usuario nuevo.
2. Obtener su authToken.
3. Enviar una solicitud POST a `/api/v1/kits`.
4. Incluir en el cuerpo JSON un nombre que incumpla
   las reglas de validación.
5. Revisar el código de estado de la respuesta.

### 5. Datos de prueba

| Caso | Nombre enviado | Resultado esperado |
|---|---|---|
| 1 | "" | HTTP 400 |
| 2 | "Kit123" | HTTP 400 |
| 3 | "Kit_name" | HTTP 400 |
| 4 | "Kit @#$%" | HTTP 400 |
| 5 | "123456" | HTTP 400 |

### 6. Resultado esperado

La API debe rechazar los nombres que no cumplan
las reglas de validación y responder:

HTTP 400 Bad Request.

### 7. Resultado actual

La API acepta los cinco valores negativos y responde:

HTTP 201 Created.

Esto permite crear kits con nombres que incumplen
las reglas documentadas.

### 8. Evidencia

Ejecución automatizada mediante Pytest:

- Total de pruebas: 9
- Pruebas aprobadas: 4
- Pruebas fallidas: 5

Los cinco casos negativos recibieron HTTP 201
en lugar del HTTP 400 esperado.

### 9. Impacto

La validación del campo `name` no está funcionando
de acuerdo con los requisitos documentados.

Esto permite almacenar nombres de kits con formatos
no permitidos.

### 10. Entorno de pruebas

- Sistema operativo: Windows
- Lenguaje: Python 3.15
- Framework: Pytest 9.2.0
- Librería HTTP: Requests
- Tipo de aplicación: API REST
- Método HTTP: POST