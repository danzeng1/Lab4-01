class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_vertex(self, vertex):
        self.vertices.add(vertex)
        if vertex not in self.edges:
            self.edges[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)
        if vertex2 not in self.edges[vertex1]:
            self.edges[vertex1].append(vertex2)

    def get_vertices(self):
        return list(self.vertices)

    def get_edges(self):
        edge_list = []
        for vertex in self.edges:
            for neighbor in self.edges[vertex]:
                edge_list.append((vertex, neighbor))
        return edge_list

    def is_connected(self, vertex1, vertex2):
        return vertex2 in self.edges.get(vertex1, [])

    def find_path(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return path
        if start not in self.edges:
            return None
        for node in self.edges[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None

def create_graph():
    return Graph()

def add_vertex(graph, vertex):
    graph.add_vertex(vertex)

def add_edge(graph, vertex1, vertex2):
    graph.add_edge(vertex1, vertex2)

def get_vertices(graph):
    return graph.get_vertices()

def get_edges(graph):
    return graph.get_edges()

def is_connected(graph, vertex1, vertex2):
    return graph.is_connected(vertex1, vertex2)

def find_path(graph, start, end):
    return graph.find_path(start, end)