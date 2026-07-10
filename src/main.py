"""
Sprint 5 - Árboles 2-3 y Árbol B
Demostracion de operaciones con árboles en la biblioteca virtual.
Este modulo integra todas las estructuras implementadas hasta el momento.
"""

# Importaciones de módulos y clases necesarias para la demostración
# Estructuras de datos
from src.structures.pila import Pila # Llamando a la clase Pila desde el módulo pila.py
from src.structures.cola import Cola # Llamando a la clase Cola desde el módulo cola.py
from src.structures.listaEnlazada import ListaEnlazada # Llamando a la clase ListaEnlazada desde el módulo lista_enlazada.py
from src.structures.arbolBinario import ArbolBinario # Llamando a la clase ArbolBinario desde el módulo arbol_binario.py
from src.structures.arbolAVL import ArbolAVL # Llamando a la clase ArbolAVL desde el módulo arbol_avl.py
from src.structures.arbol23 import Arbol23 # Llamando a la clase Arbol23 desde el módulo arbol23.py

# Importaciones de modelos
from src.models.libro import Libro # Llamando a la clase Libro desde el módulo libro.py
from src.models.usuario import Usuario # Llamando a la clase Usuario desde el módulo usuario.py

# Importaciones de servicios que utilizan las estructuras de datos
from src.services.historial_service import HistorialService # Llamando a la clase HistorialService desde el módulo historial_service.py
from src.services.reserva_service import ReservaService # Llamando a la clase ReservaService desde el módulo reserva_service.py
from src.services.catalogo_service import CatalogoService # Llamando a la clase CatalogoService desde el módulo catalogo_service.py
from src.services.busqueda_service import BusquedaService # Llamando a la clase BusquedaService desde el módulo busqueda_service.py
from src.services.indice_service import IndiceService # Llamando a la clase IndiceService desde el módulo indice_service.py

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

def demostrar_arbol_binario():
    """Demostracion del Arbol Binario de Busqueda"""
    print("\n" + "="*60)
    print("DEMOSTRACION DE ARBOL BINARIO DE BUSQUEDA")
    print("="*60)
    
    arbol = ArbolBinario()
    
    # Insertar elementos
    print("\n1. Insertando elementos:")
    datos = [50, 30, 70, 20, 40, 60, 80]
    for dato in datos:
        arbol.insertar(dato)
    print(f"Arbol: {arbol}")
    print(f"Tamano: {len(arbol)}")
    print(f"Altura: {arbol.altura()}")
    
    # Buscar elementos
    print("\n2. Buscando elementos:")
    print(f"Buscar 40: {arbol.buscar(40)}")
    print(f"Buscar 99: {arbol.buscar(99)}")
    
    # Recorridos
    print("\n3. Recorridos:")
    print(f"Inorden (ordenado): {list(arbol.recorrer_inorden())}")
    print(f"Preorden: {list(arbol.recorrer_preorden())}")
    print(f"Postorden: {list(arbol.recorrer_postorden())}")
    print(f"Por niveles: {list(arbol.recorrer_por_niveles())}")
    
    # Eliminar elementos
    print("\n4. Eliminando elemento 30:")
    arbol.eliminar(30)
    print(f"Arbol despues de eliminar 30: {arbol}")
    print(f"Nuevo tamano: {len(arbol)}")


def demostrar_arbol_avl():
    """Demostracion del Arbol AVL (auto-balanceado)"""
    print("\n" + "="*60)
    print("DEMOSTRACION DE ARBOL AVL")
    print("="*60)
    
    arbol_avl = ArbolAVL()
    arbol_abb = ArbolBinario()
    
    # Comparativa con datos ordenados (peor caso para ABB)
    print("\n1. Comparativa con datos ordenados:")
    print("Insertando 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    
    for i in range(1, 11):
        arbol_avl.insertar(i)
        arbol_abb.insertar(i)
    
    print(f"Altura ABB: {arbol_abb.altura()} (puede degenerar)")
    print(f"Altura AVL: {arbol_avl.altura()} (siempre balanceado)")
    
    print("\n2. Recorrido inorden de AVL (ordenado):")
    print(list(arbol_avl.recorrer_inorden()))
    
    # Demostrar balanceo
    print("\n3. Insertando elementos en diferentes ordenes:")
    arbol2 = ArbolAVL()
    
    # Insercion que causa rotacion
    arbol2.insertar(30)
    arbol2.insertar(20)
    arbol2.insertar(10)  # Esta insercion causa rotacion derecha
    
    print(f"Arbol despues de insertar 30, 20, 10:")
    print(f"Elementos: {arbol2.to_list()}")
    print(f"Altura: {arbol2.altura()}")
    
    # Buscar elementos
    print("\n4. Busqueda en AVL:")
    print(f"Buscar 20: {arbol2.buscar(20)}")
    print(f"Buscar 99: {arbol2.buscar(99)}")


def demostrar_busqueda_service():
    """Demostracion del servicio de busqueda con arboles"""
    print("\n" + "="*60)
    print("DEMOSTRACION DEL SERVICIO DE BUSQUEDA")
    print("="*60)
    
    busqueda = BusquedaService()
    
    # Crear libros de ejemplo
    libros = [
        Libro("ISBN-001", "Cien anos de soledad", "Gabriel Garcia Marquez", 1967),
        Libro("ISBN-002", "El amor en los tiempos del colera", "Gabriel Garcia Marquez", 1985),
        Libro("ISBN-003", "Don Quijote", "Miguel de Cervantes", 1605),
        Libro("ISBN-004", "El principito", "Antoine de Saint-Exupery", 1943),
        Libro("ISBN-005", "1984", "George Orwell", 1949),
        Libro("ISBN-006", "Fahrenheit 451", "Ray Bradbury", 1953),
    ]
    
    # Agregar libros al servicio de busqueda
    print("\n1. Agregando libros al indice:")
    for libro in libros:
        busqueda.agregar_libro(libro)
    print(f"Total de libros: {busqueda.cantidad_libros()}")
    
    # Buscar por ISBN
    print("\n2. Busqueda por ISBN:")
    libro = busqueda.buscar_por_isbn("ISBN-003")
    print(f"ISBN-003: {libro.titulo if libro else 'No encontrado'}")
    
    # Buscar por titulo
    print("\n3. Busqueda por titulo:")
    libro = busqueda.buscar_por_titulo("El principito")
    print(f"'El principito': {libro.autor if libro else 'No encontrado'}")
    
    # Buscar por autor
    print("\n4. Busqueda por autor:")
    libros_garcia = busqueda.buscar_por_autor("Gabriel Garcia Marquez")
    print(f"Libros de Gabriel Garcia Marquez: {len(libros_garcia)}")
    for l in libros_garcia:
        print(f"  - {l.titulo} ({l.anio})")
    
    # Listar todos los titulos ordenados
    print("\n5. Todos los titulos en orden alfabetico:")
    titulos = busqueda.listar_por_titulo()
    for titulo in titulos:
        print(f"  - {titulo}")
    
    # Estadisticas de los arboles
    print("\n6. Estadisticas de los indices:")
    stats = busqueda.estadisticas()
    print(f"Total de libros: {stats['total_libros']}")
    print(f"Indice ISBN: tamano={stats['indice_isbn']['tamano']}, altura={stats['indice_isbn']['altura']}")
    print(f"Indice Titulo: tamano={stats['indice_titulo']['tamano']}, altura={stats['indice_titulo']['altura']}")
    print(f"Indice Autor: tamano={stats['indice_autor']['tamano']}, altura={stats['indice_autor']['altura']}")

def demostrar_arbol23():
    """Demostracion del Arbol 2-3 (Sprint 5)"""
    print("\n" + "="*60)
    print("DEMOSTRACION DE ARBOL 2-3")
    print("="*60)
    
    print("\n1. Insertando elementos:")
    arbol = Arbol23()
    
    # Insertar elementos en orden (peor caso para ABB, ideal para 2-3)
    elementos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for elem in elementos:
        arbol.insertar(elem)
        print(f"  Insertado {elem}: altura={arbol.altura()}, elementos={len(arbol)}")
    
    print(f"\n2. Estado final del arbol:")
    print(f"  Elementos: {len(arbol)}")
    print(f"  Altura: {arbol.altura()} (siempre balanceado)")
    print(f"  Recorrido inorden: {arbol.to_list()[:10]}...")
    
    print("\n3. Busqueda en Arbol 2-3 (O(log n)):")
    print(f"  Buscar 50: {'Encontrado' if 50 in arbol else 'No encontrado'}")
    print(f"  Buscar 99: {'Encontrado' if 99 in arbol else 'No encontrado'}")
    

def demostrar_indice_service():
    """Demostracion del servicio de indice con Arbol 2-3 (Sprint 5)"""
    print("\n" + "="*60)
    print("DEMOSTRACION DEL INDICE CON ARBOL 2-3")
    print("="*60)
    
    indice = IndiceService()
    
    # Crear libros de ejemplo
    libros = [
        Libro("978-9582813758", "La culpa es de la vaca", "Jaime López Gutiérrez", 2002),
        Libro("978-8432036262", "Cosmos", "Carl Sagan", 1982),
        Libro("978-0-201-61622-4", "Doña Bárbara", "Rómulo Gallegos", 1929),
        Libro("978-980-15-0498-6", "Guía Caracol Integral 5° Edición Docente", "Santillana", 2011),
        Libro("978-8498382662", "Harry Potter y la piedra filosofal", "J.K. Rowling", 1998),
        Libro("978-84-450-1958-0", "El Señor de los Anillos", "J. R. R. Tolkien", 1977),
    ]
    
    print("\n1. Agregando libros al indice:")
    for libro in libros:
        indice.agregar_libro(libro)
        print(f"  Agregado: {libro.titulo}")
    
    print(f"\n2. Total de libros: {indice.cantidad_libros()}")
    
    print("\n3. Busqueda por ISBN (O(log n)):")
    isbn_buscar = "978-0-13-235088-4"
    libro = indice.buscar_por_isbn(isbn_buscar)
    if libro:
        print(f"  Encontrado: {libro.titulo} por {libro.autor}")
    
    print("\n4. Busqueda por titulo exacto (O(log n)):")
    libro = indice.buscar_por_titulo("Clean Code")
    if libro:
        print(f"  Encontrado: {libro.titulo} (ISBN: {libro.isbn})")
    
    print("\n5. Busqueda por autor (O(log n)):")
    libros_autor = indice.buscar_por_autor("Eric Matthes")
    for l in libros_autor:
        print(f"  - {l.titulo} ({l.anio})")
    
    print("\n6. Estadisticas del indice:")
    stats = indice.estadisticas()
    print(f"  Total libros: {stats['total_libros']}")
    print(f"  ISBN index: {stats['indice_isbn']['tamano']} elementos, altura {stats['indice_isbn']['altura']}")
    print(f"  Titulo index: {stats['indice_titulo']['tamano']} elementos, altura {stats['indice_titulo']['altura']}")
    print(f"  Autor index: {stats['indice_autor']['tamano']} elementos, altura {stats['indice_autor']['altura']}")

def main():
    """Función principal que ejecuta todas las demostraciones"""
    print("="*60)
    print("Biblioteca virtual - Sprint 5")
    print("  Pilas | Colas | Listas Enlazadas | Árboles Binarios | AVL | Árbol 2-3")
    print("="*60)
    
# Sprint 2 - Pilas y Colas
    demostrar_pila()
    demostrar_cola()
    demostrar_servicios()
    
    # Sprint 3 - Listas Enlazadas
    demostrar_lista_enlazada()
    demostrar_catalogo()
    
    # Sprint 4 - Arboles Binarios y AVL
    demostrar_arbol_binario()
    demostrar_busqueda_service()
    
    # Sprint 5 - Arbol 2-3
    demostrar_arbol23()
    demostrar_indice_service()
    
        
    print("\n" + "="*50)
    print("Fin de la demostración.")
    print("="*50)


if __name__ == "__main__":
    main()