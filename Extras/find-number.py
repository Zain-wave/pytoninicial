import random

def adivina_el_numero():
    print(" Bienvenido al juego: Adivina el número ")
    #randint genera un numero aleatorio entero
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("Adivina un número entre 1 y 100: "))
        intentos += 1

        if intento < numero_secreto:
            print("Muy bajo 📉")
        elif intento > numero_secreto:
            print("Muy alto 📈")
        else:
            print(f"¡Correcto! 🎉 Lo lograste en {intentos} intentos.")
            break

adivina_el_numero()
