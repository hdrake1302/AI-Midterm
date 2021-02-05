import json

from que import Queue

class Graph:
    def __init__(self):
        with open("ex2_graph.json", 'r') as read_file:
            self.graph = json.load(read_file)

    def print_graph(self):
        for rows in self.graph:
            for cols in rows:
                print(cols, end=' ')
            print()

    def BFS(self):
        count_islands = 0

        # all directions stored as a dictionary
        # (row, column) is the values of the keys
        # N: North, S: South, E: East, W: West
        directions = {"N": (-1, 0), "S": (1, 0),
                      "E": (0, 1), "W": (0, -1),
                      "NE": (-1, 1), "NW": (-1, -1),
                      "SE": (1, 1), "SW": (1, -1)}

        queue = Queue()

        for row in range(len(self.graph)):
            for column in range(len(self.graph[0])):
                if self.graph[row][column] == 1:
                    count_islands += 1
                    # Mark as visited
                    self.graph[row][column] = 2

                    queue.enqueue((row, column))
                    while not queue.empty():
                        current_r, current_c = queue.dequeue()

                        for d in directions:
                            # move to every direction
                            r = current_r + directions[d][0]
                            c = current_c + directions[d][1]

                            if 0 <= r < len(self.graph) and 0 <= c < len(self.graph) and self.graph[r][c] == 1:
                                queue.enqueue((r, c))
                                self.graph[r][c] = 2

        return count_islands

g = Graph()
g.print_graph()

print(g.BFS(), "islands")