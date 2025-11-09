import os
import time
from seating import SalaDeCine

START_MENU = {
    1: "Administrador",
    2: "Empleado",
    3: "Salir"
}

ADMIN_MENU = {
    1: "Agregar pelicula",
    2: "Modificar pelicula",
    3: "Eliminar pelicula",
    4: "Estadisticas",
    5: "Volver al menú principal"
}

EMPLOYEE_MENU = {
    1: "Comprar boletos",
    2: "Cambiar boletos",
    3: "Reembolso",
    4: "Lista peliculas",
    5: "Volver al menú principal"
}

# --------------------------------------------------------------------------------------------------------------------

def _mostrar_menu(menu: dict, titulo: str):
    os.system("cls" if os.name == "nt" else "clear")
    
    print(f"\n--- 🍿 {titulo} ---")
    for key, value in menu.items():
        print(f"{key}. {value}")
    print("-------------------------")

def _obtener_opcion(rango_max: int) -> int:
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= rango_max:
                return opcion
            else:
                print(f"❌ Opción inválida. Ingrese un número entre 1 y {rango_max}.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingrese un número.")

# --------------------------------------------------------------------------------------------------------------------

def _comprar_boletos_flow(peliculas_obj_list: list):
    if not peliculas_obj_list:
        print("⚠️ No hay películas cargadas para la venta de boletos. Volviendo en 3 segundos...")
        time.sleep(3) 
        return

    print("\n--- 🎬 Películas en Cartelera ---")
    for i, pelicula in enumerate(peliculas_obj_list):
        print(f"{i + 1}. {pelicula.titulo}") 
    print("-----------------------------------")


    try:
        opcion_pelicula = _obtener_opcion(len(peliculas_obj_list))
        pelicula_seleccionada = peliculas_obj_list[opcion_pelicula - 1]
    except IndexError:
        print("❌ Selección fuera de rango. Volviendo al menú anterior en 2 segundos...")
        time.sleep(2)
        return
    
    print(f"\n✅ Seleccionaste: '{pelicula_seleccionada.titulo}'")
    
    sala = SalaDeCine(pelicula_seleccionada.titulo)
    print("\n--- 💺 Pantalla de Selección de Asientos (Presiona 'q' para confirmar o salir) ---")
    asientos_seleccionados = sala.seleccionar_asientos()
    
    if asientos_seleccionados:
        print(f"🎉 Boletos comprados para {pelicula_seleccionada.titulo}: {len(asientos_seleccionados)} asientos.")
        print(f"Asientos seleccionados: {asientos_seleccionados}")
    else:
        print("🤷‍♂️ No se seleccionaron asientos. Volviendo al menú anterior en 2 segundos...")
        time.sleep(2)
        
        
# ------------------------------------------------------------------------



def menu_administrador_flow():
    while True:
        _mostrar_menu(ADMIN_MENU, "Menú Administrador")
        opcion = _obtener_opcion(len(ADMIN_MENU))
        
        if opcion == 5:
            break
        
        print(f"🛠️ [Admin] Seleccionaste: {ADMIN_MENU[opcion]}. Lógica a implementar.")
        # Aquí se ejecutaría la lógica (agregar_pelicula, etc.)


def menu_empleado_flow(peliculas_obj_list: list):
    while True:
        _mostrar_menu(EMPLOYEE_MENU, "Menú Empleado")
        opcion = _obtener_opcion(len(EMPLOYEE_MENU))
        
        if opcion == 5:
            break
        
        if opcion == 1:
            print(f"🎟️ Seleccionaste: {EMPLOYEE_MENU[opcion]}")
            _comprar_boletos_flow(peliculas_obj_list) 
        else:
            print(f"🎟️ [Empleado] Seleccionaste: {EMPLOYEE_MENU[opcion]}. Lógica a implementar.")
            
# --------------------------------------------------------------------------------------------------------------------


def iniciar_programa(lista_objetos_peliculas: list):
    print("✨ Bienvenido al Sistema de Gestión de Cine ✨")
    
    while True:
        _mostrar_menu(START_MENU, "Menú Principal")
        opcion = _obtener_opcion(len(START_MENU))
        
        if opcion == 1:
            menu_administrador_flow()
        elif opcion == 2:
            menu_empleado_flow(lista_objetos_peliculas)
        elif opcion == 3:
            print("👋 ¡Gracias por usar el sistema! Saliendo...")
            break