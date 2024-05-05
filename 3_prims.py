import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_algo(self):
        visited = [False] * self.V
        min_heap = []
        start_vertex = 0
        visited[start_vertex] = True

        for neighbor, weight in self.graph[start_vertex]:
            heapq.heappush(min_heap, (weight, start_vertex, neighbor))

        min_spanning_tree = []
        minimum_cost = 0

        while min_heap:
            weight, u, v = heapq.heappop(min_heap)
            if not visited[v]:
                visited[v] = True
                min_spanning_tree.append((u, v, weight))
                minimum_cost += weight
                for neighbor, edge_weight in self.graph[v]:
                    if not visited[neighbor]:
                        heapq.heappush(min_heap, (edge_weight, v, neighbor))

        print("Prim's Minimum Spanning Tree:")
        for u, v, weight in min_spanning_tree:
            print(f"{u} - {v}: {weight}")
        print(f"Minimum cost: {minimum_cost}")


g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 4, 3)
g.add_edge(5, 4, 3)
g.prim_algo()
