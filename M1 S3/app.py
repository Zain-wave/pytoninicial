from servicios import Inventario
#from archivos import ArchivoInventario

def mostrar_Menu():
    print(" MENU PRINCIPAL ".center(50,"="))
    print("1) Agregar Producto")
    print("2) Mostrar Inventario")
    print("3) Buscar Producto")
    print("4) Actualizar Producto")
    print("5) Eliminar Producto")
    print("6) Estadisticas")
    print("7) Guardar CSV")
    print("8) Cargar CSV")
    print("9) Salir")
    


def validar(msg, min=0.0):
    while True:     
        match msg:
            case "Digite el precio ":
                try:
                    n = float(input(msg))
                    if n < min:
                        print(f"Debe ingresar un numero mayor o igual que {min}")
                        continue
                    return n
                except ValueError:
                    print("El dato ingresado es invalido, Intente nuevamente")
            case "Digite la cantidad ":
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
                nombre = str(input("Nombre del producto a actualizar: "))
                nuevo_precio = validar("Nuevo precio (0 para no cambiar): ", 0)
                nueva_cantidad = validar("Nueva cantidad (0 para no cambiar): ", 0)
                inventario.actualizar_producto(
                    nombre,
                    nuevo_precio if nuevo_precio != 0 else None,
                    nueva_cantidad if nueva_cantidad != 0 else None,
                )
            elif opcion == "5":
                nombre = input("Nombre del producto a eliminar: ")
                inventario.eliminar_producto(nombre)

            elif opcion == "6":
                inventario.calcular_estadisticas()
            elif opcion == "7":
                pass
            elif opcion == "8":
                pass
            elif opcion == "9":
                print("Saliendo del programa.....")
                break
            else:
                pass
        except Exception as e:
            print (f"Error {e}")
            continue
        
        
        
if __name__ == "__main__":
    main()