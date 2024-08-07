# Аналіз алгоритмів DFS та BFS на прикладі екологічної мережі

## Опис графа

Граф представляє екологічну мережу, де вершини представляють різні організми, а ребра - взаємодії між ними.

## Алгоритми

### DFS (Depth-First Search)

DFS починає з початкової вершини та досліджує якнайглибше по кожній гілці перед поверненням.

### BFS (Breadth-First Search)

BFS починає з початкової вершини та досліджує всі її сусіди перед переходом до наступного рівня.

## Результати

### Шлях DFS
['PlantA', 'Herbivore1', 'Carnivore1', 'Carnivore2', 'Herbivore2', 'PlantB']

### Шлях BFS
['PlantA', 'Herbivore1', 'Herbivore2', 'Carnivore1', 'Carnivore2', 'PlantB']

## Порівняння

- DFS: Шлях може бути довшим і більш звивистим, оскільки алгоритм спочатку досліджує найглибші гілки.
- BFS: Шлях більш рівномірний і менш глибокий, оскільки алгоритм досліджує всі вершини на одному рівні перед переходом до наступного.

## Висновок

Різниця у шляхах обумовлена різними підходами до дослідження графа: DFS глибоко досліджує кожну гілку перед поверненням, тоді як BFS рівномірно досліджує всі сусіди на кожному рівні.