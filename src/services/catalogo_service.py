"""
Servicio: Catálogo de Libros
Utiliza la Lista Enlazada para gestionar el catálogo de libros.

El catálogo es dinámico y permite:
- Agregar libros (al inicio, final o posición específica)
- Eliminar libros por ISBN o posición
- Buscar libros por título o autor
- Recorrer todos los libros
"""

from src.structures.listaEnlazada import ListaEnlazada
from src.models.libro import Libro
from typing import Optional, List, Iterator

class CatalogoService:
    """
    Servicio que gestiona el catálogo de libros usando Lista Enlazada.
    
    ¿Por qué usar Lista Enlazada?
    - Inserción y eliminación frecuente de libros en posiciones intermedias: O(1)
    - No necesitamos acceso aleatorio rápido (no es como un array)
    - Podemos recorrer en ambos sentidos (doble enlace)
    - Tamaño dinámico sin necesidad de redimensionar
    """
    
    def __init__(self):
        """Inicializa el catálogo con una lista enlazada vacía"""
        self._libros = ListaEnlazada[Libro]()
        self._contador_isbn = 1  # Para generar ISBNs autoincrementales en demo
    
    def agregar_libro(self, titulo: str, autor: str, anio: int) -> Libro:
        """
        Agrega un nuevo libro al final del catálogo.
        
        Args:
            titulo: Título del libro
            autor: Autor del libro
            anio: Año de publicación
        
        Returns:
            El libro creado
        
        Limitación: La inserción es al final (O(1)), 
        no hay ordenamiento automático
        """
        isbn = f"ISBN-{self._contador_isbn:04d}"
        self._contador_isbn += 1
        
        libro = Libro(isbn, titulo, autor, anio)
        self._libros.insertar_final(libro)
        
        return libro
    
    def agregar_libro_inicio(self, libro: Libro) -> None:
        """
        Agrega un libro al inicio del catálogo.
        
        Complejidad: O(1)
        
        Args:
            libro: Libro a agregar
        
        Limitación: Desordena el catálogo si antes estaba ordenado
        """
        self._libros.insertar_inicio(libro)
    
    def agregar_libro_posicion(self, posicion: int, libro: Libro) -> bool:
        """
        Agrega un libro en una posición específica del catálogo.
        
        Complejidad: O(n)
        
        Args:
            posicion: Índice donde insertar
            libro: Libro a agregar
        
        Returns:
            True si se insertó correctamente
        
        Limitación: Requiere conocer la posición exacta
        """
        return self._libros.insertar_en_posicion(posicion, libro)
    
    def eliminar_libro(self, isbn: str) -> Optional[Libro]:
        """
        Elimina un libro del catálogo por su ISBN.
        
        Complejidad: O(n) - n = tamaño del catálogo
        
        Args:
            isbn: ISBN del libro a eliminar
        
        Returns:
            El libro eliminado o None si no existe
        
        Limitación: Busca secuencialmente, no hay indexación por ISBN
        """
        # Buscar el libro por ISBN
        for libro in self._libros.recorrer_adelante():
            if libro.isbn == isbn:
                # Guardar referencia antes de eliminar
                libro_eliminado = libro
                self._libros.eliminar_por_valor(libro)
                return libro_eliminado
        
        return None
    
    def eliminar_por_posicion(self, posicion: int) -> Optional[Libro]:
        """
        Elimina un libro del catálogo por su posición.
        
        Complejidad: O(n)
        
        Args:
            posicion: Índice del libro a eliminar
        
        Returns:
            El libro eliminado o None si la posición es inválida
        """
        return self._libros.eliminar_en_posicion(posicion)
    
    def buscar_por_titulo(self, titulo: str) -> list[Libro]:
        """
        Busca libros que coincidan parcialmente con el título.
        
        Complejidad: O(n) - n = tamaño del catálogo
        
        Args:
            titulo: Título o parte del título a buscar
        
        Returns:
            Lista de libros que coinciden con la búsqueda
        
        Limitación: La búsqueda es secuencial y sensible a mayúsculas/minúsculas
        """
        resultados = []
        titulo_busqueda = titulo.lower()
        
        for libro in self._libros.recorrer_adelante():
            if titulo_busqueda in libro.titulo.lower():
                resultados.append(libro)
        
        return resultados
    
    def buscar_por_autor(self, autor: str) -> list[Libro]:
        """
        Busca libros por autor (coincidencia exacta).
        
        Complejidad: O(n) - n = tamaño del catálogo
        
        Args:
            autor: Nombre del autor a buscar
        
        Returns:
            Lista de libros del autor
        
        Limitación: Requiere coincidencia exacta del nombre del autor
        """
        resultados = []
        autor_busqueda = autor.lower()
        
        for libro in self._libros.recorrer_adelante():
            if autor_busqueda in libro.autor.lower():
                resultados.append(libro)
        
        return resultados
    
    def buscar_por_isbn(self, isbn: str) -> Optional[Libro]:
        """
        Busca un libro por su ISBN.
        
        Complejidad: O(n) - n = tamaño del catálogo
        
        Args:
            isbn: ISBN del libro a buscar
        
        Returns:
            El libro encontrado o None
        
        Limitación: No soporta búsqueda binaria, es secuencial
        """
        for libro in self._libros.recorrer_adelante():
            if libro.isbn == isbn:
                return libro
        return None
    
    def listar_libros(self) -> List[Libro]:
        """
        Obtiene todos los libros del catálogo en orden.
        
        Returns:
            Lista de todos los libros
        
        Limitación: Crea una nueva lista, no modifica la estructura
        """
        return self._libros.to_list()
    
    def recorrer_catalogo(self) -> Iterator[Libro]:
        """
        Recorre el catálogo de libros hacia adelante.
        
        Yields:
            Cada libro en orden
        
        Limitación: No permite modificar la lista durante el recorrido
        """
        for libro in self._libros.recorrer_adelante():
            yield libro
    
    def recorrer_inverso(self) -> Iterator[Libro]:
        """
        Recorre el catálogo de libros hacia atrás (último → primero).
        
        Yields:
            Cada libro en orden inverso
        
        Limitación: No permite modificar la lista durante el recorrido
        """
        for libro in self._libros.recorrer_atras():
            yield libro
    
    def cantidad_libros(self) -> int:
        """Retorna el número de libros en el catálogo"""
        return len(self._libros)
    
    def esta_vacio(self) -> bool:
        """Verifica si el catálogo está vacío"""
        return self._libros.esta_vacia()
    
    def mostrar_catalogo(self) -> None:
        """
        Muestra el catálogo en consola de manera formateada.
        """
        print("\n" + "="*60)
        print("CATÁLOGO DE LIBROS")
        print("="*60)
        
        if self.esta_vacio():
            print("📚 El catálogo está vacío")
            return
        
        for i, libro in enumerate(self._libros.recorrer_adelante(), 1):
            estado = "✅ Disponible" if libro.disponible else "❌ Prestado"
            print(f"{i:3}. {libro.isbn} | {libro.titulo}")
            print(f"     Autor: {libro.autor} | Año: {libro.anio} | {estado}")
        
        print(f"\nTotal de libros: {self.cantidad_libros()}")