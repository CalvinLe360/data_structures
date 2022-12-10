class AdjacencyList:
    def __init__(self):
        self.nodeUID = 0
        self.nodeGraph = {}

    def addNode(self):
        self.nodeGraph[str(self.nodeUID)] = set([])
        self.nodeUID += 1

    def removeNode(self, node):
        if node not in self.nodeGraph:
            print(str(node) + " is not in the graph!")
            return

        self.nodeGraph.pop(node)

    def addEdge(self, node1, node2):
        if node1 not in self.nodeGraph:
            print(str(node1) + " is not in the graph!")
            return

        if node2 not in self.nodeGraph:
            print(str(node2) + " is not in the graph!")
            return

        self.nodeGraph[node1].add(node2)
        self.nodeGraph[node2].add(node1)

    def removeEdge(self, node1, node2):
        if node1 not in self.nodeGraph:
            print(str(node1) + " is not in the graph!")
            return

        if node2 not in self.nodeGraph:
            print(str(node2) + " is not in the graph!")
            return

        self.nodeGraph[node1].discard(node2)
        self.nodeGraph[node2].discard(node1)