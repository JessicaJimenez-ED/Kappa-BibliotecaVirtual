"""
Servicio: Cache de Libros
Utiliza Tabla Hash para acceso instantáneo.

Uso en el proyecto:
- Caché de libros mas consultados
- Acceso instantáneo por ISBN (O(1))
- Almacenamiento temporal de usuarios activos
"""

from structures.tablaHash import TablaHash
from models.libro import Libro
from typing import Optional, List


class CacheService:
    """
    Servicio de caché que utiliza Tabla Hash.
    
    La tabla hash usa dict de Python, proporcionando rendimiento O(1) en todas las operaciones.
    """
    
    def __init__(self):
        """Inicializa el caché con una tabla hash."""
        self._cache = TablaHash()
        self._estadisticas = {
            'aciertos': 0,
            'fallos': 0
        }
    
    def agregar(self, isbn: str, libro: Libro) -> None:
        """Agrega un libro al caché. O(1) promedio."""
        self._cache.insertar(isbn, libro)
    
    def buscar(self, isbn: str) -> Optional[Libro]:
        """Busca un libro en el caché. O(1) promedio."""
        libro = self._cache.buscar(isbn)
        if libro is not None:
            self._estadisticas['aciertos'] += 1
        else:
            self._estadisticas['fallos'] += 1
        return libro
    
    def eliminar(self, isbn: str) -> bool:
        """Elimina un libro del caché. O(1) promedio."""
        return self._cache.eliminar(isbn)
    
    def esta_en_cache(self, isbn: str) -> bool:
        """Verifica si un libro esta en caché."""
        return isbn in self._cache
    
    def vaciar(self) -> None:
        """Vacia completamente el caché."""
        self._cache.vaciar()
        self._estadisticas['aciertos'] = 0
        self._estadisticas['fallos'] = 0
    
    def tamano(self) -> int:
        """Retorna el número de elementos en caché."""
        return self._cache.tamano()
    
    def estadisticas(self) -> dict:
        """Retorna estadisticas de uso del caché."""
        total = self._estadisticas['aciertos'] + self._estadisticas['fallos']
        if total > 0:
            tasa_acierto = self._estadisticas['aciertos'] / total * 100
        else:
            tasa_acierto = 0
        
        return {
            'aciertos': self._estadisticas['aciertos'],
            'fallos': self._estadisticas['fallos'],
            'total': total,
            'tasa_acierto': f"{tasa_acierto:.1f}%",
            'tamano_cache': self.tamano()
        }
    
    def listar_todos(self) -> List[Libro]:
        """Lista todos los libros en cache."""
        return self._cache.obtener_todos_valores()
    
    def demostrar_hash(self, isbn: str) -> None:
        """Demuestra la función hash para un ISBN."""
        self._cache.mostrar_hash_demo(isbn)
    
    def __str__(self) -> str:
        return str(self._cache)