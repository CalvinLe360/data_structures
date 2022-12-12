class BinaryTreeNode:
    def __init__(self, data):
        self.data = int(data)
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None

class BinaryTree:
    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def addNode(self, node: BinaryTreeNode):
        if self.root is None:
            self.root = node
            return
        
        target = self.root
        while True:
            if node.data < target.data:
                if target.left is None:
                    target.left = node
                    return
                else:
                    target = target.left
            else:
                if target.right is None:
                    target.right = node
                    return
                else:
                    target = target.right

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
    binaryTree = BinaryTree()

    for i in instructions:
        print(i)

    while True:
        print()