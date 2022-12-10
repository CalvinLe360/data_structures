import random


class LinkedListNode:
    def __init__(self, data):
        self.data = str(data)
        self.next: LinkedListNode = None

class LinkedList:
    def __init__(self, root):
        self.root = root

    def appendNode(self, newNode: LinkedListNode):
        # Case: Root
        if self.root is None:
            self.root = newNode
        else:
            # Appending to the end of the list
            current = self.root
            while current.next is not None:
                current = current.next
            current.next = newNode

    def insertNode(self, newNode: LinkedListNode, index: int):
        # Error Case
        if index < 0:
            return False

        # Case: No Root Node or Index 0
        if index == 0 or self.root is None:
            newNode.next = self.root
            self.root = newNode
        else:
            # Inserts at specified position or end if the index is too high
            target = self.root
            while index > 1 and target.next is not None:
                target = target.next
                index -= 1
            
            newNode.next = target.next
            target.next = newNode
        
        return True

    def deleteNode(self, value):
        if self.root is None:
            return False

        # Case: Root Node
        if self.root.data == value:
            self.root = self.root.next
            return True
        else:
            target = self.root
            while target.next is not None:
                if target.next.data == value:
                    target.next = target.next.next
                    return True
                target = target.next

        return False

    def deleteNodeAt(self, index):
        # Case: Linked List has no node
        if self.root is None:
            return False
        
        # Case: Root Node
        if index == 0:
            self.root = self.root.next
        else:
            target = self.root
            while index > 1 and target.next is not None:
                target = target.next
                index -= 1
            # Case: Index is too large
            if target.next is None:
                return False
            target.next = target.next.next
        
        return True

    def searchNode(self, value):
        target = self.root
        
        while target is not None:
            if target.data == value:
                return True
            target = target.next
        return False

    def getNode(self, index):
        target = self.root

        # Iterates through next pointers until found
        while target is not None and index > 0:
            target = target.next
            index -= 1
        
        if target is None:
            return None
        else:
            return target.data
    
    def printList(self):
        target = self.root
        while target is not None:
            print(target.data, end=" -> ")
            target = target.next
        print("None")

instructions = [
    "? - Read Instructions Again",
    "append x - Append node with value X into the tail of the list",
    "delete x - Deletes the first node with value X from the list",
    "search x - Searches the list for a value x. Returns true if a node contains x and false otherwise",
    "insert x y - Inserts a node with value x to index y",
    "remove x - Removes a node at the specified index",
    "print - Prints the entire linked list",
    "random - Random Insertion of numbers",
    "quit - Closes the program",
]

def main():
    newList = LinkedList(None)
    numbers = list(range(10))
    random.shuffle(numbers)

    for i in instructions:
        print(i)

    while True:
        userInput = input("Type your input: ").split()

        if userInput[0] == "?":
            for i in instructions:
                print(i)
        elif userInput[0] == "random":
            for n in numbers:
                newList.appendNode(LinkedListNode(n))
            newList.printList()
        elif userInput[0] == "print":
            newList.printList()
        elif userInput[0] == "quit":
            exit(0)
        elif len(userInput) > 1:
            if userInput[0] == "append":
                newList.appendNode(LinkedListNode(userInput[1]))
                newList.printList()
            elif userInput[0] == "delete":
                result = newList.deleteNode(userInput[1])
                if result == False:
                    print("Node not found - no deletion made")
                else:
                    newList.printList()
            elif userInput[0] == "search":
                result = newList.searchNode(userInput[1])
                if result == False:
                    print("Node not found - searched for: " + userInput[1])
                else:
                    print("Node found! Searched for: " + userInput[1])
            elif userInput[0] == "remove":
                result = newList.deleteNodeAt(int(userInput[1]))
                if result == False:
                    print("Node not found - no deletion made")
                else:
                    newList.printList()
            elif userInput[0] == "insert" and len(userInput) > 2:
                if userInput[2].isnumeric():
                    newList.insertNode(LinkedListNode(userInput[1]), int(userInput[2]))
                    newList.printList()
                else:
                    print("Invalid Input bruhh")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")



main()