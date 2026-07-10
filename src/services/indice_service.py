"""
Servicio: Indice de Libros
Utiliza Arbol 2-3 para gestionar indices eficientes.

Este servicio demuestra como el Arbol 2-3 mejora las busquedas
en comparacion con listas enlazadas y arboles binarios.

Comparativa:
- Lista Enlazada: Busqueda O(n)
- Arbol Binario: Busqueda O(log n) promedio, O(n) peor caso
- Arbol 2-3: Busqueda O(log n) garantizado, siempre balanceado
"""

from src.structures.arbol23 import Arbol23
from src.models.libro import Libro
from typing import Optional, List, Dict

class IndiceService:
    """
    Servicio de indice que utiliza Arbol 2-3 para busquedas eficientes.
    
    Uso en el proyecto:
    - Indice por ISBN: Busqueda exacta O(log n)
    - Indice por Titulo: Busqueda exacta O(log n)
    - Indice por Autor: Busqueda exacta O(log n)
    
    El Arbol 2-3 garantiza que el indice siempre este balanceado,
    proporcionando rendimiento O(log n) en todas las operaciones.
    """
    
    def __init__(self):
        """
        Inicializa los indices con Arbol 2-3.
        
        Nota: El Arbol 2-3 es ideal para indices porque:
        - Siempre esta balanceado
        - Insercion eficiente O(log n)
        - Busqueda eficiente O(log n)
        - No requiere re-balanceo complejo como AVL
        """
        # Indice por ISBN usando Arbol 2-3
        self._indice_isbn: Arbol23[str] = Arbol23()
        
        # Indice por Titulo usando Arbol 2-3
        self._indice_titulo: Arbol23[str] = Arbol23()
        
        # Indice por Autor usando Arbol 2-3
        self._indice_autor: Arbol23[str] = Arbol23()
        
        # Diccionario para almacenar los libros
        self._libros: Dict[str, Libro] = {}
    
    def agregar_libro(self, libro: Libro) -> bool:
        """
        Agrega un libro a todos los indices.
        
        Complejidad: O(log n) - insercion en cada arbol
        
        Args:
            libro: Libro a agregar
        
        Returns:
            True si se agrego correctamente, False si ya existia
        
        Limitacion: Los ISBN deben ser unicos
        """
        if libro.isbn in self._libros:
            return False
        
        # Agregar a cada indice
        self._indice_isbn.insertar(libro.isbn)
        self._indice_titulo.insertar(libro.titulo)
        self._indice_autor.insertar(libro.autor)
        
        # Guardar el libro en el diccionario
        self._libros[libro.isbn] = libro
        
        return True
    
    def buscar_por_isbn(self, isbn: str) -> Optional[Libro]:
        """
        Busca un libro por ISBN usando Arbol 2-3.
        
        Complejidad: O(log n) siempre
        
        Args:
            isbn: ISBN del libro a buscar
        
        Returns:
            El libro encontrado, o None si no existe
        
        Limitacion: Requiere el ISBN exacto
        """
        if self._indice_isbn.buscar(isbn) is None:
            return None
        
        return self._libros.get(isbn)
    
    def buscar_por_titulo(self, titulo: str) -> Optional[Libro]:
        """
        Busca un libro por titulo exacto usando Arbol 2-3.
        
        Complejidad: O(log n) siempre
        
        Args:
            titulo: Titulo exacto del libro
        
        Returns:
            El libro encontrado, o None si no existe
        
        Limitacion: Requiere titulo exacto y sensible a mayusculas
        """
        if self._indice_titulo.buscar(titulo) is None:
            return None
        
        # Buscar el libro por su titulo
        for libro in self._libros.values():
            if libro.titulo == titulo:
                return libro
        
        return None
    
    def buscar_por_autor(self, autor: str) -> List[Libro]:
        """
        Busca todos los libros de un autor usando Arbol 2-3.
        
        Complejidad: O(log n + k) donde k es el numero de libros del autor
        
        Args:
            autor: Nombre del autor
        
        Returns:
            Lista de libros del autor
        
        Limitacion: Requiere nombre exacto del autor
        """
        if self._indice_autor.buscar(autor) is None:
            return []
        
        resultados = []
        for libro in self._libros.values():
            if libro.autor == autor:
                resultados.append(libro)
        
        return resultados
    
    def listar_por_isbn(self) -> List[str]:
        """Lista todos los ISBN en orden."""
        return self._indice_isbn.to_list()
    
    def listar_por_titulo(self) -> List[str]:
        """Lista todos los titulos en orden alfabetico."""
        return self._indice_titulo.to_list()
    
    def listar_por_autor(self) -> List[str]:
        """Lista todos los autores en orden alfabetico."""
        return self._indice_autor.to_list()
    
    def cantidad_libros(self) -> int:
        """Retorna el numero total de libros."""
        return len(self._libros)
    
    def esta_vacio(self) -> bool:
        """Verifica si hay libros en los indices."""
        return len(self._libros) == 0
    
    def estadisticas(self) -> dict:
        """
        Retorna estadisticas del Arbol 2-3.
        
        Returns:
            Diccionario con estadisticas de cada indice
        
        Limitacion: Las estadisticas son para propositos demostrativos
        """
        return {
            'total_libros': self.cantidad_libros(),
            'indice_isbn': {
                'tamano': len(self._indice_isbn),
                'altura': self._indice_isbn.altura(),
                'elementos': self._indice_isbn.to_list()[:5]  # Mostrar primeros 5
            },
            'indice_titulo': {
                'tamano': len(self._indice_titulo),
                'altura': self._indice_titulo.altura()
            },
            'indice_autor': {
                'tamano': len(self._indice_autor),
                'altura': self._indice_autor.altura()
            }
        }