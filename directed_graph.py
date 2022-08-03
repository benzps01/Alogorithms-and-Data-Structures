'''
This is an example of directed graph
Created Graph data structure
Added method to find all paths between 2 points
created method to find shortest path between 2 points
'''

class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for source, dest in self.edges:
            if source in self.graph_dict:
                self.graph_dict[source].append(dest)

            else:
                self.graph_dict[source] = [dest]
        print("Graph dict: ",self.graph_dict)

    def get_paths(self, source, dest,path = []):
        path = path + [source]
        if source == dest:
            return [path]

        if source not in self.graph_dict:
            return []     

        paths = []
        for node in self.graph_dict[source]:
            if node not in path:
                new_path = self.get_paths(node,dest,path)
                for p in new_path:
                    paths.append(p)

        return paths

    def get_shortest_path(self, source, dest, path=[]):
        path = path + [source]
        if source == dest:
            return path
        if source not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[source]:
            if node not in path:
                sp = self.get_shortest_path(node,dest,path)
                if shortest_path is None or len(sp) < len(shortest_path):
                    shortest_path = sp
                
        return shortest_path





                 


routes = [
    ('Mumbai','Paris'),
    ('Mumbai','Dubai'),
    ('Paris','Dubai'),
    ('Paris','New York'),
    ('Dubai','New York'),
    ('New York','Toronto')
]

route_graph = Graph(routes)
source = "Mumbai"
dest = "New York"

#print(f"Paths between {source} and {dest}: ",route_graph.get_paths(source,dest))
print(f"Shortest paths between {source} and {dest}: ",route_graph.get_shortest_path(source,dest))

