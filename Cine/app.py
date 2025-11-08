from api import obtener_peliculas_populares
from seating import SalaDeCine

#Menu inicial
start = {
    1: ("Administrador"),
    2: ("Empleado"),
    3: ("Salir")
}

def menu_start():
    for i in range(1, len(start) + 1):
        print(f"{i}. {start[i]}")

# Menu administrador
admin = {
    1: ("Agregar pelicula"),
    2: ("Modificar pelicula"),
    3: ("Eliminar pelicula"),
    4: ("Estadisticas"),
    4: ("Salir"),
}
# Menu empleado
employee = {
    1: ("Comprar boletos"),
    2: ("Cambiar boletos"),
    3: ("Reembolso"),
    4: ("Lista peliculas"),
    5: ("Salir"),
}



def main():
    #seating()
    #lista_peliculas = obtener_peliculas_populares(10)
    sala = SalaDeCine("Interstellar")
    sala.seleccionar_asientos()
    
if __name__ == "__main__":
    main()
