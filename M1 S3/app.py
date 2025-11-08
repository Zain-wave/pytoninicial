from servicios import Inventario
from archivos import archivo_inventario

# Menú principal con las opciones disponibles
menu = {
    1: ("Agregar Producto"),
    2: ("Mostrar Inventario"),
    3: ("Buscar Producto"),
    4: ("Actualizar Producto"),
    5: ("Eliminar Producto"),
    6: ("Estadisticas"),
    7: ("Guardar CSV"),
    8: ("Cargar CSV"),
    9: ("Salir"),
}


def mostrar_Menu():
    # Muestro el menu con un formato bonito en color amarillo
    print("\033[33m MENU PRINCIPAL \033[0m".center(50, "="))
    for i in range(1, len(menu) + 1):
        print(f"{i}. {menu[i]}")
    


def validar(msg, min=0.0):
    # Funcion para validar las entradas numericas
    while True:
        # match-case es el switch de otros lenguajes
        match msg:
            case "Digite el precio " | "Nuevo precio (0 para no cambiar): ":
                try:
                    n = float(input(msg))
                    if n < min:
                        print(f"Debe ingresar un numero mayor o igual que {min}")
                        continue
                    return n
                except ValueError:
                    print("El dato ingresado es invalido, Intente nuevamente")
            
            case "Digite la cantidad " | "Nueva cantidad (0 para no cambiar): ":
                try:
                    n = int(input(msg))
                    if n < min:
                        print(f"Debe ingresar un numero mayor o igual que {min}")
                        continue
                    return n
                except ValueError:
                    print("El dato ingresado es invalido, Intente nuevamente")        


def main():
    # Creo una instancia del inventario
    inventario = Inventario()

    while True:
        try:
            mostrar_Menu()
            opcion = input("Seleccione una opcion (1-9) ").strip()
            
            if opcion == "1":
                # Agrego producto nuevo
                nombre = str(input("Digite el nombre del producto ")).strip()
                cantidad = validar("Digite la cantidad ", 0)
                precio = validar("Digite el precio ", 0)
                inventario.agregar_producto(nombre, cantidad, precio)

            elif opcion == "2":
                # Muestro inventario completo
                inventario.mostrar_inventario()

            elif opcion == "3":
                #  Busco producto por nombre
                nombre = str(input("Digite el nombre del producto a buscar: ")).strip()
                p = inventario.buscar_producto(nombre)
                print(p if p else "❌ Producto no encontrado")

            elif opcion == "4":
                # Actualizo los datos de un producto
                nombre = str(input("Digite el nombre del producto a actualizar: ")).strip()
                p = inventario.buscar_producto(nombre)
                if p:
                    nuevo_precio = validar("Nuevo precio (0 para no cambiar): ", 0)
                    nueva_cantidad = validar("Nueva cantidad (0 para no cambiar): ", 0)
                    inventario.actualizar_producto(
                        nombre,
                        nuevo_precio if nuevo_precio != 0 else None,
                        nueva_cantidad if nueva_cantidad != 0 else None,
                    )
                else:
                    print("❌ Producto no encontrado")

            elif opcion == "5":
                # Elimino un producto por nombre
                nombre = input("Nombre del producto a eliminar: ")
                inventario.eliminar_producto(nombre)

            elif opcion == "6":
                # Muestro las estadísticas del inventario
                inventario.calcular_estadisticas()

            elif opcion == "7":
                # Guardo el inventario actual en un archivo JSON
                archivo_inventario.guardar_csv(inventario.productos)

            elif opcion == "8":
                # Cargo productos desde el archivo JSON y los fusiono con el inventario actual si es necesario
                inventario.productos = archivo_inventario.cargar_json(inventario)

            elif opcion == "9":
                # Salir del programa
                print("Saliendo del programa.....")
                break

            else:
                # Opcion que no es valida
                print("Opción no válida, intente nuevamente.")
        
        except (Exception, ValueError, KeyboardInterrupt) as e:
            # Si ocurre un error 
            print(f"\nError: Entrada invalida o interrupcion detectada")
            continue
        
        
# Entrada del programa
if __name__ == "__main__":
    main()
