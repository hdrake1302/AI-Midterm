import json

from main import Graph

g = Graph()

g.add_edge("Arad", "Timisoara", 118)
g.add_edge("Arad", "Siubiu", 140)
g.add_edge("Arad", "Zerind", 75)

# Zerind
g.add_edge("Zerind", "Oradea", 71)

# Oradea
g.add_edge("Oradea", "Siubiu", 151)

# Siubiu
g.add_edge("Siubiu", "Fagaras", 99)
g.add_edge("Siubiu", "Rimnicu Vilcea", 80)

# Fagaras
g.add_edge("Fagaras", "Bucharest", 211)

# Bucharest
g.add_edge("Bucharest", "Pitesti", 101)
g.add_edge("Bucharest", "Giurgiu", 90)
g.add_edge("Bucharest", "Urziceni", 85)

# Timisoara
g.add_edge("Timisoara", "Lugoj", 70)

# Lugoj
g.add_edge("Lugoj", "Mehadia", 75)

# Mehadia
g.add_edge("Mehadia", "Drobeta", 75)

# Drobeta
g.add_edge("Drobeta", "Craiova", 120)

# Craiova
g.add_edge("Craiova", "Rimnicu Vilcea", 146)
g.add_edge("Craiova", "Pitesti", 138)

# Rimnicu Vilcea
g.add_edge("Rimnicu Vilcea", "Pitesti", 97)

# Pitesti
# Already

# Urziceni
g.add_edge("Urziceni", "Hirsova", 98)
g.add_edge("Urziceni", "Vaslui", 142)

# Hirsova
g.add_edge("Hirsova", "Eforie", 86)

# Vaslui
g.add_edge("Vaslui", "Iasi", 92)

# Iasi
g.add_edge("Iasi", "Neamt", 87)

with open("data_file.json", "w") as write_file:
    json.dump(g.graph, write_file, indent=4)