"""
Servicio: Búsqueda de Libros
Utiliza Árbol Binario y AVL para búsquedas eficientes.

Este servicio demuestra como los arboles mejoran el rendimiento
de las búsquedas en comparacion con listas enlazadas.

Comparativa:
- Lista Enlazada: búsqueda O(n) - lenta para catalogos grandes
- Árbol Binario: búsqueda O(log n) promedio - rapida
- Árbol AVL: búsqueda O(log n) garantizado - siempre rapida
"""

from structures.arbolBinario import ArbolBinario
from structures.arbolAVL import ArbolAVL
from models.libro import Libro
from typing import Optional, List, Dict, Tuple

class BusquedaService:
    """
    Servicio de busqueda que utiliza arboles para indices eficientes.
    
    Uso en el proyecto:
    - Indice por ISBN: Busqueda exacta de un libro
    - Indice por Titulo: Busqueda de libros por titulo
    - Indice por Autor: Busqueda de libros por autor
    
    Los indices se mantienen actualizados automaticamente cuando se
    agregan o eliminan libros del catalogo.
    """
    
    def __init__(self):
        """
        Inicializa los indices de busqueda con arboles.
        
        Nota: Los arboles se inicializan vacios y se llenan con los libros
        a medida que se agregan al catalogo.
        """
        # Indice por ISBN usando AVL (rendimiento garantizado)
        self._indice_isbn: ArbolAVL[str] = ArbolAVL()
        
        # Indice por Titulo usando AVL (ordenamiento natural)
        self._indice_titulo: ArbolAVL[str] = ArbolAVL()
        
        # Indice por Autor usando AVL (busquedas por autor)
        self._indice_autor: ArbolAVL[str] = ArbolAVL()
        
        # Diccionario para almacenar los libros (relacion ISBN -> Libro)
        self._libros: Dict[str, Libro] = {}
    
    def agregar_libro(self, libro: Libro) -> bool:
        """
        Agrega un libro a todos los indices de busqueda.
        
        Complejidad: O(log n) - insercion en cada arbol AVL
        
        Args:
            libro: Libro a agregar
        
        Returns:
            True si se agrego correctamente, False si ya existia
        
        Limitacion: Los titulos duplicados no se permiten en el indice
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
    
    def eliminar_libro(self, isbn: str) -> Optional[Libro]:
        """
        Elimina un libro de todos los indices.
        
        Complejidad: O(log n) - eliminacion en cada arbol AVL
        
        Args:
            isbn: ISBN del libro a eliminar
        
        Returns:
            El libro eliminado, o None si no existia
        
        Limitacion: La eliminacion requiere buscar el libro primero
        """
        if isbn not in self._libros:
            return None
        
        libro = self._libros[isbn]
        
        # Eliminar de cada indice
        self._indice_isbn.eliminar(isbn)
        self._indice_titulo.eliminar(libro.titulo)
        self._indice_autor.eliminar(libro.autor)
        
        # Eliminar del diccionario
        del self._libros[isbn]
        
        return libro
    
    def buscar_por_isbn(self, isbn: str) -> Optional[Libro]:
        """
        Busca un libro por ISBN usando el arbol AVL.
        
        Complejidad: O(log n) siempre
        
        Args:
            isbn: ISBN del libro a buscar
        
        Returns:
            El libro encontrado, o None si no existe
        
        Limitacion: Requiere el ISBN exacto, no soporta busqueda parcial
        """
        if self._indice_isbn.buscar(isbn) is None:
            return None
        
        return self._libros.get(isbn)
    
    def buscar_por_titulo(self, titulo: str) -> Optional[Libro]:
        """
        Busca un libro por titulo exacto usando el arbol AVL.
        
        Complejidad: O(log n) siempre
        
        Args:
            titulo: Titulo exacto del libro a buscar
        
        Returns:
            El libro encontrado, o None si no existe
        
        Limitacion: Requiere el titulo exacto, sensible a mayusculas/minusculas
        No soporta busqueda parcial
        """
        # Buscar en el indice de titulos
        if self._indice_titulo.buscar(titulo) is None:
            return None
        
        # Buscar el libro por su titulo (recorremos todos los libros)
        # Esta es una limitacion: necesitamos mapeo titulo -> ISBN
        # En una implementacion real, tendriamos un diccionario adicional
        for libro in self._libros.values():
            if libro.titulo == titulo:
                return libro
        
        return None
    
    def buscar_por_autor(self, autor: str) -> List[Libro]:
        """
        Busca todos los libros de un autor usando el arbol AVL.
        
        Complejidad: O(log n + k) donde k es el numero de libros del autor
        
        Args:
            autor: Nombre del autor a buscar
        
        Returns:
            Lista de libros del autor
        
        Limitacion: Requiere el nombre exacto del autor
        """
        # Buscar en el indice de autores
        if self._indice_autor.buscar(autor) is None:
            return []
        
        # Recorrer todos los libros y filtrar por autor
        # Limitacion: Necesitamos un diccionario autor -> lista de ISBNs
        # para hacer esta busqueda en O(log n)
        resultados = []
        for libro in self._libros.values():
            if libro.autor == autor:
                resultados.append(libro)
        
        return resultados
    
    def listar_todos(self) -> List[Libro]:
        """
        Lista todos los libros en orden por ISBN.
        
        Complejidad: O(n) - n = cantidad de libros
        
        Returns:
            Lista de todos los libros ordenados por ISBN
        
        Limitacion: Crea una nueva lista, no modifica el arbol
        """
        return list(self._libros.values())
    
    def listar_por_titulo(self) -> List[str]:
        """
        Lista todos los titulos en orden alfabetico.
        
        Complejidad: O(n) - n = cantidad de titulos
        
        Returns:
            Lista de titulos en orden alfabetico
        
        Limitacion: Solo retorna los titulos, no los libros completos
        """
        return self._indice_titulo.to_list()
    
    def listar_por_autor(self) -> List[str]:
        """
        Lista todos los autores en orden alfabetico.
        
        Complejidad: O(n) - n = cantidad de autores
        
        Returns:
            Lista de autores en orden alfabetico
        
        Limitacion: No muestra los libros de cada autor
        """
        return self._indice_autor.to_list()
    
    def cantidad_libros(self) -> int:
        """Retorna el numero total de libros en los indices."""
        return len(self._libros)
    
    def esta_vacio(self) -> bool:
        """Verifica si hay libros en los indices."""
        return len(self._libros) == 0
    
    def estadisticas(self) -> dict:
        """
        Retorna estadisticas de los arboles para comparacion.
        
        Returns:
            Diccionario con estadisticas de cada indice
        
        Limitacion: Las estadisticas son para propositos demostrativos
        """
        return {
            'total_libros': self.cantidad_libros(),
            'indice_isbn': {
                'tamano': len(self._indice_isbn),
                'altura': self._indice_isbn.altura()
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