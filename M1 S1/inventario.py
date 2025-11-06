def pedir_nombre(prompt="Digite nombre del artículo: "):
    while True:
        nombre = input(prompt).strip()
        if nombre:
            return nombre
        print("Nombre inválido. Intenta nuevamente.")


def pedir_precio(prompt="Digite el precio (ej: 12.50): "):
    while True:
        texto = input(prompt).strip()
        try:
            precio = float(texto)
            if precio >= 0:
                return precio
            else:
                print(" El precio no puede ser negativo.")
        except ValueError:
            print("Precio inválido. Usa un número decimal. Ej: 12.50")


def pedir_cantidad(prompt="Digite la cantidad (ej: 7): "):
    while True:
        texto = input(prompt).strip()
        try:
            cantidad = int(texto)
            if cantidad >= 0:
                return cantidad
            else:
                print(" La cantidad debe ser mayor o igual a 0.")
        except ValueError:
            print("Cantidad inválida. Usa un número entero. Ej: 7")


def main():
    print("=== Registro de producto en inventario ===")
    
    nombre = pedir_nombre()
    precio = pedir_precio()
    cantidad = pedir_cantidad()
    costo_total = precio * cantidad

    print("\n✅ Registro exitoso:")
    print(f"Artículo: {nombre}")
    print(f"Precio unitario: ${precio:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Costo total: ${costo_total:.2f}")


if __name__ == "__main__":
    main()
