class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        tmp = Node(data)
        tmp.next = None

        if self.head is None:
            self.head = tmp
            tmp.prev = None
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = tmp
        tmp.prev = last
        return

    def printList(self):

        tmp = self.head
        while tmp:
            print(str(tmp.data)+'->')
            last = tmp
            tmp = tmp.next


        while last:
            print(str(last.data)+'<-')
            last = last.prev

    def insertAfter(self, prev_node, new_data):
        tmp = Node(new_data)
        if self.head is None:
            self.head = new_data
            tmp.next = None
            tmp.prev = None
            return

        head = self.head
        while head:
            if head.data == prev_node:
                next = head.next
                head.next = tmp
                tmp.prev = head
                tmp.next = next
                next.prev = tmp
                return
            head = head.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.prev = None
        if self.head is None:
            self.head = new_node
            new_node.next = None
            return

        head = self.head
        head.prev = new_node
        new_node.next = head
        self.head = new_node
        return



if __name__ == "__main__":
    l1 =  DoublyLinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(4)
    l1.insertAfter(2, 3)
    l1.push(0)
    l1.printList()
