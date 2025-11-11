import datetime

tarifa_n = 500
tarifa_p = 750
penalizacion = 2000

# Guardamos: [tipo_bicicleta, costo_por_minuto, metodo_pago, tiempo_SOLICITADO]
alquiler_activo = []

def realizar_alquiler(finde):
    global alquiler_activo
    
    if alquiler_activo:
        print("\nYa tienes una bicicleta alquilada. Debes DEVOLVERLA primero (Opción 4).")
        return

    while True:
        print(" Selección de Bicicleta ".center(50, "="))
        print(f"\n1. Estándar ${tarifa_n}")
        print(f"2. Premium ${tarifa_p}")
        opcion_bici = input("Elige el tipo de bicicleta (1 o 2): ")

        if opcion_bici == '1':
            tipo_bicicleta = "Estándar"
            costo_por_minuto = tarifa_n
            break
        elif opcion_bici == '2':
            tipo_bicicleta = "Premium"
            costo_por_minuto = tarifa_p
            break
        else:
            print("Opcion no valida. Por favor, selecciona 1 o 2.")

    tiempo_solicitado = 0
    while True:
        try:
            tiempo_solicitado = int(input("Ingresa el tiempo de uso SOLICITADO en minutos: "))
            if tiempo_solicitado > 0:
                break
            else:
                print("Ingresa un numero positivo/entero.")
        except ValueError:
            print("Debe ingresar números.")

    metodo_pago = ""
    while True:
        print(" Método de Pago ".center(50, "="))
        print("\n1. Efectivo")
        print("2. Tarjeta")
        print("3. Puntos")
        opcion_pago = input("Selecciona el método de pago (1, 2 o 3): ")

        if opcion_pago == '1':
            metodo_pago = "cash"
            break
        elif opcion_pago == '2':
            metodo_pago = "card"
            break
        elif opcion_pago == '3':
            metodo_pago = "points"
            break
        else:
            print("Opción de pago no válida.")
            
    alquiler_activo = [tipo_bicicleta, costo_por_minuto, metodo_pago, tiempo_solicitado]
    print(f"\nAlquiler de bicicleta {tipo_bicicleta} registrado por {tiempo_solicitado} minutos.")
    print("Recuerda DEVOLVERLA (Opción 4) al finalizar para realizar el pago.")


def liquidar_alquiler(finde):
    global alquiler_activo
    
    if not alquiler_activo:
        print("\nNo hay un alquiler activo para pagar. Por favor, realiza un alquiler primero (Opción 1).")
        return

    tipo_bicicleta, costo_por_minuto, metodo_pago, tiempo_solicitado = alquiler_activo
    

    tiempo_real_uso = 0
    print(f"\nEl tiempo solicitado inicialmente fue de: {tiempo_solicitado} minutos.")
    while True:
        try:
            # pedimos el tiempo que la persona realmente uso la cicla
            tiempo_real_uso = int(input("Ingresa el tiempo REAL de uso en minutos para la devolución: "))
            if tiempo_real_uso > 0:
                break
            else:
                print("Ingresa un numero positivo/entero.")
        except ValueError:
            print("Debe ingresar números.")

    if tiempo_real_uso > tiempo_solicitado:
        diferencia = tiempo_real_uso - tiempo_solicitado
        print(f"\n Papi se paso por {diferencia} minutos.")
    else:
        print("\n Bicicleta devuelta a tiempo.")
        
    datos = calculate(tipo_bicicleta, metodo_pago, tiempo_real_uso, tiempo_solicitado, costo_por_minuto, finde, penalizacion)


    print(" Recibo ".center(50, "="))
    print(f"\n{mostrar(*datos)}\n")
    print("".center(50, "="))
    
    alquiler_activo = []
    print("\nLiquidación completada. Alquiler cerrado. \n")
    
def calculate(ride: str, payment_method: str, time: int, tiempo_solicitado: int, base_amount: int, day: bool, penalty: int):
    total_cost = base_amount * time
    discount = False
    surcharge = False
    penaltyBool = False

    if payment_method == "card" and time >= 60:
        discount = True
        total_cost -= total_cost * 0.1  # 10%
    if payment_method == "points" and time < 10:
        pass
    if day:
        surcharge = True
        total_cost += total_cost * 0.05  # 5% de recargo por fin de semana

    if time > tiempo_solicitado:
        penaltyBool = True
        total_cost += penalty  # penalización

    return [ride, time, base_amount, discount, penaltyBool, surcharge, total_cost]


def mostrar(ride, time, base_amount, discount, penalty, surcharge, total_cost):
    text = f"""El tipo de bicicleta fue: {ride}
El tiempo de uso REAL fue: {time} minutos
Con un precio base de: ${base_amount} por minuto\n"""
    if discount:
        text += "Descuento aplicado: 10%\n"
    if surcharge:
        text += "Recargo por fin de semana: 5%\n"
    if penalty:
        text += f"Penalización por demora (Excedió el tiempo solicitado): ${penalizacion}\n"

    text += f"\nVALOR TOTAL A PAGAR: ${total_cost:.2f}" 
    return text

def consultar_tarifas(finde):
    print("\n Tarifas del Servicio")

    print("\n Tarifas Base (Por minuto)")
    print(f"* Bicicleta Estándar: ${tarifa_n}")
    print(f"* Bicicleta Premium:  ${tarifa_p}")

    print("\n Descuentos y Recargos")
    print(" Descuento por Tarjeta: 10% de descuento si el pago es con ´Tarjeta´ y el tiempo de uso es de 60 minutos o más.")

    estado_finde = "APLICA" if finde else "NO APLICA"
    print(f" Recargo por Fin de Semana (5%): Actualmente {estado_finde}.")
    print(" Pago con Puntos: No aplica descuentos ni recargos adicionales.")

    print("\n Penalización por Tiempo")
    print(f" Se aplica una Penalización por Demora de $ {penalizacion} si el tiempo de uso supera el tiempo solicitado.")


def main():
    hoy = datetime.datetime.now()
    dia_semana = hoy.weekday() #pone numeros a los dias

    finde = dia_semana >= 5

    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    nombre_dia = dias[dia_semana]

    print(f" Hoy es {nombre_dia}. Recargo por fin de semana: {'SÍ (5%)' if finde else 'NO (0%)'}")
    # ----------------------------------------------

    opciones = [
        " Menu Principal ".center(50, "="),
        "\n1. Alquilar Bicicleta",
        "2. Consultar Tarifas",
        "3. Salir del Sistema (Solo si no hay alquiler activo)",
        "4. Devolver Bicicleta (PAGO)"
    ]

    try:
        while True:
            for opcion in opciones:
                print(opcion)

            seleccion = input("\n Selecciona una opción (1, 2, 3 o 4): ")

            if seleccion == '1':
                realizar_alquiler(finde)

            elif seleccion == '2':
                consultar_tarifas(finde)

            elif seleccion == '4':
                liquidar_alquiler(finde)
                
            elif seleccion == '3':
                if alquiler_activo:
                    print("\n Debes DEVOLVER y pagar el alquiler activo primero (Opción 4).")
                    continue 
                else:
                    print("Gracias vuelva pronto")
                    break

            else:
                print("\n Opción no válida. Por favor, selecciona 1, 2, 3 o 4.")
    except KeyboardInterrupt:
        print("\n No funciona esa tecla aquí")


if __name__ == "__main__":
    main()