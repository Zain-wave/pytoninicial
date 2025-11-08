class Movie:
    def __init__(self, nombre, precio, cantidad):
        # Inicializo los datos básicos del producto
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def subtotal(self):
        # Calculo el valor total del producto (precio * cantidad)
        return self.precio * self.cantidad

    def __str__(self):
        # Devuelve una cadena con la info del producto para mostrar más fácil
        return f"{self.nombre} - Precio: ${self.precio:.2f} - Cantidad: {self.cantidad}"