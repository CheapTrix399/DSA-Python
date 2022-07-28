from datastructures import Stack, Queue
class Graph:
    def __init__(self,vertices,edges):
        self.vertices = vertices
        self.edges = edges
    def get_neighbours(self,vertex):
        neighbors = []
        for edge in self.edges.items():
            if(edge[0]==vertex):
                if(edge[1] not in neighbors):
                    neighbors.append(edge[1])
            elif(edge[1]==vertex):
                if(edge[0] not in neighbors):
                    neighbors.append(edge[0])
        return neighbors
    def depth_first_search(self,start_vertex,find_vertex):
        stack = Stack()
        visited = [start_vertex]
        stack.push(start_vertex)
        path_exists = 0
        path = []
        while(len(stack.stack)!=0):
            neighbors = self.get_neighbours(stack.stack[-1])
            removal = []
            for neighbor in neighbors:
                if(neighbor in visited):
                    removal.append(neighbor)
            for x in removal:
                neighbors.remove(x) #removing unvisited neighbors
            if(len(neighbors)!=0):
                stack.push(neighbors[0])
                visited.append(neighbors[0])
                if(neighbors[0]==find_vertex):
                    path = stack.stack.copy()
                    path_exists = 1
            else:
                stack.pop()
        return [path_exists,path]
    def breadth_first_search(self,start_vertex,find_vertex):
        q = Queue()
        visited = [start_vertex]
        q.push(start_vertex)
        while(len(q.q)!=0):
            neighbors = self.get_neighbours(q.q[-1])
            q.pop()
            removal = []
            for neighbor in neighbors:
                if(neighbor in visited):
                    removal.append(neighbor)
            for x in removal:
                neighbors.remove(x) #removing unvisited neighbors
            if(len(neighbors)!=0):
                for neighbor in neighbors:
                    q.push(neighbor)
                    visited.append(neighbor)
                    if(neighbor==find_vertex):
                        path_exists = 1
            else:
                q.pop()
        return path_exists       

# vertices = ["S","A","B","C","D"]
# edges = {"S":"A","A":"D","D":"C","C":"S","S":"B","B":"D"}
# graph = Graph(vertices,edges)
# dfs = graph.depth_first_search("S","D")
# print(dfs[1])
# bfs = graph.breadth_first_search("A","C")
# print(bfs)