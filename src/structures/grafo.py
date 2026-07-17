"""
Módulo: Grafo
Sprint 6 - Estructuras de datos: Grafos

Características:
- Representación con listas de adyacencia (eficiente para grafos dispersos)
- Recorridos: BFS (Breadth First Search) y DFS (Depth First Search)
- Detección de caminos entre nodos

Complejidades:
- Agregar vértice: O(1)
- Agregar arista: O(1)
- BFS: O(V + E) donde V = vertices, E = aristas
- DFS: O(V + E)

Limitaciones:
- No soporta grafos con aristas ponderadas (solo no ponderados)
- No detecta ciclos automaticamente
- No es dirigido (las conexiones son bidireccionales)
- No implementa eliminacion de vertices/aristas
"""

from typing import Dict, List, Set, Optional, Any, Iterator
from collections import deque


class Grafo:
    """
    Grafo no dirigido para recomendaciones de libros.
    
    Uso en el proyecto:
    - Recomendar libros similares (comparten autor, genero, etc.)
    - Encontrar caminos de lectura (si leiste X, te gustara Y)
    - Agrupar libros por temas o autores
    
    Representacion: Lista de adyacencia (diccionario de conjuntos)
    - Cada libro (ISBN) es un vertice
    - Las aristas conectan libros relacionados
    """
    
    def __init__(self):
        """Inicializa un grafo vacio."""
        self._adyacencia: Dict[str, Set[str]] = {}
        self._vertices: int = 0
        self._aristas: int = 0
    
    # MÉTODOS DE CONSTRUCCIÓN
    
    def agregar_vertice(self, vertice: str) -> bool:
        """
        Agrega un vértice al grafo.
        
        Complejidad: O(1)
        
        Argumentos:
            vertice: Identificador del vértice (ej: ISBN de un libro)
        
        Returns:
            True si se agregó correctamente, False si ya existia
        
        Limitación: No se pueden agregar vértices con el mismo identificador
        """
        if vertice in self._adyacencia:
            return False
        
        self._adyacencia[vertice] = set()
        self._vertices += 1
        return True
    
    def agregar_arista(self, vertice1: str, vertice2: str) -> bool:
        """
        Agrega una arista entre dos vertices.
        
        Complejidad: O(1)
        
        Argumentos:
            vertice1: Primer vertice
            vertice2: Segundo vertice
        
        Returns:
            True si se agregó correctamente, False si ya existia
        
        Limitación: Grafo no dirigido (conexión bidireccional)
        """
        if vertice1 not in self._adyacencia or vertice2 not in self._adyacencia:
            return False
        
        if vertice2 in self._adyacencia[vertice1]:
            return False
        
        # Agregar en ambas direcciones (grafo no dirigido)
        self._adyacencia[vertice1].add(vertice2)
        self._adyacencia[vertice2].add(vertice1)
        self._aristas += 1
        return True
    
    # MÉTODOS DE RECORRIDO
    
    def bfs(self, inicio: str) -> List[str]:
        """
        Recorrido BFS (Breadth First Search) desde un vertice.
        
        Complejidad: O(V + E)
        
        Argumentos:
            inicio: Vertice de inicio
        
        Returns:
            Lista de vertices en orden de recorrido
        
        Limitación: No soporta búsqueda por peso de aristas
        """
        if inicio not in self._adyacencia:
            return []
        
        visitados: Set[str] = set()
        cola = deque([inicio])
        recorrido: List[str] = []
        
        visitados.add(inicio)
        
        while cola:
            vertice = cola.popleft()
            recorrido.append(vertice)
            
            for vecino in sorted(self._adyacencia[vertice]):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        
        return recorrido
    
    def dfs(self, inicio: str) -> List[str]:
        """
        Recorrido DFS (Depth First Search) desde un vertice.
        
        Complejidad: O(V + E)
        
        Argumentos:
            inicio: Vertice de inicio
        
        Returns:
            Lista de vertices en orden de recorrido
        
        Limitación: No soporta búsqueda por peso de aristas
        """
        if inicio not in self._adyacencia:
            return []
        
        visitados: Set[str] = set()
        recorrido: List[str] = []
        
        self._dfs_recursivo(inicio, visitados, recorrido)
        return recorrido
    
    def _dfs_recursivo(self, vertice: str, visitados: Set[str], recorrido: List[str]) -> None:
        """
        Metodo recursivo para DFS.
        
        Argumentos:
            vertice: Vertice actual
            visitados: Conjunto de vertices visitados
            recorrido: Lista de vertices en orden de recorrido
        
        Limitación: Recursión puede causar stack overflow en grafos muy grandes
        """
        visitados.add(vertice)
        recorrido.append(vertice)
        
        for vecino in sorted(self._adyacencia[vertice]):
            if vecino not in visitados:
                self._dfs_recursivo(vecino, visitados, recorrido)
    
    # MÉTODOS DE BUSQUEDA
    
    def encontrar_camino(self, inicio: str, destino: str) -> Optional[List[str]]:
        """
        Encuentra un camino entre dos vertices usando BFS.
        
        Complejidad: O(V + E)
        
        Argumentos:
            inicio: Vertice de inicio
            destino: Vertice de destino
        
        Returns:
            Lista de vertices que forman el camino, o None si no existe
        
        Limitación: Encuentra el camino más corto en número de aristas
        """
        if inicio not in self._adyacencia or destino not in self._adyacencia:
            return None
        
        if inicio == destino:
            return [inicio]
        
        visitados: Set[str] = {inicio}
        cola = deque([(inicio, [inicio])])
        
        while cola:
            vertice, camino = cola.popleft()
            
            for vecino in self._adyacencia[vertice]:
                if vecino not in visitados:
                    nuevo_camino = camino + [vecino]
                    if vecino == destino:
                        return nuevo_camino
                    visitados.add(vecino)
                    cola.append((vecino, nuevo_camino))
        
        return None
    
    def obtener_vecinos(self, vertice: str) -> List[str]:
        """
        Obtiene los vecinos de un vertice.
        
        Complejidad: O(1)
        
        Argumentos:
            vertice: Vertice a consultar
        
        Returns:
            Lista de vecinos del vertice
        """
        if vertice not in self._adyacencia:
            return []
        return sorted(list(self._adyacencia[vertice]))
    
    # MÉTODOS DE CONSULTA
    
    def numero_vertices(self) -> int:
        """Retorna el numero de vertices."""
        return self._vertices
    
    def numero_aristas(self) -> int:
        """Retorna el numero de aristas."""
        return self._aristas
    
    def esta_conectado(self, vertice1: str, vertice2: str) -> bool:
        """
        Verifica si dos vertices estan conectados.
        
        Complejidad: O(1)
        """
        if vertice1 not in self._adyacencia:
            return False
        return vertice2 in self._adyacencia[vertice1]
    
    def obtener_vertices(self) -> List[str]:
        """Retorna todos los vertices del grafo."""
        return sorted(list(self._adyacencia.keys()))
    
    # MÉTODOS DE REPRESENTACIÓN
    
    def __str__(self) -> str:
        """Representación en string del grafo."""
        if self._vertices == 0:
            return "Grafo: vacío"
        
        lineas = []
        for vertice in sorted(self._adyacencia.keys()):
            vecinos = sorted(self._adyacencia[vertice])
            if vecinos:
                lineas.append(f"{vertice} -> {', '.join(vecinos)}")
            else:
                lineas.append(f"{vertice} -> (sin conexiones)")
        
        return f"Grafo (V={self._vertices}, E={self._aristas}):\n" + "\n".join(lineas)