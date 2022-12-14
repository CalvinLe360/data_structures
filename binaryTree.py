import random


class BinaryTreeNode:
    def __init__(self, data):
        self.data = int(data)
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None
        self.parent: BinaryTreeNode = None

class BinaryTree:
    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def printTree(self):
        def height(root: BinaryTreeNode):
            return 1 + max(height(root.left), height(root.left)) if root else -1
        nLevels = height(self.root)
        width = pow(2, nLevels + 1)

        queue = [(self.root, 0, width, 'c')]
        levels = []

        while len(queue) > 0:
            node, level, x, align = queue.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append([])

                levels[level].append([node, level, x, align])
                seg = width // (pow(2, level + 1))
                queue.append((node.left, level + 1, x - seg, 'l'))
                queue.append((node.right, level + 1, x + seg, 'r'))


        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ''
            pstr = ''
            seg = width // (pow(2, i + 1))
            for n in l:
                valstr = str(n[0].data)
                if n[3] == 'r':
                    linestr += ' ' * (n[2]-preline-1-seg-seg//2) + '¯' * (seg +seg//2) + '\\'
                    preline = n[2] 
                if n[3]=='l':
                    linestr += ' ' * (n[2]-preline-1) + '/' + '¯' * (seg + seg // 2)  
                    preline = n[2] + seg + seg // 2
                pstr += ' ' * (n[2]-pre-len(valstr)) + valstr # correct the potition acording to the number size
                pre = n[2]
            print(linestr)
            print(pstr)  

    def addNode(self, node: BinaryTreeNode):
        if self.root is None:
            self.root = node
            return
        
        target = self.root
        while True:
            if node.data < target.data:
                if target.left is None:
                    target.left = node
                    node.parent = target
                    return
                else:
                    target = target.left
            else:
                if target.right is None:
                    target.right = node
                    node.parent = target
                    return
                else:
                    target = target.right

    def getPredecessor(self, node: BinaryTreeNode):
        if not node.left:
            return node
        
        target = node.left
        while target.right:
            target = target.right

        return target

    def getSuccessor(self, node: BinaryTreeNode):
        if not node.right:
            return node
        
        target = node.right
        while target.left:
            target = target.left

        return target
    
    def deleteNode(self, nodeValue):
        if self.root is None:
            return

        target = self.root
        while True:
            if target is None:
                return False

            if target.data == nodeValue:
                # No Children
                if target.left:
                    predecessor = self.getPredecessor(target)
                    target.data, predecessor.data = predecessor.data, target.data
                    target = predecessor
                elif target.right:
                    successor = self.getSuccessor(target)
                    target.data, successor.data = successor.data, target.data
                    target = successor
                else:
                    if target.parent:
                        if target.parent.left == target:
                            target.parent.left = None
                        else:
                            target.parent.right = None
                    target.parent = None
                    if target == self.root:
                        self.root = None
                    return True
            elif nodeValue < target.data:
                target = target.left
            else:
                target = target.right

    def searchNode(self, nodeValue):
        if self.root is None:
            return False

        target = self.root
        while True:
            if target is None:
                return False

            if target.data == nodeValue:
                return True
            elif nodeValue < target.data:
                target = target.left
            else:
                target = target.right

    def random(self, nodeCount):
        if self.root is None:
            self.addNode(BinaryTreeNode("50"))

        for _ in range(nodeCount):
            nodeValue = random.randint(0, 100)
            self.addNode(BinaryTreeNode(str(nodeValue)))

    def inorder(self, node: BinaryTreeNode):
        if node is None:
            return

        self.inorder(node.left)
        print(node.data, end= " -> ")
        self.inorder(node.right)

    def preorder(self, node: BinaryTreeNode):
        if node is None:
            return

        print(node.data, end= " -> ")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node: BinaryTreeNode):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end= " -> ")

    

instructions = [
    "? - Read Instructions Again",
    "add x - Adds a node to the binary tree",
    "delete x - Deletes a node in the binary tree if found",
    "search x - Finds a node int the binary tree",
    "random x - Adds this many nodes of random values to the tree",
    "print - Prints the entire linked list",
    "inorder - Prints elements inorder",
    "preorder - Prints elements preorder",
    "postorder - Prints elements postorder",
    "quit - Closes the program",
]

def main():
    binaryTree = BinaryTree(None)

    for i in instructions:
        print(i)

    while True:
        userInput = input("Type your input: ").split()

        if userInput[0] == "?":
            for i in instructions:
                print(i)
        elif userInput[0] == "print":
            binaryTree.printTree()
        elif userInput[0] == "inorder":
            binaryTree.inorder(binaryTree.root)
            print()
        elif userInput[0] == "preorder":
            binaryTree.preorder(binaryTree.root)
            print()
        elif userInput[0] == "postorder":
            binaryTree.postorder(binaryTree.root)
            print()
        elif userInput[0] == "quit":
            exit(0)
        elif len(userInput) > 1:
            if userInput[0] == "add":
                binaryTree.addNode(BinaryTreeNode(userInput[1]))
                binaryTree.printTree()
            elif userInput[0] == "delete":
                if binaryTree.deleteNode(int(userInput[1])):
                    print("Successfully deleted from the tree: ", userInput[1])
                    binaryTree.printTree()
                else:
                    print("Cannot delete the specified node: ", userInput[1])
            elif userInput[0] == "search":
                if binaryTree.searchNode(int(userInput[1])):
                    print("Successfully found a node in tree: ", userInput[1])
                else:
                    print("Cannot find the specified node: ", userInput[1])
            elif userInput[0] == "random":
                binaryTree.random(int(userInput[1]))
                binaryTree.printTree()
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")

main()