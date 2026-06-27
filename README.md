# Kappa-BibliotecaVirtual
Proyecto de estructura de datos sección 01, Bliblioteca Virtual
La Biblioteca Virtual permitirá gestionar libros digitales, usuarios, préstamos, devoluciones y búsquedas de información. El sistema facilitará la administración del catálogo y el acceso eficiente a los recursos bibliográficos.

# Integrantes:
  Jessica Jiménez
  C.I: 27.977.142

  Daniela Jiménez
  C.I: 26.833.900

  Eduard Mosqueda
  C.I: 27.181.134

  María De Franceschi
  C.I: 29.516.285

  Cleyrton Bermúdez
  C.I: 32013719

- **Lenguaje:** Python 3.8+
- **Testing:** unittest (biblioteca estándar)
- **Control de versiones:** Git
- **Repositorio:** GitHub

## Sprint 3 - Listas Enlazadas (agrega información/descripción sobre el sprint 3 a lo anterior)
### Estructuras Implementadas (/structures)
- **Pila (Stack):** Utilizada para historial de acciones del usuario
  - Operaciones: push, pop, peek, is_empty, size
  - Complejidad: O(1) para todas las operaciones básicas
  
- **Cola (Queue):** Utilizada para gestión de reservas
  - Operaciones: enqueue, dequeue, front, is_empty, size
  - Complejidad: O(1) para todas las operaciones básicas

- **Lista Enlazada:**
  - Operaciones: inserción, eliminación y recorrido de elementos de la lista

### Servicios (/services)
  HistorialService: Maneja el historial de acciones (Pila)
  ReservaService: Gestiona reservas de libros (Cola)
  CatalogoService: Maneja la gestión de catálogos (Listas enlazadas)


### Modelos (/models)
  Añadido libro.py y usuario.py para la representación de modelos de biblioteca virtual
  según lo estipulado en el plan de implementación del proyecto.