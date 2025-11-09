#agregar estudiantes
#mostrar todos los estudiantes y sus promedios
#mostrar mejor estudiante
#salir

# key value
#nombre nota
# {
#     ana : 5,
#     marcela: 5
# }


def agregar_estudiante(estudiantes):
    nombre = input("Nombre del estudiante")
    if nombre == "":
        print("nombre no puede estar vacio")
        return

    try:
        cantidad = int(input("cuantas notas quieres ingresar"))
        if cantidad <= 0:
            print("la cantidad debe ser mayor que 0")
            return
    except ValueError:
        print("Debe ingresar un numero valido")
        return

    notas = []
    for i in range(cantidad):
        while True:
            try:
                nota = float(input(f"Dijite la nota {i+1}"))
                
                if 0 <= nota <= 5:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 5")
                
            except ValueError:
                print("Debe ingresar un numero valido")
                return
            
    promedio = sum(notas)/len(notas)
    estudiantes[nombre] = promedio
    print(f"estudiante {nombre} agregado exitosamente con promedio {promedio}")

    


def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes")
        return
    
    for nombre, promedio in estudiantes.items():
        print(f"{nombre} --> {promedio}")



def mostrar_mejor_promedio(estudiantes):
    if not estudiantes:
        print("No hay estudiantes")
        return
    mejor = max(estudiantes, key=estudiantes.get)
    print(f"el mejor promedio es de {mejor} con {estudiantes[mejor]}")





estudiantes = {}
while True:
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. mostrar mejor estudiante")
    print("4. salir")
    
    
    opcion = input("Elije una opcion")
    
    if opcion == "1":
        agregar_estudiante(estudiantes)
    elif opcion == "2":
        mostrar_estudiantes(estudiantes)
    elif opcion == "3":
        mostrar_mejor_promedio(estudiantes)
    elif opcion == "4":
        print("Saliendo")
        break
    else:
        print("Opcion no valida")
