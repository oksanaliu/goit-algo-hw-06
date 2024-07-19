import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G_ecosystem = nx.Graph()

# Додавання вершин організми
organisms = ['PlantA', 'PlantB', 'Herbivore1', 'Herbivore2', 'Carnivore1', 'Carnivore2']
G_ecosystem.add_nodes_from(organisms)

# Додавання ребер взаємодії між організмами
interactions = [('PlantA', 'Herbivore1'), ('PlantA', 'Herbivore2'),
                ('PlantB', 'Herbivore1'), ('Herbivore1', 'Carnivore1'),
                ('Herbivore2', 'Carnivore1'), ('Carnivore1', 'Carnivore2')]
G_ecosystem.add_edges_from(interactions)

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G_ecosystem, seed=42)  
nx.draw(G_ecosystem, pos, with_labels=True, node_size=2000, node_color='lightyellow', font_size=12, font_weight='bold')
plt.title('Ecological Network Graph')
plt.show()

# DFS та BFS функції
def dfs(graph, start, path=[]):
    path = path + [start]
    for node in graph.neighbors(start):
        if node not in path:
            path = dfs(graph, node, path)
    return path

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = list(graph.neighbors(node))
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

# Використання алгоритмів DFS та BFS для знаходження шляхів
start_node = 'PlantA'
dfs_path = dfs(G_ecosystem, start_node)
bfs_path = bfs(G_ecosystem, start_node)

print(f"DFS path starting from {start_node}: {dfs_path}")
print(f"BFS path starting from {start_node}: {bfs_path}")

# Аналіз основних характеристик
num_nodes_ecosystem = G_ecosystem.number_of_nodes()
num_edges_ecosystem = G_ecosystem.number_of_edges()
degrees_ecosystem = dict(G_ecosystem.degree())

print(f"Number of nodes: {num_nodes_ecosystem}")
print(f"Number of edges: {num_edges_ecosystem}")
print(f"Degrees of nodes: {degrees_ecosystem}")