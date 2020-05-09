"""
To-do
-----

1. Generate random winnable graph
    - Money on the board >= genus(#edges - #vertices + 1)
"""


import random

class Graph(object):
    def __init__(self   , graph_dict = None):
        """Initialise a graph"""
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

        self.value_dict = {}

    def vertices(self):
        """Getter that returns the
        the vertices of the graph"""
        return list(self.graph_dict.keys())

    def edges(self):
        """Getter that returns the
        edges of the graph"""
        return self.__generate_edges()

    def add_vertex(self, vertex, value):
        """Adds the given vertex
        by adding a new entry to the
        graph_dict: {vertex:[]}"""
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
            self.value_dict[vertex] = value

    def add_edge(self, edge):
        """Adds an edge between
        two vertices"""
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def set_vertex_value(self, vertex, value):
        """Sets the value of a vertex"""
        self.value_dict[vertex] = value

    def __generate_edges(self):
        """Static method to
        generate the edges of the
        graph. An edge is a set with
        one or two vertices"""
        edges = []
        for vertex in self.graph_dict:
            for neighbor in self.graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def transfer(self, vertex1, vertex2):
        """Transfers 1 unit from vertex1
        to vertex2"""
        self.value_dict[vertex1] -= 1
        self.value_dict[vertex2] += 1

    def game_won(self):
        for value in self.value_dict:
            if self.value_dict[value] < 0:
                return False
        return True

    def __str__(self):
        result = "Vertices:"
        for key in self.graph_dict:
            result += str(key) + "(" + str(self.value_dict[key]) + ") "
        result += "\nEdges: "
        for edge in self.__generate_edges():
            result += str(edge) + " "
        return result


def generate_winnable_graph():
    """Static method that generates
    a graph where it is possible to win"""
    # Generate a random number from 1-26
    vertex_num = random.randrange(1, 27)
    # Dictionary to hold the vertices
    vertices = {}
    # Add vertex_num vertices
    for i in range(vertex_num):
        vertices[chr(i+65)] = []

    #Add edges
    for i in range(vertex_num):
        vertices[chr(i+65)] = [chr(i+66)]
    vertices[chr(vertex_num+65)] = [chr(65)]

    out_graph = Graph(vertices)

    #Generate values for each vertice
    for i in range(vertex_num):
        out_graph.set_vertex_value(vertices[chr(i + 65)], i)

if __name__ == "__main__":

    g = {"A": ["C"],
         "B": ["C"],
         "C": ["A", "B"]
         }
    graph = Graph(g)
    graph.set_vertex_value("A", -1)
    graph.set_vertex_value("B", 0)
    graph.set_vertex_value("C", 0)

    generate_winnable_graph()









