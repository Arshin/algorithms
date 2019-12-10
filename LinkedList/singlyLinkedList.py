# How do you find the middle element of a singly linked list in one pass?
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            return None

        tmp = self.head
        while tmp:
            print(str(tmp.data)+'->')
            tmp = tmp.next

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

    def middleElement(self):
        slow = self.head
        fast = self.head

        if self.head is not None:
            if (fast is not None and fast.next is not None):
                fast = fast.next.next
                slow = slow.next

        print('middle is '+ str(slow.data))


if __name__ == "__main__":
    l1 =  DoublyLinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(4)
    l1.append(5)
    l1.printList()
    l1.middleElement()
