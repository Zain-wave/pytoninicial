def es_par(numero):
    return numero % 2 == 0 #Devuelve True si el número es par

def mostrar_pares_impares(n):
    pares = 0
    impares = 0
    i = 0

    while i <= n:
        if es_par(i):
            print(f"{i} es PAR")
            pares += 1
        else:
            print(f"{i} es IMPAR")
            impares += 1
        i += 1

    print("\n📊 Resultado final:")
    print(f"Total de números analizados: {n + 1}")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")


def main():
    print("=== Verificador de números pares e impares ===")
    limite = int(input("Ingresa un número: "))
    mostrar_pares_impares(limite)


if __name__ == "__main__":
    main()
#lo corro directamente