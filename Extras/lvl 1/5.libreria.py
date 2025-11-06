precio_libro = 25000

estudiante = input("¿Eres estudiante? (s/n): ").lower()

if estudiante == "s":
    total = precio_libro * 0.85  # 15% 
    tiene_cupon = input("¿Tienes cupón? (s/n): ").lower()

    if tiene_cupon == "s":
        cupon = input("Ingresa el código del cupón: ").strip()
        if cupon == "LIBRO10":
            total *= 0.90  # 10% adicional sobre el precio ya descontado
        else:
            print("Cupón incorrecto, no se aplica descuento extra.")
else:
    if estudiante == "n":
        total = precio_libro
        print("No aplica descuento de estudiante.")
    else:
        print("Respuesta inválida.")
        total = precio_libro

print(f"Total a pagar: ${total:.0f}")
