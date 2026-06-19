# src/models/libro.py
"""
Modelo: Libro
Representación de un libro en la biblioteca virtual
"""

class Libro:
    """Clase que representa un libro en el sistema"""
    
    def __init__(self, isbn: str, titulo: str, autor: str, anio: int):
        """
        Constructor del libro.
        
        Argumentos:
            isbn: Código ISBN único del libro
            titulo: Título del libro
            autor: Nombre del autor
            anio: Año de publicación
        """
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True
    
    def prestar(self) -> bool:
        """
        Marca el libro como prestado si está disponible.
        
        Returns:
            True si se pudo prestar, False si no estaba disponible
        """
        if self.disponible:
            self.disponible = False
            return True
        return False
    
    def devolver(self) -> None:
        """
        Marca el libro como disponible
        """
        self.disponible = True
    
    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.isbn} - {self.titulo} ({self.autor}) - {estado}"