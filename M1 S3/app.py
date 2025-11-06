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
                inventario.agregar_Productos(nombre, cantidad, precio)
                print("Producto agregado exitosamente")
                pass
            elif opcion == "2":
                #inventario.mostrar()
                pass
            elif opcion == "3":
                nombre = str(input("Digite el nombre del producto a buscar: ")).strip()
                p = inventario.buscar_nombre(nombre)
                p = ""
                print(p if p else "Producto no encontrado")
            elif opcion == "4":
                pass
            elif opcion == "5":
                pass
            elif opcion == "6":
                pass
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