class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def subtotal(self):
        #Calcula el valor total del producto (precio * cantidad)
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f} - Cantidad: {self.cantidad}"

class Inventario:
    def __init__(self):
        self.productos = []
    
    
    def agregar_producto(self, nombre, cantidad, precio):
        #Agrega un nuevo producto o actualiza si ya existe.
        existente = self.buscar_producto(nombre)
        if existente:
            existente.cantidad += cantidad
            existente.precio = precio
            print(f"✅ Producto '{nombre}' actualizado")
        else:
            self.productos.append(Producto(nombre, precio, cantidad))
            print(f"✅ Producto '{nombre}' agregado al inventario.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        print("\n Inventario actual:")
        for p in self.productos:
            print(" -", p)

    def buscar_producto(self, nombre):
        for p in self.productos:
            if p.nombre.lower() == nombre.lower():
                return p
        return None
    
    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        #Actualiza precio y/o cantidad de un producto
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
        p = self.buscar_producto(nombre)
        if p:
            self.productos.remove(p)
            print(f"Producto '{nombre}' eliminado.")
        else:
            print(f"❌ Producto '{nombre}' no encontrado.")

    def calcular_estadisticas(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        unidades_totales = sum(p.cantidad for p in self.productos)
        valor_total = sum(p.subtotal() for p in self.productos)
        producto_mas_caro = max(self.productos, key=lambda p: p.precio)
        producto_mayor_stock = max(self.productos, key=lambda p: p.cantidad)
        
        print("\n📊 Estadísticas del inventario:")
        print(f"Unidades totales: {unidades_totales}")
        print(f"Valor total: ${valor_total:,.2f}")
        print(f"Producto más caro: {producto_mas_caro.nombre} (${producto_mas_caro.precio:.2f})")
        print(f"Producto con más stock: {producto_mayor_stock.nombre} ({producto_mayor_stock.cantidad} unidades)")
