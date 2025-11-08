# import os
# import msvcrt  # sirve para leer teclas
# # tamaño del cuadro
# FILAS = 10
# COLUMNAS = 10

# # limpiar pantalla
# def limpiar():
#     os.system("cls")

# def mostrar_cuadro(cursor_fila, cursor_col):
#     limpiar()
#     print("🎬 Usa las flechas para moverte (q para salir)\n")
#     for f in range(FILAS):
#         for c in range(COLUMNAS):
#             if f == cursor_fila and c == cursor_col:
#                 print("🟦", end=" ")  # posicion actual
#             else:
#                 print("⬜", end=" ")  # asiento vacio
#         print()
#     print()
    
    
# def seating():
#     cursor_fila = 0
#     cursor_col = 0

#     while True:
#         mostrar_cuadro(cursor_fila, cursor_col)
#         tecla = msvcrt.getch()  # lee una tecla

#         if tecla == b"q":  # salir
#             limpiar()
#             print("👋 Programa terminado.")
#             break

# # Codigos de las flechitas
# # 
# #   Flecha arriba    → b'\xe0' luego b'H'
# #   Flecha abajo     → b'\xe0' luego b'P'
# #   Flecha derecha   → b'\xe0' luego b'M'
# #   Flecha izquierda → b'\xe0' luego b'K'

#         if tecla == b"\xe0":
#             flecha = msvcrt.getch()
#             if flecha == b"H":  # arriba
#                 cursor_fila = max(0, cursor_fila - 1)
#             elif flecha == b"P":  # abajo
#                 cursor_fila = min(FILAS - 1, cursor_fila + 1)
#             elif flecha == b"M":  # derecha
#                 cursor_col = min(COLUMNAS - 1, cursor_col + 1)
#             elif flecha == b"K":  # izquierda
#                 cursor_col = max(0, cursor_col - 1)

import os
import msvcrt 
from typing import List, Dict, Any

class SalaDeCine:

    FILAS = 10
    COLUMNAS = 10

    def __init__(self, titulo_pelicula: str, filas: int = FILAS, columnas: int = COLUMNAS):
        """Inicializa la sala con el título de la película."""
        self.titulo = titulo_pelicula
        self.filas = filas
        self.columnas = columnas
        self.cursor_fila = 0
        self.cursor_col = 0
        self.teclas_flecha = {
            b'H': 'arriba',
            b'P': 'abajo',
            b'M': 'derecha',
            b'K': 'izquierda'
        }
        # Lista para guardar los asientos seleccionados
        self.asientos_seleccionados = [] 

    def _limpiar(self):
        os.system("cls")

    def _mostrar_cuadro(self):
        self._limpiar()
        print(f"🎥 **{self.titulo}**")
        print("----------------------------------------------------------------------")
        print("➡️  Usa flechas para moverte. [Enter] para seleccionar/deseleccionar. [Q] para salir/volver.\n")
        
        for f in range(self.filas):
            for c in range(self.columnas):
                if f == self.cursor_fila and c == self.cursor_col:
                    print("🟦", end=" ")  # Posición actual (Cursor)
                elif (f, c) in self.asientos_seleccionados:
                    print("🟥", end=" ")  # Asiento Seleccionado
                else:
                    print("⬜", end=" ")  # Asiento vacío
            print()
        print("\nAsientos seleccionados:", self.asientos_seleccionados)
        print("----------------------------------------------------------------------")

    def _mover_cursor(self, direccion):
        if direccion == 'arriba':
            self.cursor_fila = max(0, self.cursor_fila - 1)
        elif direccion == 'abajo':
            self.cursor_fila = min(self.filas - 1, self.cursor_fila + 1)
        elif direccion == 'derecha':
            self.cursor_col = min(self.columnas - 1, self.cursor_col + 1)
        elif direccion == 'izquierda':
            self.cursor_col = max(0, self.cursor_col - 1)

    def _seleccionar_asiento(self):
        #Marca o desmarca el asiento actual
        asiento_actual = (self.cursor_fila, self.cursor_col)
        if asiento_actual in self.asientos_seleccionados:
            self.asientos_seleccionados.remove(asiento_actual)
            print(f"Asiento {asiento_actual} deseleccionado.")
        else:
            self.asientos_seleccionados.append(asiento_actual)
            print(f"Asiento {asiento_actual} seleccionado.")
    
    def seleccionar_asientos(self) -> List[tuple]:
        while True:
            self._mostrar_cuadro()
            tecla = msvcrt.getch()

            if tecla == b"q":  # Salir/Volver al menú
                return self.asientos_seleccionados

            if tecla == b"\r": # Tecla Enter para seleccionar
                self._seleccionar_asiento()
                continue
                
            if tecla == b"\xe0": # Flechas
                flecha = msvcrt.getch()
                if flecha in self.teclas_flecha:
                    direccion = self.teclas_flecha[flecha]
                    self._mover_cursor(direccion)