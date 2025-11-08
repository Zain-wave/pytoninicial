import requests
import json

API_KEY = "8a85a8773c3f69b24158b496338439c8" 
BASE_URL = "https://api.themoviedb.org/3/movie/popular"

# Parámetros de la solicitud
params = {
    'api_key': API_KEY,
    'language': 'es-ES' 
}

# ---------------------

def obtener_peliculas_populares(limite):
    
    lista_peliculas = []
    
    try:
        #solicitud a la api
        response = requests.get(BASE_URL, params)
        response.raise_for_status() 

        #paso el json a un diccionario
        data = response.json()

        # extraigo la lista de resultados
        movies = data.get('results', [])
        #mostrar la cantidad de peliculas que le solicite
        for i, movie in enumerate(movies[:limite]):
            lista_peliculas.append(movie)
            
        return lista_peliculas
            
            
    except requests.exceptions.RequestException as err:
        print(f"❌ Ocurrió un error al realizar la solicitud: {err}")
