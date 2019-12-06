class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            return
        else:
            tmp = self.head
        while tmp:
            print(str(tmp.data)+'->')
            tmp = tmp.next

    def append(self, x):
        tmp = Node(x)
        if self.head is None:
            self.head = tmp
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = tmp


def mergeLinkedLists(head1, head2):

    temp = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        temp = head1
        temp.next = mergeLinkedLists(head1.next, head2)
    else:
        temp = head2
        temp.next = mergeLinkedLists(head1, head2.next)

    return temp




l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(5)
# l1.printList()
l2 = LinkedList()
l2.append(1)
l2.append(3)
l2.append(4)
# l2.printList()
merged = LinkedList()
merged.head = mergeLinkedLists(l1.head, l2.head)
merged.printList()
