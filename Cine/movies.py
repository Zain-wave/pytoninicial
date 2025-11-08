class Movie:
    def __init__(self, titulo: str, genero: str, sinopsis: str, image: str):
        # Inicializo los datos básicos de la pelicula
        self.titulo = titulo
        self.genero = genero
        self.sinopsis = sinopsis
        self.image = image


    def __str__(self) -> str:
        return (
            f"🎬 Título: {self.titulo}\n"
            f"🎭 Género: {self.genero}\n"
            f"📝 Sinopsis: {self.sinopsis[:100]}... [Ver más]\n"
            f"🖼️ Imagen: {self.image}"
        )
        
    def to_dict(self) -> dict:
        return {
            "titulo": self.titulo,
            "genero": self.genero,
            "sinopsis": self.sinopsis,
            "image": self.image
        }