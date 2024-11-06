import pandas as pd
import os
import folium
import time
from flask import Flask, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



app = Flask(__name__)

chrome_options = Options()
chrome_options.add_argument("--headless")  # Modo headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Función para obtener los sismos
def obtener_sismos():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)  # Añadir opciones headless
    driver.get("https://rsn.ucr.ac.cr/actividad-sismica/ultimos-sismos")
    time.sleep(1)
    tabla = driver.find_element(By.XPATH, '//*[@id="adminForm"]/table')
    filas = tabla.find_elements(By.TAG_NAME, "tr")

    df_sismos = pd.DataFrame(columns=['Fecha', 'Hora Local', 'Localización', 'Profundidad', 'Magnitud', 'Intensidades', 'Origen', 'Latitud', 'Longitud'])

    for i in range(5):  # Limitar a los primeros 5 registros
        filas[i].click()
        time.sleep(1)
        info_sismo = driver.find_element(By.XPATH, '//*[@id="sp-component"]/div/article/div[2]').text
        coordenadas = driver.find_element(By.XPATH, '//*[@id="sp-component"]/div/article/div[2]/p[7]').text

        sismo_data = {}
        info_sismo_lines = info_sismo.splitlines()

        for line in info_sismo_lines:
            if "Fecha:" in line:
                sismo_data['Fecha'] = line.split(": ")[1].strip()
            elif "Hora Local:" in line:
                sismo_data['Hora Local'] = line.split(": ")[1].strip()
            elif "Localización:" in line:
                sismo_data['Localización'] = line.split(": ")[1].strip()
            elif "Profundidad:" in line:
                sismo_data['Profundidad'] = line.split(": ")[1].strip()
            elif "Magnitud:" in line:
                sismo_data['Magnitud'] = line.split(": ")[1].strip()
            elif "Intensidades:" in line:
                sismo_data['Intensidades'] = line.split(": ")[1].strip()
            elif "Origen:" in line:
                sismo_data['Origen'] = line.split(": ")[1].strip()

        coord_clean = coordenadas.replace("Coordenadas: ", "").strip()
        latitud_str, longitud_str = coord_clean.split(" y ")
        latitud = float(latitud_str.strip().replace(',', '.'))
        longitud = float(longitud_str.strip().replace(',', '.').rstrip('.'))

        sismo_data['Latitud'] = latitud
        sismo_data['Longitud'] = longitud

        df_nuevo_sismo = pd.DataFrame([sismo_data])
        df_sismos = pd.concat([df_sismos, df_nuevo_sismo], ignore_index=True)

        driver.back()
        time.sleep(1)
        filas = tabla.find_elements(By.TAG_NAME, "tr")

    driver.quit()
    return df_sismos

# Ruta para la página principal
@app.route('/')
def index():
    df_sismos = obtener_sismos()
    mapa_html = crear_mapa(df_sismos)  # Crear el mapa y obtener el HTML
    return render_template('index.html', sismos=df_sismos, mapa_html=mapa_html)

# Ruta para obtener los sismos en formato JSON
@app.route('/actualizar_sismos')
def actualizar_sismos():
    df_sismos = obtener_sismos()
    return jsonify(df_sismos.to_dict(orient='records'))  # Devuelve los sismos en formato JSON

# Función para crear el mapa
def crear_mapa(df_sismos):
    # Crear un mapa centrado en Costa Rica
    mapa = folium.Map(location=[9.9281, -84.0907], zoom_start=7)

    # Agregar marcadores para cada sismo
    for _, sismo in df_sismos.iterrows():
        folium.Marker(
            location=[sismo['Latitud'], sismo['Longitud']],
            popup=f"{sismo['Fecha']} {sismo['Hora Local']}<br>Magnitud: {sismo['Magnitud']}<br>Localización: {sismo['Localización']}",
            icon=folium.Icon(color='red')
        ).add_to(mapa)

    # Guardar el mapa en un archivo HTML
    mapa.save('mapa_sismos.html')
    return mapa._repr_html_()  # Retornar el HTML del mapa

if __name__ == '__main__':
    app.run(debug=True)
