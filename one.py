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

# Аналіз основних характеристик
num_nodes_ecosystem = G_ecosystem.number_of_nodes()
num_edges_ecosystem = G_ecosystem.number_of_edges()
degrees_ecosystem = dict(G_ecosystem.degree())

print(f"Number of nodes: {num_nodes_ecosystem}")
print(f"Number of edges: {num_edges_ecosystem}")
print(f"Degrees of nodes: {degrees_ecosystem}")