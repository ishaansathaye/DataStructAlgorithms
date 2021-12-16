class Graph:
    def __init__(self, edges):
        self.edges = edges
    


if __name__ == '__main__':
    routes = [ #use tuples to simulate routes between cities
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)