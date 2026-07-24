"""
Servicio: Recomendaciones de Libros
Utiliza un Grafo para recomendar libros similares.

Uso en el proyecto:
- Recomendar libros que comparten autor
- Recomendar libros que comparten genero/tema
- Encontrar caminos de lectura
"""

from structures.grafo import Grafo
from models.libro import Libro
from typing import List, Optional, Dict, Set

class RecomendacionService:
    """
    Servicio de recomendaciones basado en un grafo de relaciones entre libros.
    
    Las relaciones pueden ser:
    - Mismo autor
    - Mismo genero
    - Libros similares (definido por el usuario)
    - Libros que suelen leerse juntos
    """
    
    def __init__(self):
        """Inicializa el grafo de recomendaciones."""
        self._grafo = Grafo()
        self._libros: Dict[str, Libro] = {}
    
    def agregar_libro(self, libro: Libro) -> bool:
        """
        Agrega un libro al sistema de recomendaciones.
        
        Complejidad: O(1)
        
        Args:
            libro: Libro a agregar
        
        Returns:
            True si se agrego correctamente
        """
        if libro.isbn in self._libros:
            return False
        
        self._libros[libro.isbn] = libro
        self._grafo.agregar_vertice(libro.isbn)
        return True
    
    def conectar_por_autor(self, autor: str) -> None:
        """
        Conecta todos los libros del mismo autor.
        
        Complejidad: O(n²) - n = numero de libros del autor
        """
        isbns = [isbn for isbn, libro in self._libros.items() if libro.autor == autor]
        
        for i in range(len(isbns)):
            for j in range(i + 1, len(isbns)):
                self._grafo.agregar_arista(isbns[i], isbns[j])
    
    def conectar_libros(self, isbn1: str, isbn2: str) -> bool:
        """
        Conecta dos libros especificos.
        
        Args:
            isbn1: ISBN del primer libro
            isbn2: ISBN del segundo libro
        
        Returns:
            True si se conectaron correctamente
        """
        if isbn1 not in self._libros or isbn2 not in self._libros:
            return False
        
        return self._grafo.agregar_arista(isbn1, isbn2)
    
    def recomendar_por_autor(self, isbn: str) -> List[Libro]:
        """
        Recomienda libros del mismo autor.
        
        Complejidad: O(1)
        """
        if isbn not in self._libros:
            return []
        
        autor = self._libros[isbn].autor
        return [libro for libro in self._libros.values() 
                if libro.autor == autor and libro.isbn != isbn]
    
    def recomendar_bfs(self, isbn: str, profundidad: int = 2) -> List[Libro]:
        """
        Recomienda libros mediante BFS.
        
        Args:
            isbn: ISBN del libro de referencia
            profundidad: Niveles de profundidad a explorar
        
        Returns:
            Lista de libros recomendados
        """
        if isbn not in self._libros:
            return []
        
        # Obtener todos los libros alcanzables por BFS
        visitados = set()
        cola = [(isbn, 0)]
        visitados.add(isbn)
        recomendados = []
        
        while cola:
            actual, nivel = cola.pop(0)
            
            if nivel >= profundidad:
                continue
            
            for vecino in self._grafo.obtener_vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    if vecino in self._libros:
                        recomendados.append(self._libros[vecino])
                    cola.append((vecino, nivel + 1))
        
        return recomendados
    
    def encontrar_camino_lectura(self, isbn1: str, isbn2: str) -> List[Libro]:
        """
        Encuentra un camino de lectura entre dos libros.
        
        Args:
            isbn1: ISBN del libro de inicio
            isbn2: ISBN del libro de destino
        
        Returns:
            Lista de libros que forman el camino
        """
        if isbn1 not in self._libros or isbn2 not in self._libros:
            return []
        
        camino = self._grafo.encontrar_camino(isbn1, isbn2)
        if camino is None:
            return []
        
        return [self._libros[isbn] for isbn in camino if isbn in self._libros]
    
    def estadisticas(self) -> dict:
        """Retorna estadisticas del grafo de recomendaciones."""
        return {
            'total_libros': len(self._libros),
            'vertices': self._grafo.numero_vertices(),
            'aristas': self._grafo.numero_aristas(),
            'vertices_conectados': sum(1 for v in self._grafo.obtener_vertices() 
                                      if self._grafo.obtener_vecinos(v))
        }
    
    def __str__(self) -> str:
        return str(self._grafo)