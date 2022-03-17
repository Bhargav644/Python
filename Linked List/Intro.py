class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def isEmpty(self):
        if(self):
            return False
        else:
            return True

    def printList(self):
        temp = self
        while(temp):
            print(temp.value)
            temp = temp.next

    def reverseList(self):
        prev = None
        current = self
        nextPtr = current.next
        while(current):
            current.next = prev
            prev = current
            current = nextPtr
            if(current):
                nextPtr = current.next
        return prev


def printList2(self):
    temp = self
    while(temp):
        print(temp.value)
        temp = temp.next


root = Node(1)
first = Node(2)
second = Node(3)
root.next = first
first.next = second

root.printList()
printList2(root.reverseList())
