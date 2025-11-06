horas = float(input("Ingrese el número de horas: "))

if horas < 0:
    print("Error: número de horas inválido.")
else:
    tarifa_por_hora = 2000
    if horas <= 5:
        total = horas * tarifa_por_hora
    else:
        total = (horas * tarifa_por_hora) + 5000  # multa fija

    print(f"Total a pagar: ${total:.0f}")
