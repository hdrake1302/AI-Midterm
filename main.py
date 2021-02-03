import json

import que as q

class Graph:
    def __init__(self):
        self.graph = dict()

    def add_edge(self, city1, city2, distance):
        if self.graph.get(city1) is None:
            self.graph[city1] = [(city2, distance)]
        else:
            self.graph[city1].append((city2, distance))

        if self.graph.get(city2) is None:
            self.graph[city2] = [(city1, distance)]
        else:
            self.graph[city2].append((city1, distance))

    def print_graph(self):
        for city in self.graph:
            print(city + ": ", self.graph[city])

    def BFS(self):
        queue = q.Queue()
        keys = list(self.graph.keys())

        visited = dict()
        for city in self.graph:
            visited[city] = False

        queue.enqueue(keys[0])

        while not queue.empty():
            x = queue.dequeue()

            print(x)
            for city in self.graph[x]:
                if visited[city[0]] is False:
                    visited[city[0]] = True
                    queue.enqueue(city[0])

    def h(self, n):
        """return heuristic calculations from arad to bucharest"""
        with open("heuristic_data.json", "r") as write_file:
            heuristic = json.load(write_file)

        return heuristic[n]





g = Graph()

with open("graph_data.json", "r") as read_file:
    g.graph = json.load(read_file)
