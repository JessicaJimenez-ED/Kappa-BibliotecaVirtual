"""
Módulo: Arbol Binario de Búsqueda (ABB)
Sprint 4 - Estructuras de datos: Arboles Binarios
Implementación desde cero de un Arbol Binario de Búsqueda genérico en Python.

Caracteristicas:
- Insercion de nodos manteniendo la propiedad de ABB
- Búsqueda eficiente O(log n) en promedio
- Recorridos: inorden, preorden, postorden
- Eliminacion de nodos con sus tres casos

Complejidades:
- Insercion: O(log n) promedio, O(n) en el peor caso (arbol degenerado)
- Búsqueda: O(log n) promedio, O(n) en el peor caso
- Recorridos: O(n) siempre
- Eliminacion: O(log n) promedio, O(n) en el peor caso

Limitaciones:
- No se auto-balancea, puede degenerar en una lista enlazada
- Para datos ordenados, el rendimiento es pesimo O(n)
- Para búsquedas con datos desordenados, es muy eficiente
"""

from typing import Optional, TypeVar, Generic, Iterator, List # Se importan tipos genéricos y utilidades de tipado
from __future__ import annotations # Permite usar anotaciones de tipo de manera más flexible, especialmente para referencias a la propia clase

T = TypeVar('T') # Tipo genérico para los datos almacenados en el arbol

class NodoABB(Generic[T]):
    """
    Nodo del Arbol Binario de Búsqueda.
    Contiene el dato y referencias a los subarboles izquierdo y derecho.
    """
    
    def __init__(self, dato: T):
        """
        Inicializa un nodo con el dato proporcionado.
        
        Argumentos:
            dato: El dato a almacenar en el nodo
        
        Limitación: No puede almacenar None como dato valido
        """
        self.dato: T = dato
        self.izquierdo: Optional[NodoABB[T]] = None
        self.derecho: Optional[NodoABB[T]] = None
        self.altura: int = 1  # Util para AVL, pero lo dejamos para consistencia
    
    def __str__(self) -> str:
        return str(self.dato) # Representacion en string del nodo, mostrando solo el dato


class ArbolBinario(Generic[T]):
    """
    Árbol Binario de Búsqueda genérico.
    
    Uso en el proyecto:
    - Búsqueda rapida de libros por ISBN
    - Catálogo ordenado por título
    - Listado de libros en orden alfabético
    
    La propiedad de ABB: todos los elementos del subárbol izquierdo
    son menores que la raíz, y todos los del derecho son mayores.
    """
    
    def __init__(self):
        """Inicializa un árbol binario vacio."""
        self._raiz: Optional[NodoABB[T]] = None
        self._tamano: int = 0
    
    # MÉTODOS DE INSERCION
    
    def insertar(self, dato: T) -> bool:
        """
        Inserta un nuevo dato en el árbol manteniendo la propiedad de ABB.
        
        Complejidad: O(log n) promedio, O(n) en el peor caso
        
        Argumentos:
            dato: Dato a insertar
        
        Returns:
            True si se inserto correctamente, False si ya existia
        
        Limitación: No permite duplicados
        No se auto-balancea, puede degenerar
        """
        if dato is None:
            raise ValueError("No se puede insertar None en el árbol")
        
        if self.buscar(dato) is not None:
            return False  # No se permiten duplicados
        
        self._raiz = self._insertar_recursivo(self._raiz, dato)
        self._tamano += 1
        return True
    
    def _insertar_recursivo(self, nodo: Optional[NodoABB[T]], dato: T) -> NodoABB[T]:
        """
        Metodo recursivo para insertar un dato en el árbol.
        
        Argumentos:
            nodo: Nodo actual en la recursión
            dato: Dato a insertar
        
        Returns:
            El nodo actualizado con el nuevo dato
        
        Limitacion: Recursion puede causar stack overflow en arboles muy grandes
        """
        if nodo is None:
            return NodoABB(dato)
        
        if dato < nodo.dato:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, dato)
        # Si es igual, no hacemos nada (no se permite duplicados)
        
        return nodo
    
    # MÉTODOS DE BÚSQUEDA
    
    def buscar(self, dato: T) -> Optional[T]:
        """
        Busca un dato en el árbol.
        
        Complejidad: O(log n) promedio, O(n) en el peor caso
        
        Argumentos:
            dato: Dato a buscar
        
        Returns:
            El dato encontrado, o None si no existe
        
        Limitacion: No soporta Búsqueda por rango directamente
        """
        if self.esta_vacio():
            return None
        
        nodo = self._buscar_recursivo(self._raiz, dato)
        return nodo.dato if nodo else None
    
    def _buscar_recursivo(self, nodo: Optional[NodoABB[T]], dato: T) -> Optional[NodoABB[T]]:
        """
        Metodo recursivo para buscar un dato en el árbol.
        
        Argumentos:
            nodo: Nodo actual en la recursión
            dato: Dato a buscar
        
        Returns:
            El nodo encontrado, o None si no existe
        """
        if nodo is None:
            return None
        
        if dato == nodo.dato:
            return nodo
        elif dato < nodo.dato:
            return self._buscar_recursivo(nodo.izquierdo, dato)
        else:
            return self._buscar_recursivo(nodo.derecho, dato)
    
    def buscar_minimo(self) -> Optional[T]:
        """
        Encuentra el valor minimo en el arbol.
        
        Complejidad: O(log n) promedio, O(n) en el peor caso
        
        Returns:
            El valor minimo, o None si el arbol esta vacio
        
        Limitacion: Solo encuentra el minimo, no el maximo
        """
        if self.esta_vacio():
            return None
        
        nodo = self._raiz
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        
        return nodo.dato
    
    def buscar_maximo(self) -> Optional[T]:
        """
        Encuentra el valor maximo en el arbol.
        
        Complejidad: O(log n) promedio, O(n) en el peor caso
        
        Returns:
            El valor maximo, o None si el arbol esta vacio
        """
        if self.esta_vacio():
            return None
        
        nodo = self._raiz
        while nodo.derecho is not None:
            nodo = nodo.derecho
        
        return nodo.dato
    
    # MÉTODOS DE ELIMINACIÓN
    
    def eliminar(self, dato: T) -> bool:
        """
        Elimina un dato del árbol.
        
        Complejidad: O(log n) promedio, O(n) en el peor caso
        
        Argumentos:
            dato: Dato a eliminar
        
        Returns:
            True si se elimino correctamente, False si no existia
        
        Limitacion: La eliminacion considera tres casos:
        1. Nodo hoja (sin hijos): se elimina directamente
        2. Nodo con un hijo: se reemplaza por el hijo
        3. Nodo con dos hijos: se reemplaza por el minimo del subarbol derecho
        """
        if self.esta_vacio():
            return False
        
        if self.buscar(dato) is None:
            return False
        
        self._raiz = self._eliminar_recursivo(self._raiz, dato)
        self._tamano -= 1
        return True
    
    def _eliminar_recursivo(self, nodo: Optional[NodoABB[T]], dato: T) -> Optional[NodoABB[T]]:
        """
        Método recursivo para eliminar un dato del árbol.
        
        Argumentos:
            nodo: Nodo actual en la recursión
            dato: Dato a eliminar
        
        Returns:
            El nodo actualizado después de la eliminación
        
        Limitación: No se balancea después de la eliminación
        """
        if nodo is None:
            return None
        
        if dato < nodo.dato:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, dato)
        else:
            # Caso 1: Nodo hoja (sin hijos)
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            
            # Caso 2: Nodo con un hijo
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            
            # Caso 3: Nodo con dos hijos
            # Encontrar el minimo del subarbol derecho
            sucesor = self._encontrar_minimo(nodo.derecho)
            nodo.dato = sucesor.dato
            # Eliminar el sucesor del subarbol derecho
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.dato)
        
        return nodo
    
    def _encontrar_minimo(self, nodo: NodoABB[T]) -> NodoABB[T]:
        """
        Encuentra el nodo con el valor minimo en un subarbol.
        
        Argumentos:
            nodo: Raiz del subarbol
        
        Returns:
            El nodo con el valor minimo
        
        Limitacion: Asume que el subarbol no esta vacio
        """
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual
    
    # MÉTODOS DE RECORRIDO
    
    def recorrer_inorden(self) -> Iterator[T]:
        """
        Recorrido inorden: izquierda - raiz - derecha.
        
        Complejidad: O(n) - n = tamano del árbol
        
        Yields:
            Los elementos en orden ascendente
        
        Limitación: No modifica el árbol durante el recorrido
        
        Nota: Este recorrido es util para obtener los datos ordenados
        """
        return self._recorrer_inorden_recursivo(self._raiz)
    
    def _recorrer_inorden_recursivo(self, nodo: Optional[NodoABB[T]]) -> Iterator[T]:
        """Método recursivo para recorrido inorden."""
        if nodo is not None:
            yield from self._recorrer_inorden_recursivo(nodo.izquierdo)
            yield nodo.dato
            yield from self._recorrer_inorden_recursivo(nodo.derecho)
    
    def recorrer_preorden(self) -> Iterator[T]:
        """
        Recorrido preorden: raiz - izquierda - derecha.
        
        Complejidad: O(n) - n = tamano del árbol
        
        Yields:
            Los elementos en orden preorden
        
        Limitación: No modifica el árbol durante el recorrido
        
        Nota: Util para copiar el árbol o guardar su estructura
        """
        return self._recorrer_preorden_recursivo(self._raiz)
    
    def _recorrer_preorden_recursivo(self, nodo: Optional[NodoABB[T]]) -> Iterator[T]:
        """Método recursivo para recorrido preorden."""
        if nodo is not None:
            yield nodo.dato
            yield from self._recorrer_preorden_recursivo(nodo.izquierdo)
            yield from self._recorrer_preorden_recursivo(nodo.derecho)
    
    def recorrer_postorden(self) -> Iterator[T]:
        """
        Recorrido postorden: izquierda - derecha - raiz.
        
        Complejidad: O(n) - n = tamano del árbol
        
        Yields:
            Los elementos en orden postorden
        
        Limitación: No modifica el árbol durante el recorrido
        
        Nota: Util para eliminar el arbol de forma segura
        """
        return self._recorrer_postorden_recursivo(self._raiz)
    
    def _recorrer_postorden_recursivo(self, nodo: Optional[NodoABB[T]]) -> Iterator[T]:
        """Metodo recursivo para recorrido postorden."""
        if nodo is not None:
            yield from self._recorrer_postorden_recursivo(nodo.izquierdo)
            yield from self._recorrer_postorden_recursivo(nodo.derecho)
            yield nodo.dato
    
    def recorrer_por_niveles(self) -> Iterator[T]:
        """
        Recorrido por niveles (BFS - Breadth First Search).
        
        Complejidad: O(n) - n = tamano del arbol
        
        Yields:
            Los elementos nivel por nivel (de arriba a abajo)
        
        Limitacion: Requiere una cola auxiliar
        No soporta recorrido en profundidad
        """
        if self.esta_vacio():
            return
        
        # Usamos una cola simple con lista
        cola = [self._raiz]
        
        while cola:
            nodo = cola.pop(0)  # FIFO
            yield nodo.dato
            
            if nodo.izquierdo is not None:
                cola.append(nodo.izquierdo)
            if nodo.derecho is not None:
                cola.append(nodo.derecho)
    
    # ========== METODOS DE CONSULTA ==========
    
    def esta_vacio(self) -> bool:
        """Verifica si el arbol esta vacio. Complejidad: O(1)"""
        return self._raiz is None
    
    def tamano(self) -> int:
        """Retorna el numero de elementos. Complejidad: O(1)"""
        return self._tamano
    
    def altura(self) -> int:
        """
        Calcula la altura del arbol.
        
        Complejidad: O(n) - n = tamano del arbol
        
        Returns:
            La altura del arbol (0 si esta vacio)
        
        Limitacion: Recorre todo el arbol para calcular la altura
        """
        return self._calcular_altura(self._raiz)
    
    def _calcular_altura(self, nodo: Optional[NodoABB[T]]) -> int:
        """Metodo recursivo para calcular la altura."""
        if nodo is None:
            return 0
        return 1 + max(
            self._calcular_altura(nodo.izquierdo),
            self._calcular_altura(nodo.derecho)
        )
    
    def __len__(self) -> int:
        """Permite usar len(arbol)."""
        return self._tamano
    
    def __contains__(self, dato: T) -> bool:
        """Permite usar 'dato in arbol'."""
        return self.buscar(dato) is not None
    
    def to_list(self) -> List[T]:
        """
        Convierte el arbol a una lista ordenada.
        
        Complejidad: O(n) - n = tamano del arbol
        
        Returns:
            Lista con todos los elementos en orden ascendente
        
        Limitacion: Crea una nueva lista, no modifica el arbol
        """
        return list(self.recorrer_inorden())
    
    def __str__(self) -> str:
        """Representacion en string del arbol (recorrido inorden)."""
        if self.esta_vacio():
            return "ArbolBinario: []"
        
        elementos = list(self.recorrer_inorden())
        return f"ArbolBinario: [{', '.join(str(e) for e in elementos)}]"