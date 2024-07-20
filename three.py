import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графа
G_ecosystem = nx.Graph()

# Додавання вершин організми
organisms = ['PlantA', 'PlantB', 'Herbivore1', 'Herbivore2', 'Carnivore1', 'Carnivore2']
G_ecosystem.add_nodes_from(organisms)

# Додавання ребер взаємодії між організмами з вагами
interactions = [
    ('PlantA', 'Herbivore1', 1.0), 
    ('PlantA', 'Herbivore2', 2.0),
    ('PlantB', 'Herbivore1', 1.5), 
    ('Herbivore1', 'Carnivore1', 2.5),
    ('Herbivore2', 'Carnivore1', 2.0), 
    ('Carnivore1', 'Carnivore2', 1.0)
]
G_ecosystem.add_weighted_edges_from(interactions)

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G_ecosystem, seed=42)  
nx.draw(G_ecosystem, pos, with_labels=True, node_size=2000, node_color='lightyellow', font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G_ecosystem, 'weight')
nx.draw_networkx_edge_labels(G_ecosystem, pos, edge_labels=labels)
plt.title('Ecological Network Graph with Weights')
plt.show()

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація відстаней
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    shortest_paths = {node: [] for node in graph.nodes}
    shortest_paths[start] = [start]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]
    
    return distances, shortest_paths

# Знаходження найкоротших шляхів від кожної вершини до всіх інших
all_distances = {}
all_shortest_paths = {}
for node in G_ecosystem.nodes:
    distances, paths = dijkstra(G_ecosystem, node)
    all_distances[node] = distances
    all_shortest_paths[node] = paths

# Вивід найкоротших шляхів між всіма вершинами
for start_node, paths in all_shortest_paths.items():
    for end_node, path in paths.items():
        print(f"Shortest path from {start_node} to {end_node}: {path}")

# Аналіз основних характеристик
num_nodes_ecosystem = G_ecosystem.number_of_nodes()
num_edges_ecosystem = G_ecosystem.number_of_edges()
degrees_ecosystem = dict(G_ecosystem.degree())

print(f"Number of nodes: {num_nodes_ecosystem}")
print(f"Number of edges: {num_edges_ecosystem}")
print(f"Degrees of nodes: {degrees_ecosystem}")