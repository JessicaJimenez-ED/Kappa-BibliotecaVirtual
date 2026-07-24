"""
Sistema de Biblioteca Virtual Kappa - Menú Interactivo
Sprint 7 - Entrega Final

Este módulo proporciona una interfaz de consola para interactuar con todas
las funcionalidades del sistema de biblioteca virtual.

Los datos se mantienen en memoria durante toda la ejecución del programa.
"""

import os
import sys
from typing import Optional

# Importaciones de estructuras y servicios
from models.libro import Libro
from models.usuario import Usuario
from services.catalogo_service import CatalogoService
from services.historial_service import HistorialService
from services.reserva_service import ReservaService
from services.busqueda_service import BusquedaService
from services.indice_service import IndiceService
from services.recomendacion_service import RecomendacionService
from services.cache_service import CacheService


class BibliotecaVirtual:
    """
    Clase principal que gestiona el sistema de biblioteca virtual.
    Mantiene todos los servicios y datos en memoria.
    """
    
    def __init__(self):
        """Inicializa todos los servicios y carga datos de ejemplo."""
        print("\n" + "-"*20)
        print("  BIBLIOTECA VIRTUAL KAPPA - INICIALIZANDO")
        print("-"*20)
        
        # Inicializar servicios
        self.catalogo = CatalogoService()
        self.historial = HistorialService()
        self.reservas = ReservaService()
        self.busqueda = BusquedaService()
        self.indice = IndiceService()
        self.recomendacion = RecomendacionService()
        self.cache = CacheService()
        
        # Diccionario para almacenar usuarios registrados
        self.usuarios: dict[str, Usuario] = {}
        
        # Cargar datos de ejemplo
        self._cargar_datos_ejemplo()
        
        # Registrar acción en el historial
        self.historial.agregar_accion("Sistema inicializado")
        
        print("\n Sistema listo para usar!")
        print(f" {self.catalogo.cantidad_libros()} libros cargados")
        print(f" {len(self.usuarios)} usuarios registrados")
    
    def _cargar_datos_ejemplo(self):
        """
        Carga datos de ejemplo para demostración.
        Incluye libros, usuarios y relaciones para recomendaciones.
        """
        print("\n Cargando datos de ejemplo...")
        
        # ====== LIBROS DE EJEMPLO ======
        libros_data = [
            ("ISBN-001", "Cien años de soledad", "Gabriel García Márquez", 1967),
            ("ISBN-002", "El amor en los tiempos del cólera", "Gabriel García Márquez", 1985),
            ("ISBN-003", "Don Quijote de la Mancha", "Miguel de Cervantes", 1605),
            ("ISBN-004", "El principito", "Antoine de Saint-Exupéry", 1943),
            ("ISBN-005", "1984", "George Orwell", 1949),
            ("ISBN-006", "Fahrenheit 451", "Ray Bradbury", 1953),
            ("ISBN-007", "Rebelión en la granja", "George Orwell", 1945),
            ("ISBN-008", "Crónica de una muerte anunciada", "Gabriel García Márquez", 1981),
            ("ISBN-009", "El hobbit", "J.R.R. Tolkien", 1937),
            ("ISBN-010", "El Señor de los Anillos", "J.R.R. Tolkien", 1954),
            ("ISBN-011", "Harry Potter y la piedra filosofal", "J.K. Rowling", 1997),
            ("ISBN-012", "Harry Potter y la cámara secreta", "J.K. Rowling", 1998),
            ("ISBN-013", "Clean Code", "Robert C. Martin", 2008),
            ("ISBN-014", "The Pragmatic Programmer", "Andrew Hunt", 1999),
            ("ISBN-015", "Python Crash Course", "Eric Matthes", 2015),
        ]
        
        # Agregar libros al catálogo, índices y recomendaciones
        for isbn, titulo, autor, anio in libros_data:
            libro = Libro(isbn, titulo, autor, anio)
            self.catalogo.agregar_libro_inicio(libro)
            self.busqueda.agregar_libro(libro)
            self.indice.agregar_libro(libro)
            self.recomendacion.agregar_libro(libro)
            # Agregar algunos libros al cache
            if isbn in ["ISBN-001", "ISBN-005", "ISBN-010", "ISBN-013"]:
                self.cache.agregar(isbn, libro)
        
        # ====== CONEXIONES PARA RECOMENDACIONES ======
        # Conectar por autor
        self.recomendacion.conectar_por_autor("Gabriel García Márquez")
        self.recomendacion.conectar_por_autor("George Orwell")
        self.recomendacion.conectar_por_autor("J.R.R. Tolkien")
        self.recomendacion.conectar_por_autor("J.K. Rowling")
        
        # Conexiones adicionales entre libros similares
        self.recomendacion.conectar_libros("ISBN-004", "ISBN-005")  # El principito -> 1984
        self.recomendacion.conectar_libros("ISBN-009", "ISBN-010")  # El hobbit -> ESDLA
        self.recomendacion.conectar_libros("ISBN-011", "ISBN-012")  # Harry Potter 1 -> 2
        self.recomendacion.conectar_libros("ISBN-013", "ISBN-014")  # Clean Code -> Pragmatic
        
        # USUARIOS DE EJEMPLO
        usuarios_data = [
            ("U001", "Jessica Jiménez", "JessJim@gmail.com"),
            ("U002", "Daniela Jiménez", "daniJim@gmail.com"),
            ("U003", "Eduard Mosqueda", "EduMos@gmail.com"),
            ("U004", "María De Franceschi", "MarDFran@gmail.com"),
            ("U005", "Cleyrton Bermúdez", "CleyBer@gmail.com"),
        ]
        
        for uid, nombre, email in usuarios_data:
            self.usuarios[uid] = Usuario(uid, nombre, email)
        
        # ====== REGISTRAR EN EL HISTORIAL ======
        self.historial.agregar_accion("Datos de ejemplo cargados correctamente")
        
        print(f" {len(libros_data)} libros cargados")
        print(f" {len(usuarios_data)} usuarios registrados")
    
    def _limpiar_pantalla(self):
        """Limpia la pantalla según el sistema operativo."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _mostrar_menu(self):
        """Muestra el menú principal del sistema."""
        print("\n" + "-"*20)
        print("   BIBLIOTECA VIRTUAL KAPPA - MENÚ PRINCIPAL")
        print("-"*20)
        print("\n GESTIÓN DE LIBROS:")
        print("  1.  Mostrar catálogo completo")
        print("  2.  Agregar nuevo libro")
        print("  3.  Buscar libro por título")
        print("  4.  Buscar libro por autor")
        print("  5.  Buscar libro por ISBN")
        print("  6.  Eliminar libro del catálogo")
        print("  7.  Ver estadísticas del catálogo")
        print("\n GESTIÓN DE USUARIOS:")
        print("  8.  Mostrar usuarios registrados")
        print("  9.  Registrar nuevo usuario")
        print(" 10.  Tomar libro prestado")
        print(" 11.  Devolver libro")
        print("\n RESERVAS Y HISTORIAL:")
        print(" 12.  Crear reserva de libro")
        print(" 13.  Atender siguiente reserva")
        print(" 14.  Mostrar reservas pendientes")
        print(" 15.  Ver historial de acciones")
        print(" 16.  Deshacer última acción")
        print("\n BÚSQUEDA AVANZADA (Índices):")
        print(" 17.  Buscar por ISBN (O(log n) con AVL)")
        print(" 18.  Buscar por título exacto (O(log n) con AVL)")
        print(" 19.  Buscar por autor (O(log n) con AVL)")
        print("\n RECOMENDACIONES Y CACHE:")
        print(" 20.  Recomendar libros similares (BFS)")
        print(" 21.  Ver libros en cache (O(1))")
        print(" 22.  Ver estadísticas del cache")
        print("\n INFORMACIÓN DEL SISTEMA:")
        print(" 23.  Mostrar información de estructuras")
        print("\n 0.  Salir del sistema")
        print("-"*60)
    
    def _pausa(self):
        """Pausa la ejecución hasta que el usuario presione Enter."""
        input("\nPresiona Enter para continuar...")
    
    # ========== FUNCIONES DEL MENÚ ==========
    
    # ---- Gestión de Libros ----
    
    def mostrar_catalogo(self):
        """Muestra todos los libros del catálogo."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("   CATÁLOGO DE LIBROS")
        print("-"*20)
        
        if self.catalogo.esta_vacio():
            print("\n El catálogo está vacío")
        else:
            print(f"\nTotal de libros: {self.catalogo.cantidad_libros()}\n")
            for i, libro in enumerate(self.catalogo.recorrer_catalogo(), 1):
                estado = " Disponible" if libro.disponible else " Prestado"
                print(f"{i:3}. {libro.isbn} | {libro.titulo[:50]}")
                print(f"      {libro.autor} |  {libro.anio} | {estado}")
        
        self._pausa()
    
    def agregar_libro(self):
        """Agrega un nuevo libro al catálogo."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("  AGREGAR NUEVO LIBRO")
        print("-"*20)
        
        try:
            isbn = input("\nISBN del libro: ").strip()
            if not isbn:
                print(" El ISBN es obligatorio")
                self._pausa()
                return
            
            # Verificar si ya existe
            if self.catalogo.buscar_por_isbn(isbn):
                print(f" Ya existe un libro con ISBN: {isbn}")
                self._pausa()
                return
            
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            anio_str = input("Año de publicación: ").strip()
            
            if not titulo or not autor:
                print(" Título y autor son obligatorios")
                self._pausa()
                return
            
            try:
                anio = int(anio_str) if anio_str else 2000
            except ValueError:
                print(" Año inválido, se usará 2000")
                anio = 2000
            
            libro = Libro(isbn, titulo, autor, anio)
            self.catalogo.agregar_libro_inicio(libro)
            self.busqueda.agregar_libro(libro)
            self.indice.agregar_libro(libro)
            self.recomendacion.agregar_libro(libro)
            
            self.historial.agregar_accion(f"Libro agregado: {titulo}")
            print(f"\n Libro agregado correctamente: {titulo}")
            
        except Exception as e:
            print(f" Error al agregar libro: {e}")
        
        self._pausa()
    
    def buscar_por_titulo(self):
        """Busca libros por título (búsqueda parcial)."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print(" BUSCAR LIBRO POR TÍTULO")
        print("-"*20)
        
        titulo = input("\nIngresa el título (o parte): ").strip()
        if not titulo:
            print(" Debes ingresar un título")
            self._pausa()
            return
        
        resultados = self.catalogo.buscar_por_titulo(titulo)
        
        if not resultados:
            print(f"\n No se encontraron libros con '{titulo}'")
        else:
            print(f"\n {len(resultados)} resultado(s):\n")
            for libro in resultados:
                estado = " Disponible" if libro.disponible else " Prestado"
                print(f"    {libro.titulo}")
                print(f"       {libro.autor} | {libro.isbn} | {estado}")
        
        self._pausa()
    
    def buscar_por_autor(self):
        """Busca libros por autor (coincidencia exacta)."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print(" BUSCAR LIBRO POR AUTOR")
        print("-"*20)
        
        autor = input("\nIngresa el nombre del autor: ").strip()
        if not autor:
            print(" Debes ingresar un autor")
            self._pausa()
            return
        
        resultados = self.catalogo.buscar_por_autor(autor)
        
        if not resultados:
            print(f"\n No se encontraron libros de '{autor}'")
        else:
            print(f"\n {len(resultados)} resultado(s):\n")
            for libro in resultados:
                estado = " Disponible" if libro.disponible else " Prestado"
                print(f"    {libro.titulo} ({libro.anio}) | {estado}")
        
        self._pausa()
    
    def buscar_por_isbn(self):
        """Busca un libro por su ISBN."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print(" BUSCAR LIBRO POR ISBN")
        print("-"*20)
        
        isbn = input("\nIngresa el ISBN: ").strip()
        if not isbn:
            print(" Debes ingresar un ISBN")
            self._pausa()
            return
        
        # Buscar en catálogo (lista enlazada)
        libro = self.catalogo.buscar_por_isbn(isbn)
        
        if not libro:
            print(f"\n No se encontró libro con ISBN: {isbn}")
        else:
            estado = " Disponible" if libro.disponible else " Prestado"
            print(f"\n Libro encontrado:")
            print(f"    {libro.titulo}")
            print(f"    {libro.autor}")
            print(f"    {libro.anio}")
            print(f"   -{estado}")
        
        self._pausa()
    
    def eliminar_libro(self):
        """Elimina un libro del catálogo."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("   ELIMINAR LIBRO")
        print("-"*20)
        
        isbn = input("\nIngresa el ISBN del libro a eliminar: ").strip()
        if not isbn:
            print(" Debes ingresar un ISBN")
            self._pausa()
            return
        
        libro = self.catalogo.buscar_por_isbn(isbn)
        if not libro:
            print(f" No se encontró libro con ISBN: {isbn}")
            self._pausa()
            return
        
        print(f"\n Libro encontrado: {libro.titulo}")
        confirmar = input("¿Confirmar eliminación? (s/n): ").strip().lower()
        
        if confirmar == 's':
            self.catalogo.eliminar_libro(isbn)
            self.busqueda.eliminar_libro(isbn)
            self.indice.eliminar_libro(isbn)
            self.historial.agregar_accion(f"Libro eliminado: {libro.titulo}")
            print(f"\n Libro eliminado correctamente: {libro.titulo}")
        else:
            print("\n Operación cancelada")
        
        self._pausa()
    
    def ver_estadisticas_catalogo(self):
        """Muestra estadísticas del catálogo."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("   ESTADÍSTICAS DEL CATÁLOGO")
        print("-"*20)
        
        total = self.catalogo.cantidad_libros()
        disponibles = sum(1 for l in self.catalogo.recorrer_catalogo() if l.disponible)
        prestados = total - disponibles
        
        print(f"\n Total de libros: {total}")
        print(f" Disponibles: {disponibles}")
        print(f" Prestados: {prestados}")
        
        # Autores más comunes
        autores = {}
        for libro in self.catalogo.recorrer_catalogo():
            autores[libro.autor] = autores.get(libro.autor, 0) + 1
        
        if autores:
            print("\n Autores con más libros:")
            for autor, cantidad in sorted(autores.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"   {autor}: {cantidad} libro(s)")
        
        self._pausa()
    
    # ---- Gestión de Usuarios ----
    
    def mostrar_usuarios(self):
        """Muestra todos los usuarios registrados."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("   USUARIOS REGISTRADOS")
        print("-"*20)
        
        if not self.usuarios:
            print("\n No hay usuarios registrados")
        else:
            print(f"\nTotal: {len(self.usuarios)} usuarios\n")
            for uid, usuario in self.usuarios.items():
                print(f"    {usuario.nombre} ({uid})")
                print(f"      📧 {usuario.email}")
                prestados = len(usuario.libros_prestados)
                print(f"       {prestados} libro(s) prestado(s)")
                if prestados > 0:
                    for libro in usuario.libros_prestados:
                        print(f"         - {libro.titulo}")
        
        self._pausa()
    
    def registrar_usuario(self):
        """Registra un nuevo usuario."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("   REGISTRAR NUEVO USUARIO")
        print("-"*20)
        
        try:
            uid = input("\nID del usuario: ").strip()
            if not uid:
                print(" El ID es obligatorio")
                self._pausa()
                return
            
            if uid in self.usuarios:
                print(f" Ya existe un usuario con ID: {uid}")
                self._pausa()
                return
            
            nombre = input("Nombre completo: ").strip()
            email = input("Email: ").strip()
            
            if not nombre:
                print(" El nombre es obligatorio")
                self._pausa()
                return
            
            usuario = Usuario(uid, nombre, email if email else "sin-email@ejemplo.com")
            self.usuarios[uid] = usuario
            
            self.historial.agregar_accion(f"Usuario registrado: {nombre}")
            print(f"\n Usuario registrado correctamente: {nombre}")
            
        except Exception as e:
            print(f" Error al registrar usuario: {e}")
        
        self._pausa()
    
    def tomar_prestado(self):
        """Toma un libro prestado."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("   TOMAR LIBRO PRESTADO")
        print("-"*20)
        
        # Seleccionar usuario
        if not self.usuarios:
            print("\n No hay usuarios registrados")
            self._pausa()
            return
        
        print("\n Usuarios disponibles:")
        for uid, usuario in self.usuarios.items():
            print(f"   {uid}: {usuario.nombre}")
        
        uid = input("\nIngresa el ID del usuario: ").strip()
        usuario = self.usuarios.get(uid)
        
        if not usuario:
            print(f" No se encontró usuario con ID: {uid}")
            self._pausa()
            return
        
        # Seleccionar libro
        isbn = input("Ingresa el ISBN del libro: ").strip()
        libro = self.catalogo.buscar_por_isbn(isbn)
        
        if not libro:
            print(f" No se encontró libro con ISBN: {isbn}")
            self._pausa()
            return
        
        if not libro.disponible:
            print(f" El libro '{libro.titulo}' no está disponible")
            self._pausa()
            return
        
        # Realizar préstamo
        if usuario.tomar_prestado(libro):
            self.historial.agregar_accion(f"Libro prestado: {libro.titulo} a {usuario.nombre}")
            print(f"\n Préstamo exitoso!")
            print(f"    {libro.titulo} prestado a {usuario.nombre}")
        else:
            print(f" Error al tomar el préstamo")
        
        self._pausa()
    
    def devolver_libro(self):
        """Devuelve un libro prestado."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print(" DEVOLVER LIBRO")
        print("-"*20)
        
        if not self.usuarios:
            print("\n No hay usuarios registrados")
            self._pausa()
            return
        
        print("\n Usuarios disponibles:")
        for uid, usuario in self.usuarios.items():
            prestados = len(usuario.libros_prestados)
            if prestados > 0:
                print(f"   {uid}: {usuario.nombre} ({prestados} libros prestados)")
        
        uid = input("\nIngresa el ID del usuario: ").strip()
        usuario = self.usuarios.get(uid)
        
        if not usuario:
            print(f" No se encontró usuario con ID: {uid}")
            self._pausa()
            return
        
        if not usuario.libros_prestados:
            print(f"\n {usuario.nombre} no tiene libros prestados")
            self._pausa()
            return
        
        print(f"\n Libros prestados por {usuario.nombre}:")
        for i, libro in enumerate(usuario.libros_prestados, 1):
            print(f"   {i}. {libro.titulo} ({libro.isbn})")
        
        try:
            opcion = int(input("\nSelecciona el número del libro a devolver: "))
            if 1 <= opcion <= len(usuario.libros_prestados):
                libro = usuario.libros_prestados[opcion - 1]
                if usuario.devolver_libro(libro):
                    self.historial.agregar_accion(f"Libro devuelto: {libro.titulo} por {usuario.nombre}")
                    print(f"\n Libro devuelto correctamente: {libro.titulo}")
                else:
                    print(" Error al devolver el libro")
            else:
                print(" Opción inválida")
        except ValueError:
            print(" Debes ingresar un número válido")
        
        self._pausa()
    
    # ---- Reservas y Historial ----
    
    def crear_reserva(self):
        """Crea una reserva de libro."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("   CREAR RESERVA")
        print("-"*20)
        
        if not self.usuarios:
            print("\n No hay usuarios registrados")
            self._pausa()
            return
        
        print("\n Usuarios disponibles:")
        for uid, usuario in self.usuarios.items():
            print(f"   {uid}: {usuario.nombre}")
        
        uid = input("\nIngresa el ID del usuario: ").strip()
        usuario = self.usuarios.get(uid)
        
        if not usuario:
            print(f" No se encontró usuario con ID: {uid}")
            self._pausa()
            return
        
        isbn = input("Ingresa el ISBN del libro a reservar: ").strip()
        libro = self.catalogo.buscar_por_isbn(isbn)
        
        if not libro:
            print(f" No se encontró libro con ISBN: {isbn}")
            self._pausa()
            return
        
        reserva_id = self.reservas.crear_reserva(usuario, libro)
        self.historial.agregar_accion(f"Reserva creada: {libro.titulo} por {usuario.nombre}")
        print(f"\n Reserva creada: {reserva_id}")
        
        self._pausa()
    
    def atender_reserva(self):
        """Atiende la siguiente reserva en cola."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("   ATENDER RESERVA")
        print("-"*20)
        
        if self.reservas.esta_vacio():
            print("\n No hay reservas pendientes")
        else:
            print("\n Reservas pendientes:")
            self.reservas.mostrar_reservas()
            
            reserva_id = self.reservas.atender_reserva()
            if reserva_id:
                self.historial.agregar_accion(f"Reserva atendida: {reserva_id}")
                print(f"\n Reserva atendida exitosamente: {reserva_id}")
            else:
                print("\n Error al atender la reserva")
        
        self._pausa()
    
    def mostrar_reservas(self):
        """Muestra todas las reservas pendientes."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("  RESERVAS PENDIENTES")
        print("-"*20)
        
        self.reservas.mostrar_reservas()
        
        self._pausa()
    
    def ver_historial(self):
        """Muestra el historial de acciones."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("  HISTORIAL DE ACCIONES")
        print("-"*20)
        
        self.historial.mostrar_historial()
        
        self._pausa()
    
    def deshacer_accion(self):
        """Deshace la última acción."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("  DESHACER ÚLTIMA ACCIÓN")
        print("-"*20)
        
        if self.historial.esta_vacio():
            print("\n No hay acciones para deshacer")
        else:
            accion = self.historial.deshacer()
            print(f"\n Acción deshecha: {accion}")
        
        self._pausa()
    
    # ---- Búsqueda Avanzada (Índices) ----
    
    def buscar_avl_isbn(self):
        """Busca por ISBN usando AVL (O(log n) garantizado)."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print(" BÚSQUEDA AVANZADA POR ISBN (O(log n))")
        print("-"*20)
        
        isbn = input("\nIngresa el ISBN: ").strip()
        if not isbn:
            print(" Debes ingresar un ISBN")
            self._pausa()
            return
        
        libro = self.busqueda.buscar_por_isbn(isbn)
        
        if not libro:
            print(f"\n No se encontró libro con ISBN: {isbn}")
        else:
            print(f"\n Libro encontrado (búsqueda O(log n)):")
            print(f"    {libro.titulo}")
            print(f"    {libro.autor}")
            print(f"    {libro.anio}")
            estado = " Disponible" if libro.disponible else " Prestado"
            print(f"   -{estado}")
        
        self._pausa()
    
    def buscar_avl_titulo(self):
        """Busca por título exacto usando AVL (O(log n) garantizado)."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print(" BÚSQUEDA AVANZADA POR TÍTULO EXACTO (O(log n))")
        print("-"*20)
        
        titulo = input("\nIngresa el título exacto: ").strip()
        if not titulo:
            print(" Debes ingresar un título")
            self._pausa()
            return
        
        libro = self.busqueda.buscar_por_titulo(titulo)
        
        if not libro:
            print(f"\n No se encontró libro con título: '{titulo}'")
        else:
            print(f"\n Libro encontrado (búsqueda O(log n)):")
            print(f"    {libro.titulo}")
            print(f"    {libro.autor}")
            print(f"    {libro.anio}")
            print(f"   -ISBN: {libro.isbn}")
        
        self._pausa()
    
    def buscar_avl_autor(self):
        """Busca por autor usando AVL (O(log n) garantizado)."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print(" BÚSQUEDA AVANZADA POR AUTOR (O(log n))")
        print("-"*20)
        
        autor = input("\nIngresa el nombre del autor: ").strip()
        if not autor:
            print(" Debes ingresar un autor")
            self._pausa()
            return
        
        resultados = self.busqueda.buscar_por_autor(autor)
        
        if not resultados:
            print(f"\n No se encontraron libros de '{autor}'")
        else:
            print(f"\n {len(resultados)} libro(s) encontrado(s) (búsqueda O(log n)):")
            for libro in resultados:
                estado = " Disponible" if libro.disponible else " Prestado"
                print(f"    {libro.titulo} ({libro.anio}) | {estado}")
        
        self._pausa()
    
    # ---- Recomendaciones y Cache ----
    
    def recomendar_libros(self):
        """Recomienda libros similares usando BFS."""
        self._limpiar_pantalla()
        print("\n")
        print("  RECOMENDACIONES DE LIBROS (BFS)")
        print("\n")
        
        isbn = input("\nIngresa el ISBN del libro de referencia: ").strip()
        if not isbn:
            print(" Debes ingresar un ISBN")
            self._pausa()
            return
        
        # Verificar que el libro existe
        libro_ref = self.catalogo.buscar_por_isbn(isbn)
        if not libro_ref:
            print(f" No se encontró libro con ISBN: {isbn}")
            self._pausa()
            return
        
        print(f"\n Libro de referencia: {libro_ref.titulo} ({libro_ref.autor})")
        
        try:
            profundidad = int(input("\nProfundidad de búsqueda (1-3, recomendado 2): ").strip() or "2")
            profundidad = max(1, min(3, profundidad))
        except ValueError:
            profundidad = 2
        
        recomendados = self.recomendacion.recomendar_bfs(isbn, profundidad)
        
        if not recomendados:
            print(f"\n No se encontraron recomendaciones para '{libro_ref.titulo}'")
        else:
            print(f"\n {len(recomendados)} recomendación(es) (BFS profundidad {profundidad}):")
            for libro in recomendados:
                estado = " Disponible" if libro.disponible else " Prestado"
                print(f"    {libro.titulo} ({libro.autor}) | {estado}")
        
        self._pausa()
    
    def ver_cache(self):
        """Muestra los libros almacenados en cache."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("  ⚡ CACHE DE LIBROS (O(1))")
        print("-"*20)
        
        libros_cache = self.cache.listar_todos()
        
        if not libros_cache:
            print("\n El cache está vacío")
        else:
            print(f"\n {len(libros_cache)} libro(s) en cache:\n")
            for libro in libros_cache:
                estado = "Disponible" if libro.disponible else " Prestado"
                print(f"    {libro.titulo}")
                print(f"      {libro.isbn} | {estado}")
        
        self._pausa()
    
    def ver_estadisticas_cache(self):
        """Muestra estadísticas del cache."""
        self._limpiar_pantalla()
        print("\n" + "-"*20)
        print("   ESTADÍSTICAS DEL CACHE")
        print("-"*20)
        
        stats = self.cache.estadisticas()
        
        print(f"\n Estadísticas de uso del cache:")
        print(f"   Aciertos: {stats['aciertos']}")
        print(f"   Fallos: {stats['fallos']}")
        print(f"   Total consultas: {stats['total']}")
        print(f"   Tasa de acierto: {stats['tasa_acierto']}")
        print(f"   Tamaño del cache: {stats['tamano_cache']}")
        
        self._pausa()
    
    # ---- Información del Sistema ----
   
    def mostrar_info_estructuras(self):
        """Muestra información detallada de cada estructura."""
        self._limpiar_pantalla()
        print("\n")
        print("INFORMACIÓN DE ESTRUCTURAS")
        print("\n")
        
        print("""
-PILA (Stack) - LIFO
   Uso: Historial de acciones del usuario
   Complejidad: O(1) para todas las operaciones
   Limitación: Solo acceso a la cima

-COLA (Queue) - FIFO
   Uso: Gestión de reservas de libros
   Complejidad: O(1) para enqueue/dequeue
   Limitación: Solo acceso al frente

-LISTA DOBLEMENTE ENLAZADA
   Uso: Catálogo de libros
   Complejidad: Inserción O(1), Búsqueda O(n)
   Limitación: Búsqueda secuencial

-ÁRBOL BINARIO DE BÚSQUEDA (ABB)
   Uso: Búsqueda rápida de libros
   Complejidad: O(log n) promedio, O(n) peor caso
   Limitación: Puede degenerar con datos ordenados

-ÁRBOL AVL
   Uso: Búsqueda con rendimiento garantizado
   Complejidad: O(log n) siempre
   Limitación: Overhead por almacenamiento de alturas

-ÁRBOL 2-3
   Uso: Índice de libros por ISBN
   Complejidad: O(log n) siempre
   Limitación: No implementa eliminación

-GRAFO
   Uso: Recomendaciones de libros
   Complejidad: BFS/DFS O(V+E)
   Limitación: No ponderado, no dirigido

-TABLA HASH
   Uso: Cache de libros (acceso instantáneo)
   Complejidad: O(1) promedio
   Limitación: Orden no garantizado""")
        
        self._pausa()
    
    # ========== EJECUCIÓN PRINCIPAL ==========
    
    def ejecutar(self):
        """Ejecuta el bucle principal del menú interactivo."""
        while True:
            self._limpiar_pantalla()
            self._mostrar_menu()
            
            try:
                opcion = input("\nSelecciona una opción: ").strip()
                
                if opcion == '0':
                    print("\n¡Gracias por usar la Biblioteca Virtual Kappa!")
                    print("   Hasta luego!")
                    break
                
                # Mapeo de opciones a funciones
                opciones = {
                    '1': self.mostrar_catalogo,
                    '2': self.agregar_libro,
                    '3': self.buscar_por_titulo,
                    '4': self.buscar_por_autor,
                    '5': self.buscar_por_isbn,
                    '6': self.eliminar_libro,
                    '7': self.ver_estadisticas_catalogo,
                    '8': self.mostrar_usuarios,
                    '9': self.registrar_usuario,
                    '10': self.tomar_prestado,
                    '11': self.devolver_libro,
                    '12': self.crear_reserva,
                    '13': self.atender_reserva,
                    '14': self.mostrar_reservas,
                    '15': self.ver_historial,
                    '16': self.deshacer_accion,
                    '17': self.buscar_avl_isbn,
                    '18': self.buscar_avl_titulo,
                    '19': self.buscar_avl_autor,
                    '20': self.recomendar_libros,
                    '21': self.ver_cache,
                    '22': self.ver_estadisticas_cache,
                    '23': self.mostrar_info_estructuras,
                }
                
                if opcion in opciones:
                    opciones[opcion]()
                else:
                    print("\n Opción no válida. Intenta de nuevo.")
                    self._pausa()
                    
            except KeyboardInterrupt:
                print("\n\n¡Hasta luego!")
                break
            except Exception as e:
                print(f"\n Error inesperado: {e}")
                self._pausa()


# ========== PUNTO DE ENTRADA ==========

if __name__ == "__main__":
    # Asegurar que el directorio src está en el path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    # Crear y ejecutar la biblioteca
    biblioteca = BibliotecaVirtual()
    biblioteca.ejecutar()