"""
To-do
-----

1. Add a dictionary to hold the value of each edge
2. Update add_vertex method to add an entry to the dictionary
3. Add a set_value method to set the value of a vertex
4. Check if any other methods etc need updated
"""




class Graph(object):
    def __init__(self,graph_dict = None):
        """Initialise a graph"""
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        """Getter that returns the
        the vertices of the graph"""
        return list(self.graph_dict.keys())

    def edges(self):
        """Getter that returns the
        edges of the graph"""
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """Adds the given vertex
        by adding a new entry to the
        graph_dict: {vertex:[]}"""
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        """Adds an edge between
        two vertices"""
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

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
        result = "vertices:"
        for key in self.__graph_dict:
            result += str(key) + " "
        result += "\nedges"
        for edge in self.__generate_edges():
            result += str(edge) + " "
        return result

if __name__ == "__main__":

    g = {"A": [-2,3],
         -1: [-2],
         -2: [1, -1, 3],
         2: [3],
         3: [-2, 2, 1]
         }
    graph = Graph(g)

    print("Graph:")
    print(str(g))







