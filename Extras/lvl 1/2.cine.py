
edad = int(input("Digite la edad del cliente "))

if edad < 4:
    print("Entrada gratis")
elif edad <= 11:
    print("$4.000")
elif edad <= 59:
    print("$8.000")
elif edad > 60:
    print("$4.000 (descuento adulto mayor)")
    