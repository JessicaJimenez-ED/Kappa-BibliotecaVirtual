"""
Módulo: Pila (Stack)
Implementación desde cero de una pila genérica para el proyecto de biblioteca virtual.
Sprint 2 - Estructuras de datos: Pilas y Colas
"""

from typing import Any, List, Optional

class Pila:
    """
    Clase que implementa una Pila (LIFO - Último en entrar, primero en salir) desde cero.
    
    Esta estructura se utilizará en el proyecto para:
    - Historial de acciones de usuarios
    - Sistema de "deshacer" operaciones
    - Navegación entre páginas del sistema
    
    Complejidad temporal:
    - push: O(1)
    - pop: O(1)
    - peek: O(1)
    - is_empty: O(1)
    """
    def __init__(self):
        """
        Constructor: Inicializa una pila vacía.
        """
        self.items: List[Any] = []
        self._size: int = 0

    def push(self, elemento: Any) -> None:
        """
        Agrega un elemento a la cima de la pila.
        
        Argumentos: 
        - elemento: El elemento a agregar a la pila.
        
        Complejidad: O(1) - Inserción al final de la lista
        """
        self.items.append(elemento)
        self._size += 1

    def pop(self) -> Any:
        """
        Elimina y retorna el elemento de la cima de la pila.
        
        Returns:
            El elemento eliminado de la cima
            
        Raises:
            IndexError: Excepción lanzada si la pila está vacía
            
        Complejidad: O(1) - Eliminación del último elemento
        """
        if self.is_empty():
            raise IndexError("La pila está vacía")
        self._size -= 1
        return self.items.pop()

    def peek(self) -> Any:
        """
        Retorna el elemento de la cima sin eliminarlo.
        
        Returns:
            El elemento en la cima de la pila
            
        Raises:
            IndexError: Excepción lanzada si la pila está vacía
            
        Complejidad: O(1) - Acceso directo al último elemento
        """
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self.items[-1]

    def is_empty(self) -> bool:
        """
        Verifica si la pila está vacía.
        
        Returns:
            True si la pila está vacía, False en caso contrario
            
        Complejidad: O(1) - Verificación de longitud de la lista
        """
        return self._size == 0

    def size(self) -> int:
        """
        Retorna el número de elementos en la pila.
        
        Returns:
            Cantidad de elementos en la pila
            
        Complejidad: O(1) - Retorno de un contador de tamaño
        """
        return self._size
    
    def clear(self) -> None:
        """
        Vacía completamente la pila.
        
        Complejidad: O(1) - Reinicia la lista
        """
        self.items.clear()
        self._size = 0
    
    def to_list(self) -> List[Any]:
        """
        Convierte la pila a una lista para visualización.
        
        Returns:
            Lista con los elementos de la pila (desde la cima hasta el fondo)
            
        Complejidad: O(n) - n = tamaño de la pila
        """
        return self._items.copy()
    
    def __str__(self) -> str:
        """
        Representación en string de la pila.
        
        Returns:
            String con los elementos de la pila
        """
        return f"Pila: {self._items}"
    
    def __len__(self) -> int:
        """
        Permite usar len(pila) para obtener el tamaño.
        """
        return self._size