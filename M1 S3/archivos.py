import json
from servicios import Inventario

ARCHIVO = "productos.json"

inv = Inventario()

class archivo_inventario:
    
    # Guardo los productos del inventario en el archivo JSON
    def guardar_csv(inventario):
        # Si el inventario está vacío, no guardo nada
        if not inventario:
            print("No hay nada guardado en el inventario")
            return
        
        try:
            datos = []
            # Recorro cada producto y lo paso a diccionario
            for producto in inventario:
                datos.append({
                    "nombre": producto.nombre,
                    "cantidad": producto.cantidad,
                    "precio": producto.precio
                })

            # Abro el archivo y guardo todo el inventario en formato JSON
            with open(ARCHIVO, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)

            # Mensaje verde cuando todo sale bien
            print("\033[32mInventario guardado correctamente en productos.json\033[0m")
            
        except (Exception, ValueError, KeyboardInterrupt):
            # Si algo falla (error o Ctrl + C), muestro mensaje en rojo
            print(f"\n\033[31mError: Entrada invalida o interrupcion detectada\033[0m")



    # Método estático: no usa self ni nada de la clase, solo lo que le paso
    @staticmethod
    def cargar_json(inventario_actual):
        try:
            # Abro el archivo y cargo los productos guardados
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                datos = json.load(f)

            # Recorro los productos que vienen del archivo
            for d in datos:
                nombre = d["nombre"]
                cantidad = int(d["cantidad"])
                precio = float(d["precio"])

                # Verifico si ya existe en el inventario actual
                existente = inventario_actual.buscar_producto(nombre)

                if existente:
                    # Si ya existe, sumo cantidades y actualizo el precio
                    existente.cantidad += cantidad
                    existente.precio = precio
                    print(f"🔄 Producto '{nombre}' actualizado con datos del archivo.")
                else:
                    # Si no existe, agrego el producto
                    inventario_actual.agregar_producto(nombre, cantidad, precio)

            # Mensaje verde de éxito
            print(f"\033[32mProductos cargados y fusionados correctamente desde {ARCHIVO}\033[0m")
            return inventario_actual.productos

        except FileNotFoundError:
            # Si el archivo no existe, aviso
            print("\033[31mNo se encontró el archivo de inventario.\033[0m")
            return []

        except json.JSONDecodeError:
            # Si el archivo JSON está dañado o mal escrito
            print("\033[31mError al leer el archivo: formato JSON inválido.\033[0m")
            return []
