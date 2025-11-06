pan = 300
cantidad = int(input("Digite la cantidad de panes a comprar "))  

def compra(cantidad, precio):
    total = cantidad * precio
    if cantidad < 0:
        print("Cantidad invalida")
    elif cantidad > 50:
        descuento = 0.20
    elif cantidad > 20:
        descuento = 0.10
    else:
        descuento = 0
    
    return  total - (total*descuento)
    
print(compra(cantidad, pan))