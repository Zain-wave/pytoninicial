from api import obtener_peliculas_populares
from movies import Movie

from menu_manager import iniciar_programa


def crear_objetos_peliculas(datos_peliculas: list) -> list:
    lista_objetos_peliculas = []
    for datos in datos_peliculas:
        pelicula_obj = Movie(
            titulo=datos.get("original_title", "Título Desconocido"),
            genero=datos.get("genre_ids", "Sin Género"),
            sinopsis=datos.get("overview", "Sin sinopsis disponible."),
            image=datos.get("backdrop_path" or "poster_pat", "No Image URL")
        )
        lista_objetos_peliculas.append(pelicula_obj)
    return lista_objetos_peliculas

def main():
    #seating()
    
    datos_peliculas = obtener_peliculas_populares(10)
    lista_objetos_peliculas = crear_objetos_peliculas(datos_peliculas)
    
    iniciar_programa(lista_objetos_peliculas)
    
    # datos_peliculas = obtener_peliculas_populares(10)
    
    # lista_objetos_peliculas = []
    # for datos in datos_peliculas:
    #     # Aquí creamos el objeto Movie usando los datos del diccionario
    #     pelicula_obj = Movie(
    #         titulo=datos.get("original_title", "Título Desconocido"),
    #         genero=datos.get("genre_ids", "Sin Género"),
    #         sinopsis=datos.get("overview", "Sin sinopsis disponible."),
    #         image=datos.get("backdrop_path" or "poster_pat", "No Image URL")
    #     )
    #     lista_objetos_peliculas.append(pelicula_obj)
        
    # if lista_objetos_peliculas:
    #     print("\n--- Primer Objeto Movie Creado ---")
    #     print(lista_objetos_peliculas[0])
    #     print(lista_objetos_peliculas[1])
    #     print("----------------------------------\n")    #sala = SalaDeCine("Interstellar")
    # #sala.seleccionar_asientos()
    
if __name__ == "__main__":
    main()
