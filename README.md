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
- **Control de versiones:** Git
- **Repositorio:** GitHub

### Sprint 2 - Pilas y Colas
- **Pila (Stack):** Historial de acciones del usuario (LIFO)
- **Cola (Queue):** Reservas de libros (FIFO)

### Sprint 3 - Listas Enlazadas
- **Lista Doblemente Enlazada:** Catálogo de libros
- Inserción, eliminación, búsqueda y recorridos

### Sprint 4 - Árboles Binarios y AVL
- **ABB:** Búsqueda rápida (O(log n) promedio)
- **AVL:** Búsqueda rápida garantizada (O(log n) siempre)

### Sprint 5 - Árboles 2-3 y B
- **Árbol 2-3:** Índice balanceado para búsquedas eficientes
- **Árbol B (opcional):** Índice para grandes volúmenes de datos

| Estructura | Búsqueda | Inserción | Uso en el Proyecto |
|------------|----------|-----------|-------------------|
| Pila | O(1) | O(1) | Historial de acciones |
| Cola | O(1) | O(1) | Reservas de libros |
| Lista Enlazada | O(n) | O(1) | Catálogo general |
| ABB | O(log n)* | O(log n)* | Búsqueda simple |
| AVL | O(log n) | O(log n) | Búsqueda rápida |
| Árbol 2-3 | O(log n) | O(log n) | Índice eficiente |