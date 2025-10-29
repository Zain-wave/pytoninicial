#Binario a decimal
def Binario(bina):
    decimal = 0      
    potencia = 0     # Representa la posición

    # Recorro alrevez para poder convertir
    for digito in reversed(bina):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1 

    return decimal


# Decimal a Binario
def Decimal(deci):
    binario = "" 

    # Mientras el número sea mayor que cero
    while deci > 0:
        residuo = deci % 2
        binario = str(residuo) + binario  # Agrego el residuo al inicio
        deci = deci // 2

    return binario


num_Decimal = int(input("Dijita el número decimal: "))

def validar_Binario(bin_Ingresado):
    for digito in bin_Ingresado:
        if digito not in "01":
            return False
    return True

while True:
    num_Binario = input("Dijita el número binario: ")
    if validar_Binario(num_Binario):
        break
    else:
        print("Error: Solo puedes ingresar digitos 1 o 0") 
print(f"El número binario {num_Binario} convertido a decimal es {Binario(num_Binario)}")
print(f"El número decimal {num_Decimal} convertido a binario es {Decimal(num_Decimal)}")
