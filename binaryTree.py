class BinaryTreeNode:
    def __init__(self, data):
        self.data = int(data)
        self.leftPointer: BinaryTreeNode = None
        self.rightPointer: BinaryTreeNode = None

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
                if target.leftPointer is None:
                    target.leftPointer = node
                    return
                else:
                    target = target.leftPointer
            else:
                if target.rightPointer is None:
                    target.rightPointer = node
                    return
                else:
                    target = target.rightPointer

    def deleteNode(self, value: int):
        grandparent = self.root

        # if grandparent.data == value:


        # while grandparent is not None:
        #     if grandparent.data == value:
        #         if grandparent.leftPointer is None and grandparent.rightPointer is not None:
