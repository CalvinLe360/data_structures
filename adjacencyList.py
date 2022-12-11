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

        for n in [_ for _ in self.nodeGraph[node]]:
            self.removeEdge(node, n)

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

    def printGraph(self):
        for n in self.nodeGraph:
            print(n, end=" -> ")
            for adj in self.nodeGraph[n]:
                print(adj, end=", ")

            print()

    def bfs(self, start, end):
        explored = []
        searching = []
        queue = [start]
        
        searchDepth = 0
        while len(queue) > 0:
            searching = queue
            queue = []



instructions = [
    "? - Read Instructions Again",
    "new - Adds a new vertex to the graph",
    "remove x - Deletes a vertex with the specified id",
    "add x y - Adds an edge between two vertices",
    "destroy x y - Removes an edge between two vertices",
    "print - Prints the entire linked list",
    "quit - Closes the program",
]

def main():
    adjList = AdjacencyList()

    for i in instructions:
        print(i)

    while True:
        userInput = input("Type your input: ").split()

        if userInput[0] == "?":
            for i in instructions:
                print(i)
        elif userInput[0] == "new":
            adjList.addNode()
            adjList.printGraph()
        elif userInput[0] == "print":
            adjList.printGraph()
        elif userInput[0] == "quit":
            exit(0)
        elif len(userInput) > 1:
            if userInput[0] == "delete":
                adjList.removeNode(userInput[1])
                adjList.printGraph()
            elif len(userInput) > 2:
                if userInput[0] == "add":
                    adjList.addEdge(userInput[1], userInput[2])
                    adjList.printGraph()
                elif userInput[0] == "destroy":
                    adjList.removeEdge(userInput[1], userInput[2])
                    adjList.printGraph()
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
        else:
            print("Invalid input")

main()
