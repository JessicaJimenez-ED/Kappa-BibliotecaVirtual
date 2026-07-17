"""
Módulo: Tabla Hash
Sprint 6 - Estructuras de datos: Hashing

Se utiliza:
- dict de Python: Tabla hash nativa
- hashlib: Para función hash (opcional, demostrativo)

Características:
- Búsqueda O(1) en promedio
- Manejo automático de colisiones (dict)
- Redimensionamiento automático
- Función hash optimizada

Complejidades:
- Inserción: O(1) promedio
- Búsqueda: O(1) promedio
- Eliminación: O(1) promedio

Limitaciones:
- Las claves deben ser hashables (strings, ints, etc.)
- El orden de inserción no se mantiene (a menos que se use OrderedDict)
- No soporta claves no hashables (listas, diccionarios, etc.)
"""

from typing import Any, Optional, List, Tuple, Iterator, Dict
import hashlib  # Biblioteca estándar de hashing para python


class TablaHash:
    """
    Tabla Hash utilizando la biblioteca estándar dict de Python.
    
    Uso en el proyecto:
    - Índice por ISBN: búsqueda O(1) de libros
    - Caché de usuarios: Acceso instantáneo
    - Registro de préstamos activos
    
    La tabla utiliza la implementación nativa de Python,
    que ya maneja colisiones y redimensionamiento automaticamente.
    """
    
    def __init__(self):
        """Inicializa una tabla hash vacia usando dict de Python."""
        self._tabla: Dict[str, Any] = {}  # Dict es una tabla hash en Python
        self._tamano: int = 0
    
    # FUNCIÓN HASH 
    
    def _hash_demo(self, clave: str) -> str:
        """
        Función hash demostrativa usando biblioteca hashlib.
        
        NOTA: Esta función es solo para demostración en el código.
        En la práctica, Python usa su propio hash interno para dict.
        
        Complejidad: O(len(clave))
        
        Argumentos:
            clave: Clave a hashear
        
        Returns:
            Hash de la clave en formato hexadecimal
        
        Limitacion: Funcion hash criptografica (SHA-256) - mas lenta que
        el hash nativo de Python, pero util para demostracion.
        """
        return hashlib.sha256(clave.encode()).hexdigest()
    
    def _hash_python(self, clave: str) -> int:
        """
        Hash nativo de Python (usado internamente por dict).
        
        Complejidad: O(len(clave))
        
        Argumentos:
            clave: Clave a hashear
        
        Returns:
            Hash entero de la clave
        
        Limitacion: No se usa directamente, pero se muestra para documentacion.
        """
        return hash(clave)
    
    # MÉTODOS DE INSERCIÓN
    
    def insertar(self, clave: str, valor: Any) -> None:
        """
        Inserta un par clave-valor en la tabla hash.
        
        Complejidad: O(1) promedio
        
        Argumentos:
            clave: Clave (ej: ISBN de libro)
            valor: Valor a almacenar (ej: objeto Libro)
        
        Limitación: Si la clave ya existe, se actualiza el valor
        """
        if clave is None:
            raise ValueError("La clave no puede ser None")
        
        # Python dict maneja colisiones automaticamente
        self._tabla[clave] = valor
        self._tamano = len(self._tabla)
    
    # MÉTODOS DE BÚSQUEDA
    
    def buscar(self, clave: str) -> Optional[Any]:
        """
        Busca un valor por su clave.
        
        Complejidad: O(1) promedio
        
        Argumentos:
            clave: Clave a buscar
        
        Returns:
            El valor asociado, o None si no existe
        """
        if clave is None:
            return None
        
        return self._tabla.get(clave)
    
    def contiene(self, clave: str) -> bool:
        """
        Verifica si una clave existe en la tabla.
        
        Complejidad: O(1) promedio
        """
        return clave in self._tabla
    
    # MÉTODOS DE ELIMINACIÓN
    
    def eliminar(self, clave: str) -> bool:
        """
        Elimina un par clave-valor de la tabla.
        
        Complejidad: O(1) promedio
        
        Argumentos:
            clave: Clave a eliminar
        
        Returns:
            True si se elimino correctamente, False si no existia
        """
        if clave is None:
            return False
        
        if clave in self._tabla:
            del self._tabla[clave]
            self._tamano = len(self._tabla)
            return True
        
        return False
    
    def vaciar(self) -> None:
        """Vacia completamente la tabla hash."""
        self._tabla.clear()
        self._tamano = 0
    
    # MÉTODOS DE RECORRIDO
    
    def iterar(self) -> Iterator[Tuple[str, Any]]:
        """
        Iterador para recorrer todos los elementos de la tabla.
        
        Complejidad: O(n) - n = numero de elementos
        
        Yields:
            Tuplas (clave, valor)
        
        Limitacion: No modifica la tabla durante el recorrido
        """
        for clave, valor in self._tabla.items():
            yield (clave, valor)
    
    def obtener_todas_claves(self) -> List[str]:
        """Retorna todas las claves de la tabla."""
        return list(self._tabla.keys())
    
    def obtener_todos_valores(self) -> List[Any]:
        """Retorna todos los valores de la tabla."""
        return list(self._tabla.values())
    
    # MÉTODOS DE CONSULTA
    
    def tamano(self) -> int:
        """Retorna el número de elementos en la tabla."""
        return self._tamano
    
    def esta_vacia(self) -> bool:
        """Verifica si la tabla está vacía."""
        return self._tamano == 0
    
    def __len__(self) -> int:
        """Permite usar len(tabla)."""
        return self._tamano
    
    def __contains__(self, clave: str) -> bool:
        """Permite usar 'clave in tabla'."""
        return self.contiene(clave)
    
    def __str__(self) -> str:
        """Representación en string de la tabla."""
        if self.esta_vacia():
            return "TablaHash: vacía"
        
        elementos = []
        for clave, valor in self.iterar():
            elementos.append(f"{clave}: {valor}")
        
        return f"TablaHash (tam={self._tamano}):\n" + "\n".join(elementos)
    
    # DEMOSTRACIÓN DE HASH (OPCIONAL)
    
"""     def mostrar_hash_demo(self, clave: str) -> None:
        
        Método demostrativo para mostrar el hash de una clave.
        
        Esto cumple con el requisito de documentar la función hash.
        
        hash_sha256 = self._hash_demo(clave)
        hash_python = self._hash_python(clave)
        
        print(f"\n--- Demostracion de Hash ---")
        print(f"Clave: {clave}")
        print(f"Hash SHA-256 (hashlib): {hash_sha256[:16]}...")
        print(f"Hash Python (nativo): {hash_python}")
        print(f"Indice en tabla: {hash_python % 16} (simulado)")
"""