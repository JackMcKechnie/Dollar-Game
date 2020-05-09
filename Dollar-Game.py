"""
To-do
-----

1. Add a dictionary to hold the value of each edge ✓
2. Update add_vertex method to add an entry to the dictionary ✓
3. Add a set_value method to set the value of a vertex ✓
4. Check if any other methods etc need updated
"""




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

    def __str__(self):
        result = "Vertices:"
        for key in self.graph_dict:
            result += str(key) + "(" + str(self.value_dict[key]) + ") "
        result += "\nEdges: "
        for edge in self.__generate_edges():
            result += str(edge) + " "
        return result


if __name__ == "__main__":

    g = {"A": ["C"],
         "B": ["C"],
         "C": ["A", "B"]
         }
    graph = Graph(g)
    graph.set_vertex_value("A", 1)
    graph.set_vertex_value("B", 3)
    graph.set_vertex_value("C", 2)

    print(str(graph))








