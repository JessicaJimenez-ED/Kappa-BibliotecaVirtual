"""
Módulo: Lista Doblemente Enlazada
Implementación desde cero para el proyecto de biblioteca virtual.
Sprint 3 - Estructuras de datos: Listas Enlazadas

Características:
- Inserción al inicio, al final y en posición específica
- Eliminación por índice o por valor
- Búsqueda secuencial
- Recorrido hacia adelante y hacia atrás
- Tamaño dinámico

Complejidades:
- Insertar al inicio: O(1)
- Insertar al final: O(1)
- Insertar en posicion: O(n)
- Eliminar al inicio: O(1)
- Eliminar al final: O(1)
- Eliminar en posicion: O(n)
- Buscar: O(n) - busqueda secuencial
- Recorrer: O(n)

Limitaciones:
- No soporta búsqueda binaria porque no es un arreglo ordenado
"""

from typing import Any, Optional, TypeVar, Generic, Iterator
from __future__ import annotations

T = TypeVar('T')  # Tipo genérico para la lista


class Nodo(Generic[T]):
    """
    Nodo de la lista doblemente enlazada.
    Contiene el dato, referencia al siguiente nodo y al anterior.
    """
    
    def __init__(self, dato: T):
        """
        Inicializa un nodo con el dato proporcionado.
        
        Argumentos:
            dato: El dato a almacenar en el nodo
        
        Limitación: No puede almacenar None como dato válido (None se usa como centinela)
        """
        self.dato: T = dato
        self.siguiente: Optional[Nodo[T]] = None
        self.anterior: Optional[Nodo[T]] = None
    
    def __str__(self) -> str:
        """Representación en string del nodo"""
        return str(self.dato)


class ListaEnlazada(Generic[T]):
    """
    Lista Doblemente Enlazada genérica.
    Permite almacenar elementos de cualquier tipo y realizar operaciones básicas.
    
    USO EN EL PROYECTO:
    - Catálogo de libros: almacenar y gestionar todos los libros
    - Lista de usuarios registrados
    - Préstamos activos de un usuario
    """
    
    def __init__(self):
        """
        Constructor: Inicializa una lista vacía.
        """
        self._cabeza: Optional[Nodo[T]] = None  # Primer nodo
        self._cola: Optional[Nodo[T]] = None    # Último nodo
        self._tamano: int = 0                   # Cantidad de elementos
    
    # Métodos de inserción de elementos
    
    def insertar_inicio(self, dato: T) -> None:
        """
        Inserta un nuevo elemento al inicio de la lista.
        
        Complejidad: O(1)
        
        Argumentos:
            dato: Elemento a insertar
        
        Limitación: No permite insertar None como dato
        """
        if dato is None:
            raise ValueError("No se puede insertar None en la lista")
        
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self._cabeza = nuevo_nodo
            self._cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self._cabeza
            self._cabeza.anterior = nuevo_nodo
            self._cabeza = nuevo_nodo
        
        self._tamano += 1
    
    def insertar_final(self, dato: T) -> None:
        """
        Inserta un nuevo elemento al final de la lista.
        
        Complejidad: O(1) porque mantenemos referencia a la cola
        
        Argumentos:
            dato: Elemento a insertar
        
        Limitación: No permite insertar None como dato
        """
        if dato is None:
            raise ValueError("No se puede insertar None en la lista")
        
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self._cabeza = nuevo_nodo
            self._cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self._cola
            self._cola.siguiente = nuevo_nodo
            self._cola = nuevo_nodo
        
        self._tamano += 1
    
    def insertar_en_posicion(self, posicion: int, dato: T) -> bool:
        """
        Inserta un elemento en una posición específica (0 = inicio).
        
        Complejidad: O(n) - n = posición donde insertar
        
        Argumentos:
            posicion: Índice donde insertar (0 ≤ posicion ≤ tamaño)
            dato: Elemento a insertar
        
        Returns:
            True si se insertó correctamente, False si la posición es inválida
        
        Limitación: No permite insertar None como dato
        """
        if dato is None:
            raise ValueError("No se puede insertar None en la lista")
        
        if posicion < 0 or posicion > self._tamano:
            return False
        
        if posicion == 0:
            self.insertar_inicio(dato)
            return True
        
        if posicion == self._tamano:
            self.insertar_final(dato)
            return True
        
        # Insertar en medio
        nuevo_nodo = Nodo(dato)
        actual = self._cabeza
        
        # Avanzar hasta la posición deseada
        for _ in range(posicion):
            actual = actual.siguiente
        
        # Enlazar el nuevo nodo
        nuevo_nodo.anterior = actual.anterior
        nuevo_nodo.siguiente = actual
        actual.anterior.siguiente = nuevo_nodo
        actual.anterior = nuevo_nodo
        
        self._tamano += 1
        return True
    
    # Métodos de eliminación de elementos
    
    def eliminar_inicio(self) -> Optional[T]:
        """
        Elimina y retorna el primer elemento de la lista.
        
        Complejidad: O(1)
        
        Returns:
            El dato eliminado, o None si la lista está vacía
        
        Limitación: Si la lista queda vacía, cabeza y cola son None
        """
        if self.esta_vacia():
            return None
        
        dato = self._cabeza.dato
        
        if self._tamano == 1:
            self._cabeza = None
            self._cola = None
        else:
            self._cabeza = self._cabeza.siguiente
            self._cabeza.anterior = None
        
        self._tamano -= 1
        return dato
    
    def eliminar_final(self) -> Optional[T]:
        """
        Elimina y retorna el último elemento de la lista.
        
        Complejidad: O(1)
        
        Returns:
            El dato eliminado, o None si la lista está vacía
        
        Limitación: Si la lista queda vacía, cabeza y cola son None
        """
        if self.esta_vacia():
            return None
        
        dato = self._cola.dato
        
        if self._tamano == 1:
            self._cabeza = None
            self._cola = None
        else:
            self._cola = self._cola.anterior
            self._cola.siguiente = None
        
        self._tamano -= 1
        return dato
    
    def eliminar_en_posicion(self, posicion: int) -> Optional[T]:
        """
        Elimina y retorna el elemento en una posición específica.
        
        Complejidad: O(n) - n = posición a eliminar
        
        Argumentos:
            posicion: Índice del elemento a eliminar (0 ≤ posicion < tamaño)
        
        Returns:
            El dato eliminado, o None si la posición es inválida
        
        Limitación: No soporta eliminación por valor directamente
        """
        if posicion < 0 or posicion >= self._tamano:
            return None
        
        if posicion == 0:
            return self.eliminar_inicio()
        
        if posicion == self._tamano - 1:
            return self.eliminar_final()
        
        # Eliminar en medio
        actual = self._cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        
        dato = actual.dato
        actual.anterior.siguiente = actual.siguiente
        actual.siguiente.anterior = actual.anterior
        
        self._tamano -= 1
        return dato
    
    def eliminar_por_valor(self, dato: T) -> bool:
        """
        Elimina la primera ocurrencia de un valor en la lista.
        
        Complejidad: O(n) - n = tamaño de la lista
        
        Argumentos:
            dato: Valor a eliminar
        
        Returns:
            True si se eliminó, False si el valor no existe
        
        Limitación: Solo elimina la primera ocurrencia, no todas
        """
        if self.esta_vacia():
            return False
        
        actual = self._cabeza
        posicion = 0
        
        while actual is not None:
            if actual.dato == dato:
                self.eliminar_en_posicion(posicion)
                return True
            actual = actual.siguiente
            posicion += 1
        
        return False
    
    # Métodos de búsqueda y acceso a elementos
    
    def buscar(self, dato: T) -> int:
        """
        Busca la primera ocurrencia de un valor en la lista.
        
        Complejidad: O(n) - n = tamaño de la lista
        
        NO SOPORTA BÚSQUEDA BINARIA: La búsqueda es secuencial porque los
        datos no están ordenados ni tienen acceso aleatorio por índice.
        
        Argumentos:
            dato: Valor a buscar
        
        Returns:
            Índice de la primera ocurrencia, o -1 si no existe
        
        Limitación: Solo encuentra la primera ocurrencia
        """
        if self.esta_vacia():
            return -1
        
        actual = self._cabeza
        posicion = 0
        
        while actual is not None:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        
        return -1
    
    def buscar_todos(self, dato: T) -> list[int]:
        """
        Busca todas las ocurrencias de un valor en la lista.
        
        Complejidad: O(n) - n = tamaño de la lista
        
        Argumentos:
            dato: Valor a buscar
        
        Returns:
            Lista con todos los índices donde aparece el valor
        
        Limitación: La búsqueda es secuencial O(n)
        """
        indices = []
        if self.esta_vacia():
            return indices
        
        actual = self._cabeza
        posicion = 0
        
        while actual is not None:
            if actual.dato == dato:
                indices.append(posicion)
            actual = actual.siguiente
            posicion += 1
        
        return indices
    
    def obtener(self, posicion: int) -> Optional[T]:
        """
        Obtiene el elemento en una posición específica sin eliminarlo.
        
        Complejidad: O(n) - n = posición a obtener
        
        Argumentos:
            posicion: Índice del elemento (0 ≤ posicion < tamaño)
        
        Returns:
            El dato en la posición, o None si es inválida
        
        Limitación: No soporta acceso aleatorio O(1)
        """
        if posicion < 0 or posicion >= self._tamano:
            return None
        
        if posicion == 0:
            return self._cabeza.dato
        
        if posicion == self._tamano - 1:
            return self._cola.dato
        
        actual = self._cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        
        return actual.dato
    
    # Métodos de recorrido de la lista
    
    def recorrer_adelante(self) -> Iterator[T]:
        """
        Generador para recorrer la lista hacia adelante (inicio → final).
        
        Complejidad: O(n) - n = tamaño de la lista
        
        Yields:
            Cada elemento en orden de la lista
        
        Limitación: No modifica la lista durante el recorrido
        """
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
    
    def recorrer_atras(self) -> Iterator[T]:
        """
        Generador para recorrer la lista hacia atrás (final → inicio).
        
        Complejidad: O(n) - n = tamaño de la lista
        
        Yields:
            Cada elemento en orden inverso
        
        Limitación: No modifica la lista durante el recorrido
        """
        actual = self._cola
        while actual is not None:
            yield actual.dato
            actual = actual.anterior
    
    # Métodos de consulta de estado de la lista y otras utilidades
    
    def esta_vacia(self) -> bool:
        """Verifica si la lista está vacía. Complejidad: O(1)"""
        return self._tamano == 0
    
    def tamano(self) -> int:
        """Retorna el número de elementos en la lista. Complejidad: O(1)"""
        return self._tamano
    
    def __len__(self) -> int:
        """Permite usar len(lista)"""
        return self._tamano
    
    def __contains__(self, dato: T) -> bool:
        """Permite usar 'dato in lista'"""
        return self.buscar(dato) != -1
    
    def to_list(self) -> list[T]:
        """
        Convierte la lista enlazada a una lista de Python.
        
        Complejidad: O(n) - n = tamaño de la lista
        
        Returns:
            Lista de Python con todos los elementos
        """
        return list(self.recorrer_adelante())
    
    def __str__(self) -> str:
        """Representación en string de la lista"""
        if self.esta_vacia():
            return "ListaEnlazada: []"
        
        elementos = []
        for dato in self.recorrer_adelante():
            elementos.append(str(dato))
        
        return f"ListaEnlazada: [{', '.join(elementos)}]"
    
    def __repr__(self) -> str:
        """Representación detallada para debugging"""
        return self.__str__()