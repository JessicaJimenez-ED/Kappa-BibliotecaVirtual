# src/models/usuario.py
"""
Modelo: Usuario
Representación de un usuario en la biblioteca virtual
"""

class Usuario:
    """Clase que representa un usuario del sistema"""
    
    def __init__(self, id_usuario: str, nombre: str, email: str):
        """
        Constructor del usuario.
        
        Argumentos:
            id_usuario: ID único del usuario
            nombre: Nombre completo del usuario
            email: Correo electrónico del usuario
        """
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.libros_prestados = []  # Lista de libros actualmente prestados
    
    def tomar_prestado(self, libro: 'Libro') -> bool:  
        """
        Toma prestado un libro.
        
        Argumentos:
            libro: Libro a tomar prestado
            
        Returns:
            True si se pudo tomar, False si no
        """
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False
    
    def devolver_libro(self, libro: 'Libro') -> bool:  
        """
        Devuelve un libro prestado.
        
        Argumentos:
            libro: Libro a devolver
            
        Returns:
            True si se devolvió correctamente, False si no lo tenía prestado
        """
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            return True
        return False
    
    def __str__(self) -> str:
        return f"{self.id_usuario} - {self.nombre} ({self.email})"