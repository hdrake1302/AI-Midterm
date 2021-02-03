import json

import que as q

from queue import PriorityQueue


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

    def heuristic_search(self, start, end):
        """Perform inform search using heuristic algorithm"""
        queue = PriorityQueue()
        queue.put((self.h(start), start))

        # visited variable to check if a city is visited or not
        visited = dict()
        for city in self.graph:
            visited[city] = False

        while not queue.empty():
            x = queue.get()
            current_city = x[1]
            visited[current_city] = True

            print(x)
            if current_city == end:
                break

            for city in self.graph[current_city]:
                if visited[city[0]] is False:
                    queue.put((self.h(city[0]), city[0]))

    def A_search(self, start, end):
        """Perform inform search using A* algorithm"""
        queue = PriorityQueue()
        queue.put((self.h(start) + 0, 0, start))

        # visited variable to check if a city is visited or not
        visited = dict()
        for city in self.graph:
            visited[city] = False

        while not queue.empty():
            x = queue.get()
            current_city = x[2]
            visited[current_city] = True

            cost = x[1]
            print(x)
            if current_city == end:
                break

            for city in self.graph[current_city]:
                tmp_cost = city[1] + cost
                if visited[city[0]] is False:
                    queue.put((self.h(city[0]) + tmp_cost, tmp_cost, city[0]))


g = Graph()

with open("graph_data.json", "r") as read_file:
    g.graph = json.load(read_file)

g.A_search('Arad', 'Bucharest')