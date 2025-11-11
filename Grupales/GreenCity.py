import datetime

TARIFA_N = 500 
TARIFA_P = 750
PENALIZACION = 2000

#Funcion para realizar el alquiler
def realizar_alquiler(FINDE):
    while True:
        print("\n Selección de Bicicleta")
        print(f"1. Estándar ${TARIFA_N}")
        print(f"2. Premium ${TARIFA_P}")
        opcion_bici = input("Elige el tipo de bicicleta (1 o 2): ")
        
        if opcion_bici == '1':
            tipo_bicicleta = "Estándar"
            costo_por_minuto = TARIFA_N
            break
        elif opcion_bici == '2':
            tipo_bicicleta = "Premium"
            costo_por_minuto = TARIFA_P
            break
        else:
            print("Opcion no valida. Por favor, selecciona 1 o 2.")
            
    tiempo_uso = 0
    while True:
        try:
            tiempo_uso = int(input("Ingresa el tiempo de uso en minutos: "))
            if tiempo_uso > 0:
                break
            else:
                print("Ingresa un numero positivo/entero")
        except ValueError:
            print("Debe ingresar numeros")
            
    metodo_pago = "" 
    while True:
        print("\n--- Método de Pago ---")
        print("1. Efectivo")
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
            
    # Calcular total
    datos = calculate(tipo_bicicleta, metodo_pago, tiempo_uso, costo_por_minuto, FINDE, PENALIZACION)
    
    print(mostrar(*datos))

    
def calculate(ride: str, payment_method: str, time: int, base_amount: int, day: bool, penalty: int):
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
        
    if time > 120:
        penaltyBool = True
        total_cost += penalty  # penalización

    return [ride, time, base_amount, discount, penaltyBool, surcharge, total_cost]


def mostrar(ride, time, base_amount, discount, penalty, surcharge, total_cost):
    text = f"""El tipo de bicicleta fue: {ride}
El tiempo de uso fue: {time} minutos
Con un precio base de: ${base_amount} por minuto\n"""
    if discount:
        text += "Descuento aplicado: 10%\n"
    if surcharge:
        text += "Recargo por fin de semana: 5%\n"
    if penalty:
        text += f"Penalización por demora: ${PENALIZACION}\n"

    text += f"\nVALOR TOTAL A PAGAR: ${total_cost}"
    return text


def consultar_tarifas(FINDE):

    print("\n Tarifas del Servicio")
    
    print("\n Tarifas Base (Por minuto)")
    print(f"* Bicicleta Estándar: ${TARIFA_N}")
    print(f"* Bicicleta Premium:  ${TARIFA_P}")
    
    print("\n Descuentos y Recargos")
    print("Descuento por Tarjeta: 10% de descuento si el pago es con **Tarjeta** y el tiempo de uso es de **60 minutos o más**.")
    
    estado_finde = "APLICA" if FINDE else "NO APLICA"
    print(f"* Recargo por Fin de Semana (5%):** Actualmente *{estado_finde}*.")
    print("* Pago con Puntos:** No aplica descuentos ni recargos adicionales.")

    print("\n Penalización por Tiempo")
    print(f"* Se aplica una **Penalización por Demora** de **$ {PENALIZACION}** si el tiempo de uso supera los **120 minutos**.")


def main():
    hoy = datetime.datetime.now()
    dia_semana = hoy.weekday() #pone numeros a los dias
    
    FINDE = dia_semana >= 5 

    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    nombre_dia = dias[dia_semana]
    
    print(f" Hoy es {nombre_dia}. Recargo por fin de semana: {'SÍ (5%)' if FINDE else 'NO (0%)'}")
    # ----------------------------------------------
    try:
        while True:
            print("\n Principal ")
            print("1. Alquilar Bicicleta")
            print("2. Consultar Tarifas")
            print("3. Salir del Sistema") 
            
            opcion = input("Selecciona una opción (1, 2 o 3): ")

            if opcion == '1':
                realizar_alquiler(FINDE) 
                while True:
                    otra_vez = input("¿Deseas realizar otro alquiler (s/n)? ").lower()
                    if otra_vez == 'n':
                        print("¡Gracias por usar el sistema de alquiler!")
                        return
                    elif otra_vez == 's':
                        break 
                    else:
                        print("Respuesta no válida. Por favor, ingresa 's' o 'n'.")
                        
            elif opcion == '2':
                consultar_tarifas(FINDE) 
                
            elif opcion == '3':
                print("¡Gracias por usar el sistema de alquiler!")
                break
                
            else:
                print("\n Opción no válida. Por favor, selecciona 1, 2 o 3.")
    except KeyboardInterrupt:
        print("\n No funciona esa tecla papi")
        

if __name__ == "__main__":
    main()