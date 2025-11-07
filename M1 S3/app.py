from servicios import Inventario
from archivos import archivo_inventario

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
    print("\033[33m MENU PRINCIPAL \033[0m".center(50,"="))
    for i in range(1, len(menu) + 1):
        print(f"{i}. {menu[i]}")
    


def validar(msg, min=0.0):
    while True:
        #match-case es el equivalente a switch en python     
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
    inventario = Inventario()
    while True:
        try:
            mostrar_Menu()
            opcion = input("Seleccione una opcion (1-9) ").strip()
            
            if opcion == "1":
                nombre = str(input("Digite el nombre del producto ")).strip()
                cantidad = validar("Digite la cantidad ", 0)
                precio = validar("Digite el precio ", 0)
                inventario.agregar_producto(nombre, cantidad, precio)
                pass
            elif opcion == "2":
                inventario.mostrar_inventario()
                pass
            elif opcion == "3":
                nombre = str(input("Digite el nombre del producto a buscar: ")).strip()
                p = inventario.buscar_producto(nombre)
                print(p if p else "❌ Producto no encontrado")
            elif opcion == "4":
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
                nombre = input("Nombre del producto a eliminar: ")
                inventario.eliminar_producto(nombre)
            elif opcion == "6":
                inventario.calcular_estadisticas()
            elif opcion == "7":
                archivo_inventario.guardar_csv(inventario.productos)
            elif opcion == "8":
                inventario.productos = archivo_inventario.cargar_json(inventario)
            elif opcion == "9":
                print("Saliendo del programa.....")
                break
            else:
                pass
        except (Exception, ValueError, KeyboardInterrupt) as e:
            print (f"\nError: Entrada invalida o interrupcion detectada")
            continue
        
        
        
if __name__ == "__main__":
    main()