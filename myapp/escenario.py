from PIL import Image
import numpy as np
from .utilidades import inicializacion

def cargar_imagen(ruta_imagen):
    imagen = Image.open(ruta_imagen)
    imagen = imagen.convert("RGB")
    return imagen_a_matriz(imagen)


def imagen_a_matriz(imagen):
    ancho, alto = imagen.size
    matriz = np.zeros((alto, ancho, 3), dtype=np.uint8)

    for y in range(alto):
        for x in range(ancho):
            matriz[y, x] = imagen.getpixel((x, y))

    return matriz


def convertir_color_a_valor(color):
    r, g, b = color
    if g > 150:
        return 1
    elif b > 100:
        return 5
    return 0


def convertir_color_a_humedad(estado):
    humedad_limites = [0.2, 0.4]
    if estado == 0 or estado == 5:
        return 1
    return np.random.uniform((1 - humedad_limites[1]), (1 - humedad_limites[0]))


def espacio_imagen(matriz):
    alto, ancho, _ = matriz.shape
    matriz_grid = np.zeros((alto, ancho), dtype=np.uint8)
    matriz_humedad = np.zeros((alto, ancho))
    for y in range(alto):
        for x in range(ancho):
            color = matriz[y, x]
            matriz_grid[y, x] = convertir_color_a_valor(color)
            matriz_humedad[y, x] = convertir_color_a_humedad(matriz_grid[y, x])
    print(np.sum(matriz_grid != 0))
    return matriz_grid, matriz_humedad


def espacio_aleatorio(grid_size):
    vect_inicializacion = np.vectorize(inicializacion)
    grid = np.random.rand(grid_size[0], grid_size[1])
    grid = vect_inicializacion(grid)
    humedad_grid = np.random.rand(grid_size[0], grid_size[1])
    return grid, humedad_grid