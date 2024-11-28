# Proyecto Urban Grocers
## Descripción del Proyecto

Este proyecto tiene como objetivo realizar pruebas automatizadas de la API de Urban Grocers. Las pruebas están diseñadas para garantizar que los endpoints de la API funcionen correctamente, validen adecuadamente los datos de entrada y devuelvan las respuestas esperadas en diferentes escenarios.

El proyecto incluye la validación de los siguientes endpoints principales:
- **Creación de usuarios:** Validación de la creación de nuevos usuarios, incluyendo pruebas con nombres válidos e inválidos.
- **Creación de kits personales:** Verificación de la lógica de los kits de productos, asegurando que los datos enviados sean procesados correctamente y cumplan con las restricciones establecidas.

---

## Fuente de Documentación

Este proyecto utiliza **apiDoc** como la fuente principal de documentación. apiDoc permite generar documentación clara y detallada directamente desde las anotaciones en el código.
Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.


---

## Tecnologías Utilizadas

El proyecto emplea las siguientes herramientas y tecnologías:
- **Python 3.11**: Lenguaje principal para las pruebas automatizadas.
- **Pytest**: Framework para pruebas unitarias y funcionales.
- **Requests**: Biblioteca para manejar solicitudes HTTP.
- **apiDoc**: Herramienta para generar documentación de la API.
- **Git**: Sistema de control de versiones.
- **PyCharm**: IDE utilizado para desarrollar y gestionar el proyecto.

## Instrucciones para Ejecutar el Proyecto

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

git clone https://github.com/(usuario)/qa-project-Urban-Grocers-app-es.git


### 2. Configurar el Entorno

Asegúrate de tener Python 3.11 instalado

Puedes verificar tu versión con el siguiente comando:
python --version

Instala las dependencias necesarias

Instala cada paquete requerido para este proyecto:

Instalar pytest (framework para pruebas):
pip install pytest

Instalar requests (biblioteca para solicitudes HTTP):
pip install requests

### 3. Verifica la configuración de la API

Abre el archivo configuration.py en un editor de texto o en PyCharm.
Asegúrate de que la URL del servicio y las rutas de los endpoints sean correctas.

## Ejecutar Pruebas Automatizadas en PyCharm

### 1. Asegúrate de que PyCharm reconozca Pytest
   
Ve a File → Settings → Tools → Python Integrated Tools.
En la sección Testing, selecciona pytest como el marco de prueba predeterminado.
Haz clic en OK para guardar los cambios.

### 2. Ejecutar un archivo específico de pruebas
Navega al archivo de prueba que deseas ejecutar (por ejemplo, create_kit_name_kit_test.py).
Haz clic derecho sobre el archivo.
Selecciona Run 'pytest in create_kit_name_kit_test'.


## Estructura del Proyecto
1. README.md                   # Información del proyecto-
2. configuration.py            # Configuración de la API y rutas de endpoints
3. data.py                     # Datos reutilizables para las pruebas
4. sender_stand_request.py     # Funciones para enviar solicitudes HTTP
5. create_kit_name_kit_test.py # Pruebas automatizadas para el endpoint de creación de kits









