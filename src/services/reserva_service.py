# src/services/reserva_service.py
"""
Servicio: Reservas
Utiliza la estructura Cola para gestionar reservas en orden de llegada
"""

from structures.cola import Cola
from models.libro import Libro
from models.usuario import Usuario
from typing import Optional, Dict, List

class ReservaService:
    """
    Servicio que maneja las reservas de libros.
    Utiliza una Cola (FIFO) para atender las solicitudes en orden de llegada.
    """
    
    def __init__(self):
        """Inicializa el servicio con una cola vacía"""
        self.reservas = Cola()
        self._reservas_info = {}  # Almacena información extra de cada reserva
    
    def crear_reserva(self, usuario: Usuario, libro: Libro) -> str:
        """
        Crea una nueva reserva para un usuario y libro.
        
        Args:
            usuario: Usuario que hace la reserva
            libro: Libro a reservar
            
        Returns:
            ID de la reserva creada
            
        Limitación: No valida si el libro ya está reservado por el mismo usuario.
        """
        # Generar ID único para la reserva
        import time
        reserva_id = f"RES-{int(time.time())}-{usuario.id_usuario}"
        
        # Agregar a la cola
        self.reservas.enqueue(reserva_id)
        
        # Guardar información adicional
        self._reservas_info[reserva_id] = {
            'usuario': usuario.nombre,
            'libro': libro.titulo,
            'isbn': libro.isbn
        }
        
        print(f"✅ Reserva creada: {reserva_id} - {usuario.nombre} reservó {libro.titulo}")
        return reserva_id
    
    def atender_reserva(self) -> Optional[str]:
        """
        Atiende la siguiente reserva en la cola (FIFO).
        
        Returns:
            ID de la reserva atendida, None si no hay reservas
            
        Limitación: Elimina la reserva de la cola. Si se necesita persistencia,
        se debería almacenar en una base de datos.
        """
        if self.reservas.is_empty():
            print("❌ No hay reservas pendientes")
            return None
        
        reserva_id = self.reservas.dequeue()
        info = self._reservas_info.pop(reserva_id, {})
        
        print(f"✅ Atendiendo reserva: {reserva_id}")
        if info:
            print(f"   Usuario: {info.get('usuario')}, Libro: {info.get('libro')}")
        
        return reserva_id
    
    def ver_siguiente_reserva(self) -> Optional[str]:
        """
        Consulta la siguiente reserva sin eliminarla.
        
        Returns:
            ID de la siguiente reserva, None si no hay
            
        Limitación: Solo muestra el ID, no la información completa.
        """
        if self.reservas.is_empty():
            return None
        return self.reservas.front()
    
    def mostrar_reservas(self) -> None:
        """
        Muestra todas las reservas en la cola de manera formateada.
        """
        lista_reservas = self.reservas.to_list()
        
        print("=== RESERVAS EN COLA (orden de llegada) ===")
        if not lista_reservas:
            print("No hay reservas pendientes")
        else:
            for i, reserva_id in enumerate(lista_reservas, 1):
                info = self._reservas_info.get(reserva_id, {})
                print(f"{i}. {reserva_id} - {info.get('usuario', 'N/A')}: {info.get('libro', 'N/A')}")
    
    def cantidad_reservas(self) -> int:
        """Retorna el número de reservas pendientes"""
        return self.reservas.size()
    
    def esta_vacio(self) -> bool:
        """Verifica si hay reservas pendientes"""
        return self.reservas.is_empty()