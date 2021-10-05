from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    def getTranspose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def printSCCs(self):

        stack = []
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                self.fillOrder(i, visited, stack)

        # Create a reversed graph
        gr = self.getTranspose()

        visited = [False] * self.V

        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.DFSUtil(i, visited)


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print("Following are strongly connected components " +
      "in given graph")
g.printSCCs()
