"""
Sprint 2 - Pilas y Colas
Demostración de las estructuras implementadas en el contexto de la biblioteca virtual.
"""

from src.structures.pila import Pila
from src.structures.cola import Cola
from src.models.libro import Libro
from src.models.usuario import Usuario
from src.services.historial_service import HistorialService
from src.services.reserva_service import ReservaService


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


def main():
    """Función principal que ejecuta todas las demostraciones"""
    print("="*50)
    print("SPRINT 2 - PILAS Y COLAS")
    print("Biblioteca Virtual - Demostración")
    print("="*50)
    
    demostrar_pila()
    demostrar_cola()
    demostrar_servicios()
    
    print("\n" + "="*50)
    print("FIN DE DEMOSTRACIÓN")
    print("="*50)


if __name__ == "__main__":
    main()