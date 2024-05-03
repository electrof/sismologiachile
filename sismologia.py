import requests
from bs4 import BeautifulSoup
import time

URL_BASE = 'http://www.sismologia.cl'

def obtener_datos_sismicos(detallado=False, num_resultados=None):
    respuesta = requests.get(URL_BASE)
    if respuesta.status_code != 200:
        return "Error al obtener la página"

    soup = BeautifulSoup(respuesta.text, 'html.parser')
    tabla_sismos = soup.find('table', class_='sismologia')
    if not tabla_sismos:
        return "Tabla de sismos no encontrada"
    
    eventos = []
    filas = tabla_sismos.find_all('tr')[1:]  # Ignorar la fila de encabezados
    for fila in filas:
        columnas = fila.find_all('td')
        if len(columnas) == 3:
            evento = {
                'id_evento': columnas[0].text.strip(),  # Usar la fecha y hora como identificador único
                'fecha_local': columnas[0].text.split('\n')[0],
                'ubicacion': columnas[0].text.split('\n')[1],
                'profundidad': columnas[1].text,
                'magnitud': columnas[2].text,
                'detalles': obtener_detalles_sismicos(URL_BASE + columnas[0].find('a')['href']) if detallado else {}
            }
            eventos.append(evento)
            if num_resultados and len(eventos) >= num_resultados:
                break
    return eventos

def obtener_detalles_sismicos(enlace):
    respuesta = requests.get(enlace)
    if respuesta.status_code != 200:
        return "Error al obtener detalles"
    
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    tabla_detalles = soup.find('table', class_='sismologia informe')
    if not tabla_detalles:
        return "Detalles no disponibles"
    
    detalles = {}
    for fila in tabla_detalles.find_all('tr'):
        detalles[fila.find_all('td')[0].text] = fila.find_all('td')[1].text
    return detalles

def modo_en_vivo(intervalo=30):
    eventos_anteriores = set()
    try:
        while True:
            eventos = obtener_datos_sismicos()
            nuevos_eventos = [evento for evento in eventos if evento['id_evento'] not in eventos_anteriores]
            if nuevos_eventos:
                for evento in nuevos_eventos:
                    print(evento)
                    eventos_anteriores.add(evento['id_evento'])
            else:
                print("No hay nuevos eventos.")
            print("Esperando próxima actualización...")
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("Modo en vivo detenido")

if __name__ == "__main__":
    modo_en_vivo()