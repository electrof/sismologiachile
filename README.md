# sismologiachile
API Que funciona extrayendo datos del sitio web Del CSN (https://www.sismologia.cl)
# Módulo Sismología

Este módulo permite extraer y visualizar información sobre eventos sísmicos desde la página del CSN (Centro de Sismológico Nacional). Este módulo permite obtener datos tanto en modo básico como detallado, limitar el número de resultados, y un modo en vivo que actualiza los datos cada cierto intervalo de tiempo.

## Instalación

Para usar este módulo, necesitarás tener Python instalado en tu máquina, así como las librerías `requests` y `beautifulsoup4`. Puedes instalar estas dependencias utilizando pip:

```
pip install requests beautifulsoup4
```

## Uso del Módulo

A continuación, se describen las funciones disponibles en el módulo y cómo puedes utilizarlas en tus scripts.

### Funciones Disponibles

- `obtener_datos_sismicos(detallado=False, num_resultados=None)`: Esta función extrae los últimos eventos sísmicos. Puede devolver información básica o detallada y limitar el número de resultados.
  
  - `detallado`: Si es `True`, devuelve información detallada de cada evento.
  - `num_resultados`: Limita el número de eventos a devolver.

- `modo_en_vivo(intervalo=30)`: Esta función inicia un modo en vivo que actualiza y muestra nuevos eventos sísmicos cada `intervalo` segundos. Solo muestra nuevos eventos que no se hayan mostrado antes.

### Ejemplos

#### Obtener los últimos tres eventos en modo básico

```python
from sismologia import obtener_datos_sismicos

eventos = obtener_datos_sismicos(num_resultados=3)
for evento in eventos:
    print(evento)
```

#### Obtener eventos en modo detallado

```python
from sismologia import obtener_datos_sismicos

eventos = obtener_datos_sismicos(detallado=True, num_resultados=5)
for evento in eventos:
    print(evento)
```

#### Usar el modo en vivo

```python
from sismologia import modo_en_vivo

# Inicia el modo en vivo actualizando cada 60 segundos
modo_en_vivo(intervalo=60)
```

## Manejo de Errores

El módulo maneja varios tipos de errores, incluyendo errores de conexión y errores al encontrar la información requerida en el sitio web. Se recomienda implementar manejo de excepciones cuando se utilice este módulo en aplicaciones de producción.
