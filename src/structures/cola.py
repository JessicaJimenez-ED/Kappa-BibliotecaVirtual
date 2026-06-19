"""
Módulo: Cola (Queue)
Implementación desde cero de una cola genérica para el proyecto de biblioteca virtual.
Sprint 2 - Estructuras de datos: Pilas y Colas
"""

from typing import Any, List, Optional

class Cola:
    """
    Clase que implementa una Cola (FIFO - First In, First Out) desde cero.
    
    Esta estructura se utilizará en el proyecto para:
    - Gestión de reservas de libros
    - Sistema de préstamos en orden de llegada
    - Atención de solicitudes de usuarios
    
    Complejidad temporal:
    - enqueue: O(1)
    - dequeue: O(1)
    - front: O(1)
    - is_empty: O(1)
    """
    
    def __init__(self):
        """
        Constructor: Inicializa una cola vacía.
        """
        self.items: List[Any] = [] # Lista para almacenar los elementos de la cola
        self._size: int = 0 # Variable para mantener el tamaño de la cola, contador de elemntos
    
    def enqueue(self, elemento: Any) -> None:
        """
        Agrega un elemento al final de la cola.
        
        Argumentos: 
        - elemento: El elemento a agregar a la cola.
        
        Complejidad: O(1) - Inserción al final de la lista
        """
        self.items.append(elemento)
        self._size += 1

    def dequeue(self) -> Any:
        """
        Elimina y retorna el elemento del frente de la cola.
        
        Returns:
            El elemento eliminado del frente de la cola
            
        Raises:
            IndexError: Excepción lanzada si la cola está vacía
            
        Complejidad: O(1) - Eliminación del primer elemento
        """
        if self.is_empty():
            raise IndexError("La cola está vacía")
        self._size -= 1
        return self.items.pop(0)

    def front(self) -> Any:
        """
        Retorna el elemento del frente sin eliminarlo.
        
        Returns:
            El elemento en el frente de la cola
            
        Raises:
            IndexError: Excepción lanzada si la cola está vacía
            
        Complejidad: O(1) - Acceso directo al primer elemento
        """
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.items[0]

    def is_empty(self) -> bool:
        """
        Verifica si la cola está vacía.
        
        Returns:
            True si la cola está vacía, False en caso contrario
            
        Complejidad: O(1) - Verificación de longitud de la lista
        """
        return self._size == 0

    def size(self) -> int:
        """
        Retorna el número de elementos en la cola.
        
        Returns:
            Cantidad de elementos en la cola
            
        Complejidad: O(1) - Retorno de un contador de tamaño
        """
        return self._size

    def clear(self) -> None:
        """
        Vacía completamente la cola.
        
        Complejidad: O(1) - Reinicia la lista
        """
        self._items.clear()
        self._size = 0

    def to_list(self) -> List[Any]:
        """
        Convierte la cola a una lista para visualización.
        
        Returns:
            Lista con los elementos de la cola (desde el frente hasta el final)
            
        Complejidad: O(n) - n = tamaño de la cola
        """
        return self._items.copy()

    def __str__(self) -> str:
        """
        Representación en string de la cola.
        
        Returns:
            String con los elementos de la cola
        """
        return f"Cola: {self._items}"
    
    def __len__(self) -> int:
        """
        Retorna el número de elementos en la cola al usar len().
        
        Returns:
            Cantidad de elementos en la cola
            
        Complejidad: O(1) - Retorno de un contador de tamaño
        """
        return self._size