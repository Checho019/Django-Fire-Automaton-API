from myapp.kernels import K_V0, propagar_valor, que,K_V190,K_V145,aplicar_agua
from myapp.escenario import espacio_imagen, cargar_imagen
from myapp.utilidades import *


class Simulacion:
    def __init__(self):
        # Variables de inicialización
        self.width = 1200
        self.height = 700
        self.grid_size = [self.height // 10, self.width // 10]
        self.grid, self.humedad_grid = espacio_imagen(cargar_imagen('myapp/nuevo.jpg'))
        self.kernel = K_V0
        self.quemado = que.quemado

        # Guardar datos para reinicio
        self.estado_inicial = self.grid.copy()
        self.humedad_inicial = self.humedad_grid.copy()

        # Variables de control
        self.water_mode = False
        self.humedad_view = False
        self.paused = False
        self.running = True

    def siguiente_paso(self):
        self.grid = propagar_valor(self.grid, self.kernel, self.humedad_grid)
        self.quemado = que.quemado

    def poner_fuego(self, punto):
        self.grid[punto[0]][punto[1]] = 2

    def poner_agua(self, punto):
        self.humedad_grid = aplicar_agua(self.humedad_grid, self.kernel, (punto[0], punto[1]), self.grid)

    def reiniciar(self):
        self.grid = self.estado_inicial
        self.humedad_grid = self.estado_inicial
        que.quemado = 0
        self.kernel = K_V0

    def cambiar_velocidad(self, direccion):
        if direccion == 8:
            self.kernel = np.rot90(K_V145, k=1)
        elif direccion == 2:
            self.kernel = K_V145
        elif direccion == 6:
            self.kernel = np.rot90(K_V145, k=2)
        elif direccion == 4:
            self.kernel = np.rot90(K_V145, k=-1)
        elif direccion == 1:
            self.kernel = np.rot90(K_V190, k=1)
        elif direccion == 5:
            self.kernel = np.rot90(K_V190, k=-1)
        elif direccion == 7:
            self.kernel = np.rot90(K_V190, k=2)
        elif direccion == 3:
            self.kernel = K_V190
