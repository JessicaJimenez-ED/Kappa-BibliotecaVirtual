"""
Modulo: Árbol AVL
Sprint 4 - Estructuras de datos: Árbol AVL
Implementación desde cero de un árbol binario de busqueda auto-balanceado (AVL)

Caracteristicas:
- Árbol binario de búsqueda auto-balanceado
- Mantiene la altura balanceada con rotaciones
- Factor de balance: altura(izquierdo) - altura(derecho) ∈ {-1, 0, 1}
- Todas las operaciones garantizan O(log n)

Complejidades:
- Inserción: O(log n) siempre
- Búsqueda: O(log n) siempre
- Eliminación: O(log n) siempre
- Rotaciones: O(1) cada una

Limitaciónes:
- Más complejo de implementar que un ABB simple
- Mayor overhead por el almacenamiento de alturas
- Las rotaciones pueden ser costosas si se hacen frecuentemente
"""

from typing import Optional, TypeVar, Generic, Iterator, List # Se importan tipos para anotaciones de tipo y generics
from __future__ import annotations

T = TypeVar('T') # Tipo genérico para los datos almacenados en el arbol AVL


class NodoAVL(Generic[T]):
    """
    Nodo del Árbol AVL.
    Contiene el dato, referencias a los subarboles, y la altura del nodo.
    """
    
    def __init__(self, dato: T):
        """
        Inicializa un nodo AVL con el dato proporcionado.
        
        Argumentos:
            dato: El dato a almacenar en el nodo
        
        Limitación: No puede almacenar None como dato valido
        """
        self.dato: T = dato
        self.izquierdo: Optional[NodoAVL[T]] = None
        self.derecho: Optional[NodoAVL[T]] = None
        self.altura: int = 1  # Altura del nodo (hoja = 1)
    
    def __str__(self) -> str:
        return str(self.dato)


class ArbolAVL(Generic[T]):
    """
    Árbol AVL (Adelson-Velsky y Landis) genérico.
    
    Uso en el proyecto:
    - Busqueda rápida de libros por ISBN con rendimiento garantizado
    - Catálogo ordenado por titulo sin riesgo de degeneracion
    - Base de datos de indices para busquedas eficientes
    
    El AVL garantiza que la altura del árbol sea O(log n) siempre,
    mediante rotaciones cuando el factor de balance se desvia.
    
    Factor de balance = altura(subárbol_izquierdo) - altura(subárbol_derecho)
    Valores permitidos: -1, 0, 1
    """
    
    def __init__(self):
        """Inicializa un árbol AVL vacio."""
        self._raiz: Optional[NodoAVL[T]] = None
        self._tamano: int = 0
    
    # MÉTODOS DE INSERCIÓN
    
    def insertar(self, dato: T) -> bool:
        """
        Inserta un nuevo dato en el árbol AVL.
        
        Complejidad: O(log n) siempre
        
        Argumentos:
            dato: Dato a insertar
        
        Returns:
            True si se inserto correctamente, False si ya existia
        
        Limitación: No permite duplicados
        """
        if dato is None:
            raise ValueError("No se puede insertar None en el arbol")
        
        if self.buscar(dato) is not None:
            return False  # No se permiten duplicados
        
        self._raiz = self._insertar_recursivo(self._raiz, dato)
        self._tamano += 1
        return True
    
    def _insertar_recursivo(self, nodo: Optional[NodoAVL[T]], dato: T) -> NodoAVL[T]:
        """
        Metodo recursivo para insertar un dato en el arbol AVL.
        
        Argumentos:
            nodo: Nodo actual en la recursion
            dato: Dato a insertar
        
        Returns:
            El nodo actualizado y balanceado
        
        Limitación: Recursion puede causar stack overflow en arboles muy grandes
        """
        # Paso 1: Insercion normal de ABB
        if nodo is None:
            return NodoAVL(dato)
        
        if dato < nodo.dato:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, dato)
        else:
            return nodo  # No se permiten duplicados
        
        # Paso 2: Actualizar altura del nodo actual
        nodo.altura = 1 + max(
            self._obtener_altura(nodo.izquierdo),
            self._obtener_altura(nodo.derecho)
        )
        
        # Paso 3: Calcular factor de balance
        balance = self._obtener_balance(nodo)
        
        # Paso 4: Realizar rotaciones si es necesario
        # Caso 1: Rotacion derecha (LL)
        if balance > 1 and dato < nodo.izquierdo.dato:
            return self._rotar_derecha(nodo)
        
        # Caso 2: Rotacion izquierda (RR)
        if balance < -1 and dato > nodo.derecho.dato:
            return self._rotar_izquierda(nodo)
        
        # Caso 3: Rotacion izquierda-derecha (LR)
        if balance > 1 and dato > nodo.izquierdo.dato:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)
        
        # Caso 4: Rotacion derecha-izquierda (RL)
        if balance < -1 and dato < nodo.derecho.dato:
            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)
        
        return nodo
    
    # MÉTODOS DE ELIMINACION
    
    def eliminar(self, dato: T) -> bool:
        """
        Elimina un dato del árbol AVL.
        
        Complejidad: O(log n) siempre
        
        Argumentos:
            dato: Dato a eliminar
        
        Returns:
            True si se elimino correctamente, False si no existia
        
        Limitación: La eliminacion en AVL es compleja y requiere re-balanceo
        """
        if self.esta_vacio():
            return False
        
        if self.buscar(dato) is None:
            return False
        
        self._raiz = self._eliminar_recursivo(self._raiz, dato)
        self._tamano -= 1
        return True
    
    def _eliminar_recursivo(self, nodo: Optional[NodoAVL[T]], dato: T) -> Optional[NodoAVL[T]]:
        """
        Metodo recursivo para eliminar un dato del arbol AVL.
        
        Argumentos:
            nodo: Nodo actual en la recursion
            dato: Dato a eliminar
        
        Returns:
            El nodo actualizado y balanceado
        
        Limitación: El balanceo se realiza despues de la eliminacion
        """
        # Paso 1: Eliminacion normal de ABB
        if nodo is None:
            return None
        
        if dato < nodo.dato: # Condicional: si el dato es menor que el nodo actual, se busca en el subarbol izquierdo
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, dato)
        elif dato > nodo.dato: # si el dato es mayor que el nodo actual, se busca en el subarbol derecho
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, dato)
        else:
            # Nodo encontrado
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            
            # Nodo con dos hijos: encontrar sucesor
            sucesor = self._encontrar_minimo(nodo.derecho)
            nodo.dato = sucesor.dato
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.dato)
        
        if nodo is None:
            return None
        
        # Paso 2: Actualizar altura
        nodo.altura = 1 + max(
            self._obtener_altura(nodo.izquierdo),
            self._obtener_altura(nodo.derecho)
        )
        
        # Paso 3: Balancear
        return self._balancear(nodo)
    
    def _balancear(self, nodo: NodoAVL[T]) -> NodoAVL[T]:
        """
        Balancea un nodo específico del arbol AVL.
        
        Argumentos:
            nodo: Nodo a balancear
        
        Returns:
            El nodo balanceado
        
        Limitación: Asume que el factor de balance esta desviado
        """
        balance = self._obtener_balance(nodo)
        
        # Caso 1: Rotacion derecha (LL)
        if balance > 1 and self._obtener_balance(nodo.izquierdo) >= 0:
            return self._rotar_derecha(nodo)
        
        # Caso 2: Rotacion izquierda (RR)
        if balance < -1 and self._obtener_balance(nodo.derecho) <= 0:
            return self._rotar_izquierda(nodo)
        
        # Caso 3: Rotacion izquierda-derecha (LR)
        if balance > 1 and self._obtener_balance(nodo.izquierdo) < 0:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)
        
        # Caso 4: Rotación derecha-izquierda (RL)
        if balance < -1 and self._obtener_balance(nodo.derecho) > 0:
            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)
        
        return nodo
    
    # METODOS DE ROTACION
    
    def _rotar_derecha(self, nodo: NodoAVL[T]) -> NodoAVL[T]:
        """
        Rotación derecha (LL).
        
        Complejidad: O(1)
        
        Argumentos:
            nodo: Nodo a rotar
        
        Returns:
            La nueva raíz del subarbol
        
        Limitación: Asume que el nodo izquierdo existe
        """
        nueva_raiz = nodo.izquierdo
        subarbol_derecho = nueva_raiz.derecho
        
        # Realizar rotación
        nueva_raiz.derecho = nodo
        nodo.izquierdo = subarbol_derecho
        
        # Actualizar alturas
        nodo.altura = 1 + max(
            self._obtener_altura(nodo.izquierdo),
            self._obtener_altura(nodo.derecho)
        )
        nueva_raiz.altura = 1 + max(
            self._obtener_altura(nueva_raiz.izquierdo),
            self._obtener_altura(nueva_raiz.derecho)
        )
        
        return nueva_raiz
    
    def _rotar_izquierda(self, nodo: NodoAVL[T]) -> NodoAVL[T]:
        """
        Rotación izquierda (RR).
        
        Complejidad: O(1)
        
        Argumentos:
            nodo: Nodo a rotar
        
        Returns:
            La nueva raiz del subarbol
        
        Limitación: Asume que el nodo derecho existe
        """
        nueva_raiz = nodo.derecho
        subarbol_izquierdo = nueva_raiz.izquierdo
        
        # Realizar rotación
        nueva_raiz.izquierdo = nodo
        nodo.derecho = subarbol_izquierdo
        
        # Actualizar alturas
        nodo.altura = 1 + max(
            self._obtener_altura(nodo.izquierdo),
            self._obtener_altura(nodo.derecho)
        )
        nueva_raiz.altura = 1 + max(
            self._obtener_altura(nueva_raiz.izquierdo),
            self._obtener_altura(nueva_raiz.derecho)
        )
        
        return nueva_raiz
    
    # METODOS DE CONSULTA Y UTILIDAD
    
    def _obtener_altura(self, nodo: Optional[NodoAVL[T]]) -> int:
        """Obtiene la altura de un nodo (0 si es None)."""
        if nodo is None:
            return 0
        return nodo.altura
    
    def _obtener_balance(self, nodo: NodoAVL[T]) -> int:
        """
        Calcula el factor de balance de un nodo.
        
        Factor = altura(izquierdo) - altura(derecho)
        Valores permitidos: -1, 0, 1
        """
        if nodo is None:
            return 0
        return self._obtener_altura(nodo.izquierdo) - self._obtener_altura(nodo.derecho)
    
    def _encontrar_minimo(self, nodo: NodoAVL[T]) -> NodoAVL[T]:
        """Encuentra el nodo con el valor minimo en un subarbol."""
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual
    
    # METODOS DE BÚSQUEDA
    
    def buscar(self, dato: T) -> Optional[T]:
        """
        Busca un dato en el árbol AVL.
        
        Complejidad: O(log n) siempre
        
        Argumentos:
            dato: Dato a buscar
        
        Returns:
            El dato encontrado, o None si no existe
        """
        if self.esta_vacio():
            return None
        
        nodo = self._buscar_recursivo(self._raiz, dato)
        return nodo.dato if nodo else None
    
    def _buscar_recursivo(self, nodo: Optional[NodoAVL[T]], dato: T) -> Optional[NodoAVL[T]]:
        """Metodo recursivo para buscar un dato."""
        if nodo is None:
            return None
        
        if dato == nodo.dato:
            return nodo
        elif dato < nodo.dato:
            return self._buscar_recursivo(nodo.izquierdo, dato)
        else:
            return self._buscar_recursivo(nodo.derecho, dato)
    
    # METODOS DE RECORRIDO
    
    def recorrer_inorden(self) -> Iterator[T]:
        """Recorrido inorden: izquierda - raiz - derecha."""
        return self._recorrer_inorden_recursivo(self._raiz)
    
    def _recorrer_inorden_recursivo(self, nodo: Optional[NodoAVL[T]]) -> Iterator[T]:
        if nodo is not None:
            yield from self._recorrer_inorden_recursivo(nodo.izquierdo)
            yield nodo.dato
            yield from self._recorrer_inorden_recursivo(nodo.derecho)
    
    def recorrer_preorden(self) -> Iterator[T]:
        """Recorrido preorden: raiz - izquierda - derecha."""
        return self._recorrer_preorden_recursivo(self._raiz)
    
    def _recorrer_preorden_recursivo(self, nodo: Optional[NodoAVL[T]]) -> Iterator[T]:
        if nodo is not None:
            yield nodo.dato
            yield from self._recorrer_preorden_recursivo(nodo.izquierdo)
            yield from self._recorrer_preorden_recursivo(nodo.derecho)
    
    def recorrer_postorden(self) -> Iterator[T]:
        """Recorrido postorden: izquierda - derecha - raiz."""
        return self._recorrer_postorden_recursivo(self._raiz)
    
    def _recorrer_postorden_recursivo(self, nodo: Optional[NodoAVL[T]]) -> Iterator[T]:
        if nodo is not None:
            yield from self._recorrer_postorden_recursivo(nodo.izquierdo)
            yield from self._recorrer_postorden_recursivo(nodo.derecho)
            yield nodo.dato
    
    # ========== METODOS DE CONSULTA ==========
    
    def esta_vacio(self) -> bool:
        """Verifica si el árbol está vacío. Complejidad: O(1)"""
        return self._raiz is None
    
    def tamano(self) -> int:
        """Retorna el numero de elementos. Complejidad: O(1)"""
        return self._tamano
    
    def altura(self) -> int:
        """Calcula la altura del árbol. Complejidad: O(n)"""
        return self._obtener_altura(self._raiz)
    
    def __len__(self) -> int:
        return self._tamano
    
    def __contains__(self, dato: T) -> bool:
        return self.buscar(dato) is not None
    
    def to_list(self) -> List[T]:
        """Convierte el árbol a una lista ordenada."""
        return list(self.recorrer_inorden())
    
    def __str__(self) -> str:
        if self.esta_vacio():
            return "ArbolAVL: []"
        elementos = list(self.recorrer_inorden())
        return f"ArbolAVL: [{', '.join(str(e) for e in elementos)}]"