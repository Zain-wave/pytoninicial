chocolate = 4000
vainilla = 3500

topping = 1000

print("Helados y precios ".center(50,"="))
print("chocolate → $4.000")
print("vainilla → $3.500")


sabor = str(input("Que sabor de Helado deseas? ")).strip()

if sabor == "chocolate":
    toppi = input("Lo desea con topping? y/n ")
    if toppi == "y":
        print(f"precio total de su helado de {sabor} es: {topping+chocolate}")
    else:
        print(f"precio total de su helado de {sabor} es: {chocolate}")
elif sabor == "vainilla":
    toppi = input("Lo desea con topping? y/n ")
    if toppi == "y":
        print(f"precio total de su helado de {sabor} es: {topping+vainilla}")
    else:
        print(f"precio total de su helado de {sabor} es: {vainilla}")
else:
    print("El sabor de helado no es valido ")
    pass