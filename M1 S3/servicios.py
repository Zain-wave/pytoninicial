class Producto:
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


class Inventario:
    def __init__(self):
        # La lista donde voy a guardar todos los productos
        self.productos = []
    
    
    def agregar_producto(self, nombre, cantidad, precio):
        # Agrego un producto nuevo o actualiza si ya existe
        existente = self.buscar_producto(nombre)
        if existente:
            # Si ya existe, sumo las cantidades y actualizo el precio
            existente.cantidad += cantidad
            existente.precio = precio
            print(f"✅ Producto '{nombre}' actualizado")
        else:
            # Si no existe, lo creo y lo agrego a la lista
            self.productos.append(Producto(nombre, precio, cantidad))
            print(f"✅ Producto '{nombre}' agregado al inventario.")

    def mostrar_inventario(self):
        # Muestro todos los productos del inventario
        if not self.productos:
            print("Inventario vacío.")
            return
        print("\n Inventario actual:")
        for p in self.productos:
            print(" -", p)

    def buscar_producto(self, nombre):
        # Busco un producto por nombre (sin importar mayúsculas)
        for p in self.productos:
            if p.nombre.lower() == nombre.lower():
                return p
        return None
    
    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        # Actualizo el precio y/o cantidad de un producto
        p = self.buscar_producto(nombre)
        if not p:
            print(f"❌ Producto '{nombre}' no encontrado.")
            return
        if nuevo_precio is not None:
            p.precio = nuevo_precio
        if nueva_cantidad is not None:
            p.cantidad = nueva_cantidad
        print(f"✅ Producto '{nombre}' actualizado correctamente.")

    def eliminar_producto(self, nombre):
        # Elimino un producto del inventario por su nombre
        p = self.buscar_producto(nombre)
        if p:
            self.productos.remove(p)
            print(f"Producto '{nombre}' eliminado.")
        else:
            print(f"❌ Producto '{nombre}' no encontrado.")

    def calcular_estadisticas(self):
        # Muestro estadísticas generales del inventario
        if not self.productos:
            print("Inventario vacío.")
            return

        # Total de unidades sumando todas las cantidades
        unidades_totales = sum(p.cantidad for p in self.productos)
        # Suma del valor total del inventario
        valor_total = sum(p.subtotal() for p in self.productos)
        # Producto más caro
        producto_mas_caro = max(self.productos, key=lambda p: p.precio)
        # Producto con más unidades en stock
        producto_mayor_stock = max(self.productos, key=lambda p: p.cantidad)
        
        print("\n📊 Estadísticas del inventario:")
        print(f"Unidades totales: {unidades_totales}")
        print(f"Valor total: ${valor_total:,.2f}")
        print(f"Producto más caro: {producto_mas_caro.nombre} (${producto_mas_caro.precio:.2f})")
        print(f"Producto con más stock: {producto_mayor_stock.nombre} ({producto_mayor_stock.cantidad} unidades)")
