def formato_mensaje(func):
    """Agrega un mensaje formateado al agregar un producto."""
    def wrapper(self, *args, **kwargs):
        resultado = func(self, *args, **kwargs)
        print("✅ Producto agregado o actualizado correctamente.\n")
        return resultado
    return wrapper

#clase usadad para definir los productos
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self. cantidad = cantidad
        self.precio = precio
        
    def __str__(self):
        #metodo que permite imprimir cada producto en cuestion
        return f"{self.nombre} | Cantidad: {self.cantidad}  | Precio: {self.precio}"

    #funcion que permite calcular el valor total de cada producto
    def valor_total(self):
        return self.cantidad * self.precio


#Objeto que almacena todo lo relacionado a los productos 
class Inventario:
    def __init__(self):
        self.productos = {}
        
    #Funcion para agregar productos al inventario
    @formato_mensaje  
    def agregar_Productos(self, nombre, cantidad, precio):
        if nombre in self.productos:
            # Si ya existe, se actualiza la cantidad
            self.productos[nombre].cantidad += cantidad
            # También podrías actualizar el precio si cambió:
            self.productos[nombre].precio = precio
        else:
            nuevo = Producto(nombre, cantidad, precio)
            self.productos[nombre] = nuevo
    
    #Funcion para mostrar productos existentes
    def mostrar_Productos(self):
        #En caso de que no exista ningun producto
        if not self.productos:
            print("No hay productos en el inventario")
            return
        #En caso de que exista producto se recorre el diccionario productos y se imprime cada uno
        #siendo i la posicion de el producto y siendo p el producto en cuestion(se imprime correctamente gracias a __str__ definido en el producto) 
        for i, p in enumerate(self.productos.values(), 1):
            print(f"{i}, {p}")
            
    #Funcion para calcular informacion de los productos en memoria        
    def calcular_Estadistica(self):
        if not self.productos:
            print("No hay productos en el inventario")
            return
        
        total_productos = len(self.productos)
        total_unidades = sum(p.cantidad for p in self.productos.values())
        valor_total =  sum(p.valor_total() for p in self.productos.values())
        
        print(f"El total de productos es: {total_productos}")
        print(f"Total de unidades: {total_unidades}")
        print(f"Valor total de el inventario: {valor_total}")

def main():
    inventario = Inventario()
    while True:
        print("1. Agregar Producto")
        print("2. Ver Inventario")
        print("3. Calcular estadistica")
        print("4. Salir")
    
        opcion = input("Dijite una opcion ")
        if opcion == "1":
            try:
                nombre = str(input("Digite el nombre del producto "))
                cantidad = int(input("Digite la cantidad "))
                precio = float(input("Digite el precio "))
                inventario.agregar_Productos(nombre, cantidad, precio)
            except ValueError as e:
                print(e)
        elif opcion == "2":
            inventario.mostrar_Productos()
        elif opcion == "3":
            inventario.calcular_Estadistica()
        elif opcion == "4":
            print("Saliendo del programa.....")
            break
        else:
            print("Opcion Invalida")

if __name__ == "__main__":
    main()
