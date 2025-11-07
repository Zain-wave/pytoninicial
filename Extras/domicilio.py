#ROJO \033[0m
#VERDE 
productos = {
    1: ("Hamburguesa", 15000),
    2: ("Perro caliente", 12000),
    3: ("Pizza personal", 18000),
    4: ("Gaseosa", 4000),
    5: ("Papas fritas", 6000)
}

def mostrar_menu():
    print("\033[33m MENÚ DE PRODUCTOS \033[0m".center(50,"="))
    for i in range(1, len(productos) + 1):
            print(f"{i}. {productos[i][0]} - ${productos[i][1]:,.2f}")
            

def solicitar_domicilio(productos):
    print("\033[33m SISTEMA DE DOMICILIOS \033[0m".center(50,"="))

    # Datos del cliente
    nombre = input("Nombre completo: ")
    telefono = input("Número de teléfono: ")
    direccion = input("Dirección de entrega: ")


    pedido = []
    total = 0

    # Selección de productos
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona un producto (1-5) o 0 para finalizar: "))
            
        except ValueError:
            print("⚠️ Ingresa un número válido.\033[0m")
            continue


        if opcion == 0:
            break
        elif opcion in productos:
            cantidad = int(input(f"Ingrese la cantidad de {productos[opcion][0]}: "))
            subtotal = productos[opcion][1] * cantidad
            pedido.append((productos[opcion][0], cantidad, subtotal))
            total += subtotal
            print(f"✅ Agregado {cantidad} x {productos[opcion][0]} = ${subtotal:,.0f}\n")
        else:
            print("❌ \033[31mOpción no válida, intenta de nuevo.\033[0m\n")

    if not pedido:
        print("\033[31mNo se agregaron productos. Pedido cancelado.\033[0m")
        return

    # Método de pago
    print("\n=== MÉTODO DE PAGO ===")
    print("1. Efectivo")
    print("2. Transferencia")
    metodo = input("Selecciona una opción (1 o 2): ")

    if metodo == "1":
        metodo_pago = "Efectivo"
        valor_pago = float(input("Monto con el que paga: "))
        cambio = valor_pago - total
    elif metodo == "2":
        metodo_pago = "Transferencia"
        valor_pago = total
        cambio = 0
    else:
        print("Opción inválida, se asignará 'Efectivo'.")
        metodo_pago = "Efectivo"
        valor_pago = total
        cambio = 0

    # Resumen del pedido
    print("\n RESUMEN DEL PEDIDO ".center(50,"="))
    print(f"Cliente: {nombre}")
    print(f"Teléfono: {telefono}")
    print(f"Dirección: {direccion}")
    print("\nProductos:")
    for p in pedido:
        print(f"  - {p[1]} x {p[0]} = ${p[2]:,.0f}")
    print(f"\nTotal a pagar: ${total:,.0f}")
    print(f"Método de pago: {metodo_pago}")
    print(f"Valor entregado: ${valor_pago:,.0f}")
    print(f"Cambio: ${cambio:,.0f}")
    print("\n✅ ¡Gracias por su pedido! En breve será entregado.")



def main():
    while True:
        try:
            solicitar_domicilio(productos)
        except (Exception, ValueError, KeyboardInterrupt) as e:
            print (f"\n\033[31mError: Entrada invalida o interrupcion detectada\033[0m")
            continue
    

if __name__ == "__main__":
    main()