import json
from servicios import Inventario

ARCHIVO = "productos.json"

inv = Inventario()
class archivo_inventario:
    
    def guardar_csv(inventario):
        if not inventario:
            print("No hay nada guardado en el inventario")
            return
        try:
            datos = []
            for producto in inventario:
                datos.append({
                    "nombre": producto.nombre,
                    "cantidad": producto.cantidad,
                    "precio": producto.precio
                })

            # Guardar en el archivo JSON
            with open(ARCHIVO, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)

            print("\033[32mInventario guardado correctamente en productos.json\033[0m")
            
            
            
        except (Exception, ValueError, KeyboardInterrupt) as e:
            print (f"\n\033[31mError: Entrada invalida o interrupcion detectada\033[0m")
            

    def cargar_json():
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                datos = json.load(f)
                inventario = []
                for d in datos:
                    inventario.append(inv.agregar_producto(d["nombre"], d["cantidad"], d["precio"]))
                    print(datos)
                    print(inventario)
                return inventario
        except FileNotFoundError:
            print("No se encontró el archivo de inventario.")
            return []
