class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print()
        print("Graph Dict:", self.graph_dict)
        print("-----------")

    def get_paths(self, start, end, path=[]): #finds all paths from start destination to end destination, default value of paths is empty
        path = path + [start]
        
        if start == end: #if the start and end destination are the same -> returns the path with just a start
            return [path]

        if start not in self.graph_dict: #paths if there are no paths from the start destination
            return []
        
        paths = []
        for node in self.graph_dict[start]: #iterates through the values of the dictionary
            if node not in path: #check if the destination has been visited or not
                new_paths = self.get_paths(node, end, path) #NOTE: use recursion to get the end destination by going through all the possible values of start key
                #NOTE: use debugging to follow recursion -> **difficult to follow**
                for p in new_paths: #iterates through different paths
                    paths.append(p) #adds different paths to a list
        
        return paths #returns a list with all possible paths

    def get_shortest_path(self, start, end, path=[]): #finds shortest paths based on number of stops
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp: #check because function can return None
                    if shortest_path is None or len(sp) < len(shortest_path): #check if the shortest_path is empty or if the current short path length is less than the current shortest path length
                        shortest_path = sp
        return shortest_path


if __name__ == '__main__':
    routes = [ #use tuples to simulate routes between cities
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    d = { #want to transform given tuple structure to dictionary data structure
        "Mumbai": ["Paris", "Dubai"],
        "Paris": ["Dubai", "New York"]
    }

    route_graph = Graph(routes)
    start = "Mumbai"
    end = "Mumbai"
    print(f"Paths between {start} and {end}:", route_graph.get_paths(start, end))

    print()

    start = "Toronto"
    end = "Mumbai"
    print(f"Paths between {start} and {end}:", route_graph.get_paths(start, end))

    print()

    start = "Mumbai"
    end = "New York"
    print(f"Paths between {start} and {end}:", route_graph.get_paths(start, end))

    print()

    #testing shortest path
    start = "Toronto"
    end = "New York"
    print(f"Shortest Path between {start} and {end}:", route_graph.get_shortest_path(start, end))

    print()

    start = "New York"
    end = "New York"
    print(f"Shortest Path between {start} and {end}:", route_graph.get_shortest_path(start, end))

    print()

    start = "Mumbai"
    end = "New York"
    print(f"Shortest Path between {start} and {end}:", route_graph.get_shortest_path(start, end))

    print()

    start = "Paris"
    end = "New York"
    print(f"Shortest Path between {start} and {end}:", route_graph.get_shortest_path(start, end))
    
    print()