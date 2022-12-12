import random


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
        if node1 == node2:
            return

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
            searching.extend(queue)
            queue = []

            print("Current Search Depth: " + str(searchDepth))
            print("Elements In Depth: ", searching)
            print("Elements Explored: ", explored)
            print("---")

            while len(searching) > 0:
                exploring = searching.pop()
                explored.append(exploring)

                if exploring == end:
                    return True

                for node in self.nodeGraph[exploring]:
                    if node in explored or node in searching or node in queue:
                        continue
                    
                    queue.append(node)

            searchDepth += 1

        return False
    
    def dfs(self, start, end):
        explored = []
        stack = [start]
        
        while len(stack) > 0:
            searchingNode = stack[-1]

            print("Search Chain: " + ' -> '.join(stack))
            print("Explorable Nodes: ", self.nodeGraph[searchingNode])
            print("Fully Explored: ", explored)
            print("---")

            if searchingNode == end:
                return True

            for node in self.nodeGraph[searchingNode]:
                if node not in explored and node not in stack:
                    stack.append(node)
                    break

            if stack[-1] == searchingNode:
                explored.append(stack.pop())

        return False

    def randomGen(self):
        for _ in range(10):
            self.addNode()

        for _ in range(2):
            nodeSet1 = [_ for _ in self.nodeGraph.keys()]
            nodeSet2 = [_ for _ in self.nodeGraph.keys()]
            random.shuffle(nodeSet1)

            for x, y in zip(nodeSet1, nodeSet2):
                self.addEdge(x, y)






instructions = [
    "? - Read Instructions Again",
    "new - Adds a new vertex to the graph",
    "random - Randomly generates ten nodes and adds edges to every node"
    "remove x - Deletes a vertex with the specified id",
    "add x y - Adds an edge between two vertices",
    "destroy x y - Removes an edge between two vertices",
    "bfs x y - Searches for y from x with Breadth First Search",
    "dfs x y - Searches for y from x with Depth First Search",
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
        elif userInput[0] == "random":
            adjList.randomGen()
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
                elif userInput[0] == "bfs":
                    if adjList.bfs(userInput[1], userInput[2]):
                        print(userInput[2] + " found with BFS starting from " + userInput[1])
                    else:
                        print(userInput[2] + " cannot be found starting from " + userInput[1])
                elif userInput[0] == "dfs":
                    if adjList.dfs(userInput[1], userInput[2]):
                        print(userInput[2] + " found with DFS starting from " + userInput[1])
                    else:
                        print(userInput[2] + " cannot be found starting from " + userInput[1])
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
        else:
            print("Invalid input")

main()
