# Seguimiento de Sismos en Tiempo Real

**Descripción del Proyecto:**

Este proyecto proporciona una plataforma para monitorear la actividad sísmica reciente en Costa Rica. La aplicación muestra una lista actualizada de los últimos sismos, 
así como su ubicación en un mapa interactivo. Los usuarios también reciben notificaciones en tiempo real cuando ocurre un nuevo sismo.

**Características:**
- Visualización en tiempo real de los últimos sismos en Costa Rica.
- Mapa interactivo con las ubicaciones de los sismos utilizando **Folium**.
- Notificaciones de nuevos sismos en el navegador.
- Información detallada de cada sismo, como fecha, hora, magnitud y localización.
- Actualización automática de los datos cada minuto.

## Tecnologías Utilizadas:
- **Python**: Backend del proyecto, para el procesamiento de datos y web scraping.
- **Flask**: Framework de Python utilizado para crear la API y la interfaz web.
- **Selenium**: Herramienta de web scraping para obtener información de la Red Sismológica de Costa Rica.
- **Folium**: Biblioteca de Python para la creación de mapas interactivos.
- **Leaflet.js**: Usado en el frontend para renderizar mapas interactivos.
- **HTML y CSS**: Para el diseño de la página web.
- **JavaScript**: Para la actualización de la interfaz y manejo de notificaciones en tiempo real.

## Instalación:

Para ejecutar el proyecto localmente, sigue estos pasos:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/CrisPrezNavarro/Sismos-De-Costa-Rica.git
   cd Sismos-De-Costa-Rica

**Instalar dependencias**: Asegúrate de tener un entorno virtual de Python configurado. Luego, instala las dependencias necesarias:

pip install -r requirements.txt

**Requisitos del sistema:**
Selenium requiere que tengas instalado el driver de Chrome, si no lo tienes, se instalará automáticamente con webdriver_manager.
Instalar Flask, Folium, y otras bibliotecas necesarias ejecutando:

pip install flask selenium folium

**Ejecutar la aplicación:** Para ejecutar la aplicación, usa el siguiente comando:

python app.py
Abre tu navegador y ve a http://localhost:5000 para ver la aplicación.

**Uso:**
La aplicación mostrará la información más reciente sobre sismos en Costa Rica, incluyendo detalles como:

Fecha y hora del sismo.
Magnitud y localización.
Coordenadas geográficas.
La lista de sismos se actualiza automáticamente cada minuto, y si ocurre un nuevo sismo, recibirás una notificación en tu navegador.

**Contribuciones:**
Las contribuciones son bienvenidas. Si tienes alguna sugerencia, mejora o corrección, siéntete libre de crear un pull request o abrir un issue.

Cómo contribuir:
Haz un fork del repositorio.
Crea una rama para tu característica o corrección.
Haz commit de tus cambios.
Haz un pull request detallando tus modificaciones.

**Licencia:**
Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
