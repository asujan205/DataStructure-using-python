class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict={

        }
        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)
    def find_path(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]

        
        
if __name__ == "__main__":
    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    graph = Graph(routes)
    print(graph.edges)
    start="Mumbai"
    end="Bangaluru"
    print(graph.find_path(start,end))
    
    