import random


class LinkedListNode:
    def __init__(self, data):
        self.data = str(data)
        self.next: LinkedListNode = None

class LinkedList:
    def __init__(self, root):
        self.root = root

    def addNode(self, newNode: LinkedListNode):
        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            while current.next is not None:
                current = current.next
            current.next = newNode

    def deleteNode(self, value):
        if self.root is None:
            return False

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

    def searchNode(self, value):
        target = self.root
        
        while target is not None:
            if target.data == value:
                return True
            target = target.next
        return False

    def getNode(self, index):
        target = self.root

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
    "insert x - Insert node with value X into the list",
    "delete x - Deletes the first node with value X from the list",
    "search x - Searches the list for a value x. Returns true if a node contains x and false otherwise",
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
                newList.addNode(LinkedListNode(n))
            newList.printList()
        elif userInput[0] == "print":
            newList.printList()
        elif userInput[0] == "quit":
            exit(0)
        elif len(userInput) > 1:
            if userInput[0] == "insert":
                newList.addNode(LinkedListNode(userInput[1]))
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
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")



main()