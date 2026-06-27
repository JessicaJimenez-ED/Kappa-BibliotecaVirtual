"""
Sprint 3 - Listas Enlazadas y Catálogo de Libros
Este módulo contiene la función principal que demuestra el uso de las estructuras de datos Pila, Cola
Demostración de las estructuras implementadas en el contexto de la biblioteca virtual.
A esta demostración se le agregan las funcionalidades de búsqueda y recorrido del catálogo de libros.
"""

from src.structures.pila import Pila # Llamando a la clase Pila desde el módulo pila.py
from src.structures.cola import Cola # Llamando a la clase Cola desde el módulo cola.py
from src.models.libro import Libro # Llamando a la clase Libro desde el módulo libro.py
from src.models.usuario import Usuario # Llamando a la clase Usuario desde el módulo usuario.py
from src.services.historial_service import HistorialService # Llamando a la clase HistorialService desde el módulo historial_service.py
from src.services.reserva_service import ReservaService # Llamando a la clase ReservaService desde el módulo reserva_service.py
from src.services.catalogo_service import CatalogoService # Llamando a la clase CatalogoService desde el módulo catalogo_service.py
from src.structures.listaEnlazada import ListaEnlazada # Llamando a la clase ListaEnlazada desde el módulo lista_enlazada.py


def demostrar_pila():
    """Demostración del funcionamiento de la Pila"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN DE PILA")
    print("="*50)
    
    pila = Pila()
    
    # Agregar elementos
    print("\n1. Agregando elementos (push):")
    pila.push("Acción 1: Inicio sesión")
    pila.push("Acción 2: Buscar libro")
    pila.push("Acción 3: Prestar libro")
    print(pila)
    
    # Ver elementos
    print(f"\n2. Ver cima (peek): {pila.peek()}")
    
    # Eliminar elementos
    print(f"\n3. Eliminar cima (pop): {pila.pop()}")
    print(pila)
    
    # Verificar estado
    print(f"\n4. ¿Está vacía?: {pila.is_empty()}")
    print(f"5. Tamaño: {pila.size()}")


def demostrar_cola():
    """Demostración del funcionamiento de la Cola"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN DE COLA")
    print("="*50)
    
    cola = Cola()
    
    # Agregar elementos
    print("\n1. Agregando elementos (enqueue):")
    cola.enqueue("Reserva 1")
    cola.enqueue("Reserva 2")
    cola.enqueue("Reserva 3")
    print(cola)
    
    # Ver elemento del frente
    print(f"\n2. Ver frente (front): {cola.front()}")
    
    # Eliminar elementos
    print(f"\n3. Eliminar frente (dequeue): {cola.dequeue()}")
    print(cola)
    
    # Verificar estado
    print(f"\n4. ¿Está vacía?: {cola.is_empty()}")
    print(f"5. Tamaño: {cola.size()}")


def demostrar_servicios():
    """Demostración de los servicios que utilizan Pila y Cola"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN DE SERVICIOS")
    print("="*50)
    
    # Servicio de Historial (usa Pila)
    print("\n--- SERVICIO DE HISTORIAL (PILA) ---")
    historial = HistorialService()
    historial.agregar_accion("Usuario inició sesión")
    historial.agregar_accion("Buscó 'El principito'")
    historial.agregar_accion("Prestó 'Cien años de soledad'")
    historial.mostrar_historial()
    
    print(f"\nÚltima acción: {historial.ver_ultima_accion()}")
    print(f"Deshaciendo: {historial.deshacer()}")
    historial.mostrar_historial()
    
    # Servicio de Reservas (usa Cola)
    print("\n--- SERVICIO DE RESERVAS (COLA) ---")
    reservas = ReservaService()
    
    # Crear algunos libros y usuarios
    libro1 = Libro("123", "Python Básico", "Juan Pérez", 2020)
    libro2 = Libro("456", "Java Avanzado", "María García", 2021)
    usuario1 = Usuario("U001", "Carlos", "carlos@email.com")
    usuario2 = Usuario("U002", "Ana", "ana@email.com")
    usuario3 = Usuario("U003", "Luis", "luis@email.com")
    
    # Crear reservas
    reservas.crear_reserva(usuario1, libro1)
    reservas.crear_reserva(usuario2, libro2)
    reservas.crear_reserva(usuario3, libro1)
    
    # Mostrar estado
    reservas.mostrar_reservas()
    print(f"\nCantidad de reservas: {reservas.cantidad_reservas()}")
    
    # Atender reservas (FIFO)
    print("\nAtendiendo reservas:")
    reservas.atender_reserva()
    reservas.atender_reserva()
    
    # Mostrar estado final
    reservas.mostrar_reservas()


def demostrar_lista_enlazada():
    """
    Demostración de la Lista Doblemente Enlazada
    
    COMPLEJIDAD DE LAS OPERACIONES:
    - Agregar libro: O(1) - Inserción al final
    - Buscar por título: O(n) - Búsqueda secuencial
    - Buscar por autor: O(n) - Búsqueda secuencial
    - Buscar por ISBN: O(n) - Búsqueda secuencial
    - Eliminar libro: O(n) - Búsqueda + eliminación
    - Recorrer catálogo: O(n) - Recorrido completo
    
    NOTA: No soporta búsqueda binaria porque es una lista enlazada,
    no un arreglo ordenado.
    """
    print("\n" + "="*60)
    print("DEMOSTRACIÓN DE LISTA ENLAZADA")
    print("="*60)
    
    # Crear lista de números
    lista = ListaEnlazada()
    
    print("\n1. Insertando elementos:")
    lista.insertar_final(10)
    lista.insertar_final(20)
    lista.insertar_final(30)
    lista.insertar_inicio(5)
    print(lista)
    
    print("\n2. Insertando en posición 2:")
    lista.insertar_en_posicion(2, 15)
    print(lista)
    
    print("\n3. Eliminando al inicio:")
    eliminado = lista.eliminar_inicio()
    print(f"Eliminado: {eliminado}")
    print(lista)
    
    print("\n4. Buscando elemento 15:")
    posicion = lista.buscar(15)
    print(f"Posición: {posicion}")
    
    print("\n5. Recorrido hacia adelante:")
    for elemento in lista.recorrer_adelante():
        print(f"  → {elemento}")
    
    print("\n6. Recorrido hacia atrás:")
    for elemento in lista.recorrer_atras():
        print(f"  ← {elemento}")


def demostrar_catalogo():
    """Demostración del catálogo de libros"""
    print("\n" + "="*60)
    print("Demostración del Catálogo de Libros")
    print("="*60)
    
    catalogo = CatalogoService()
    
    # Agregar libros
    print("\n1. Agregando libros al catálogo:")
    libro1 = catalogo.agregar_libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = catalogo.agregar_libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985)
    libro3 = catalogo.agregar_libro("Don Quijote", "Miguel de Cervantes", 1605)
    libro4 = catalogo.agregar_libro("El principito", "Antoine de Saint-Exupéry", 1943)
    libro5 = catalogo.agregar_libro("1984", "George Orwell", 1949)
    
    print(f"Agregados {catalogo.cantidad_libros()} libros")
    
    # Mostrar catálogo
    catalogo.mostrar_catalogo()
    
    # Buscar por título
    print("\n2. Buscando libros con 'amor' en el título:")
    resultados = catalogo.buscar_por_titulo("amor")
    for libro in resultados:
        print(f"  📖 {libro.titulo} - {libro.autor}")
    
    # Buscar por autor
    print("\n3. Buscando libros de Gabriel García Márquez:")
    resultados = catalogo.buscar_por_autor("Gabriel García Márquez")
    for libro in resultados:
        print(f"  📖 {libro.titulo} ({libro.anio})")
    
    # Buscar por ISBN
    print("\n4. Buscando libro por ISBN:")
    isbn_buscar = libro3.isbn
    libro_encontrado = catalogo.buscar_por_isbn(isbn_buscar)
    if libro_encontrado:
        print(f"Libro Encontrado: {libro_encontrado}")
    
    # Eliminar un libro
    print(f"\n5. Eliminando libro: {libro2.titulo}")
    eliminado = catalogo.eliminar_libro(libro2.isbn)
    if eliminado:
        print(f"Libro Eliminado: {eliminado.titulo}")
    
    # Mostrar catálogo actualizado
    catalogo.mostrar_catalogo()
    
    # Recorrido inverso
    print("\n6. Recorrido inverso del catálogo (último → primero):")
    for libro in catalogo.recorrer_inverso():
        print(f"{libro.titulo}")


def main():
    """Función principal que ejecuta todas las demostraciones"""
    print("="*60)
    print("  BIBLIOTECA VIRTUAL - SPRINT 3")
    print("  Pilas | Colas | Listas Enlazadas")
    print("="*60)
    
    demostrar_pila() # Función que demuestra el funcionamiento de la Pila
    demostrar_cola() # Función que demuestra el funcionamiento de la Cola
    demostrar_servicios() # Función que demuestra los servicios de Historial y Reservas
    demostrar_lista_enlazada() # Función que demuestra la Lista Doblemente Enlazada
    demostrar_catalogo() # Función que demuestra el Catálogo de Libros con búsqueda y recorrido
    
    print("\n" + "="*50)
    print("Fin de la demostración.")
    print("="*50)


if __name__ == "__main__":
    main()