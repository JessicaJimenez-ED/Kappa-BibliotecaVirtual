# src/services/historial_service.py
"""
Servicio: Historial
Utiliza la estructura Pila para gestionar el historial de acciones
"""

from src.structures.pila import Pila
from typing import List

class HistorialService:
    """
    Servicio que maneja el historial de acciones de un usuario.
    Utiliza una Pila (LIFO) para mantener las últimas acciones en la cima.
    """
    
    MAX_HISTORIAL = 20  # Límite de acciones en el historial
    
    def __init__(self):
        """Inicializa un nuevo historial vacío"""
        self.historial = Pila()
    
    def agregar_accion(self, descripcion: str) -> None:
        """
        Agrega una acción al historial.
        
        Args:
            descripcion: Descripción de la acción realizada
            
        Limitación: Si el historial supera MAX_HISTORIAL, se elimina la acción
        más antigua (fondo de la pila).
        """
        self.historial.push(descripcion)
        
        # Si excede el límite, necesitamos eliminar el fondo
        # Limitación: No podemos acceder al fondo directamente
        # Solución: Usar una pila auxiliar o implementar pop_fondo()
        if self.historial.size() > self.MAX_HISTORIAL:
            self._limitar_historial()
    
    def _limitar_historial(self) -> None:
        """
        Método privado para limitar el tamaño del historial.
        Almacena los últimos MAX_HISTORIAL elementos.
        
        Limitación: Requiere una estructura auxiliar, lo que aumenta complejidad.
        """
        pila_aux = Pila()
        
        # Mover todos los elementos a la pila auxiliar
        while not self.historial.is_empty():
            pila_aux.push(self.historial.pop())
        
        # Sacar el elemento más antiguo (fondo original)
        pila_aux.pop()
        
        # Restaurar los elementos a la pila original
        while not pila_aux.is_empty():
            self.historial.push(pila_aux.pop())
    
    def ver_ultima_accion(self) -> str:
        """
        Obtiene la última acción sin eliminarla.
        
        Returns:
            Descripción de la última acción
        """
        return self.historial.peek()
    
    def deshacer(self) -> str:
        """
        Deshace la última acción (la elimina del historial).
        
        Returns:
            Descripción de la acción deshecha
        """
        return self.historial.pop()
    
    def obtener_historial(self) -> List[str]:
        """
        Obtiene todo el historial ordenado de más reciente a más antiguo.
        
        Returns:
            Lista de acciones en orden inverso (reciente a antiguo)
        """
        return self.historial.to_list()[::-1]  # Invertir para mostrar más reciente primero
    
    def mostrar_historial(self) -> None:
        """
        Muestra el historial en consola de manera formateada.
        """
        acciones = self.obtener_historial()
        print("=== HISTORIAL DE ACCIONES ===")
        if not acciones:
            print("No hay acciones en el historial")
        else:
            for i, accion in enumerate(acciones, 1):
                print(f"{i}. {accion}")
    
    def esta_vacio(self) -> bool:
        """Verifica si el historial está vacío"""
        return self.historial.is_empty()
    
    def cantidad_acciones(self) -> int:
        """Retorna el número de acciones en el historial"""
        return self.historial.size()