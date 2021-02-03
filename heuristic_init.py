import json

heuristic = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
                     'Eforie': 161, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226,
                     'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 'Oradea': 380,
                     'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Siubiu': 253, 'Fagaras': 176,
                     'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

with open("heuristic_data.json", "w") as write_file:
    json.dump(heuristic, write_file, indent=4)