
![Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtQhOxCbDgjJ74d_KCtNBNcje0EluubZntQQ&s)


# Proyecto Urban Grocers 

En este proyecto se automatizan las pruebas de la lista de comprobacion especificamente para el campo ***name*** en la solicitud para la creación de un kit de productos.


## Contenido

* Servidor TT
* Api Urban Grocers
* Configuración 
* Pre requisitos
* Instalación
* Ejecutando las pruebas 
* Pruebas 

## Servidor TT

[URL servidor](https://cnt-4e23be61-e6ef-425d-afbd-6aff80fedbf9.containerhub.tripleten-services.com)

[URL API](https://cnt-4e23be61-e6ef-425d-afbd-6aff80fedbf9.containerhub.tripleten-services.com/docs/)



## API Urban Grocers

#### Creación de cuenta

```http
  POST /api/v1/users
```

| Campo | Tipo    | Descripción                |
| :-------- | :------- | :------------------------- |
|`firstName`| `string` | Nombre de usuario/a, escrito en el campo ***firstName*** de la tabla Users |
| `phone` | `string` | El número de teléfono del/de la usuario/a se escribe en el campo ***phone*** de la tabla Users |
| `address` | `string` | 	La dirección del/de la usuario/a se escribe en el campo ***address*** de la tabla Users |
|  |  |  |

#### Crear un kit

```http
  POST /api/v1/kits
```

| Campo | Tipo     | Descripción                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | Encabezado de autorización en formato `Bearer {authToken}`. Cuando se pasa - se devuelven todos las cestas creadas por el/la usuario/a. |
| `Content-Type` | `string` | Valor por defecto: `application/json` |




## Configuración

Para trabajar en este proyecto se debe clonar el repositorio de github o descargar el zip comprimido

## Pre requisitos

* PyCharm
* Conectividad al servidor TripleTen
* Cuenta github

### Paso 1: Conecta tu GitHub

El primer paso es enlazar tu cuenta de GitHub a TripleTen.
Esto te permitirá enviar tus proyectos automáticamente con tan solo hacer clic en un botón, directamente dentro de la plataforma de TripleTen.

### Paso 2: Clona el repositorio

Una vez que hayas vinculado tu cuenta de TripleTen con GitHub, se creará un repositorio automáticamente. El nombre del repositorio será `qa-project-Urban-Grocers-app-es`.

Ve a GitHub y clona el nuevo repositorio en tu computadora local, siguiendo estos pasos:

  1. Abre la línea de comandos en tu computadora.
  2. Si aún no lo has hecho, crea un directorio para almacenar todos tus proyectos.
```bash
  cd ~             # asegúrate de estar en tu directorio de inicio
mkdir projects     # crea una carpeta llamada projects
cd projects        # cambia el directorio a la nueva carpeta de proyectos
```

3. Clona el repositorio con SSH.
```bash
git clone git@github.com:username/qa-project-Urban-Grocers-app-es.git
```

```bash
   💡 Asegúrate de clonar el repositorio correcto. El nombre de usuario debe ser tu propio nombre de usuario, no tripleten-com.
``` 
## Instalación.
 ### Trabaja con el proyecto de forma local

Ahora tienes una copia local del proyecto y puedes abrir la carpeta del proyecto en tu computadora.

```bash
💡 Puedes utilizar PyCharm para trabajar en el proyecto localmente. Simplemente abre PyCharm y selecciona Archivo → Abrir y luego selecciona la carpeta qa-project-Urban-Grocers-app-es que clonaste en tu computadora.
```
```bash
   Recuerda instalar pytest y request
```
Necesitaras estos archivos 
* Configuration.py : Este archivo contiene las URL que necesitas. 
* Data.py : Este archivo contiene los cuerpos de la solicitud. 
* Sender_stand_request.py : En este archivo se encuentran las solicitudes necesarias para realizar las pruebas correspondientes.
* Create_kit_name_kit_test.py : Archivo en el cual estan las pruebas pertinentes para la verificacion del campo `name`.

Cuando puedas comenzar a trabajar, "Inicia el servidor" para obtener la URL de tu servidor.



## Ejecutando las pruebas

Para poder correr las pruebas es necesario actualizar la url del servidor en el archivo Configuration 

```bash
  URL_SERVICE = " https://cnt-3f66e78a-ed4a-4c31-974e-546deae27101.containerhub.tripleten-services.com"
```

Para poder verificar la lista de comprobacion del campo `name` es necesario realizar las siguientes solicitudes:

```bash
 1.- Solicitud para crear un nuevo usuario.
 2.- Solicitud para crear un kit para el mismo usuario, definiendo el token recibido de la solicitud previa.  
 3.- Crea una función donde se solicite el resultado de la solicitud de la creación de kit y comprueba que el codigo de estado y el campo `name` cumplan los requerimientos de la lista de comprobación.

 💡 Recuerda usar los endpoint pertinentes según la solicitud 
```

## Pruebas 

| N° | Descripción    | Resultado esperado|
| :-------- | :------- | :------------------------- |
| 1 | 	El número mínimo permitido de caracteres es 1: kit_body = { "name": "a"} | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 2 | 	El número permitido de caracteres es 511: kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"} | Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud |
| 3 | El número de caracteres es menor que la cantidad permitida 0: kit_body = { "name": "" } | Código de respuesta: 400 |
| 4 | 	El número de caracteres es mayor que la cantidad permitida 512: kit_body = { "name":"El valor de prueba para esta comprobación será inferior a”  | Código de respuesta: 400 |
| 5 | 	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 6 | 	Se permiten espacios: kit_body = { "name": " A Aaa " } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 7 | 	Se permiten números: kit_body = { "name": "123" } |  	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 8 | 	El parámetro no se pasa en la solicitud: kit_body = { } | 	Código de respuesta: 400 |
| 9 | 	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 } | 	Código de respuesta: 400 |




