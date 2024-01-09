class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_first(self, data):
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head.next
            self.head.next = new_node

    def insert_last(self, data):
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node

    def delete_first(self):
        if self.head == None:
            print("노드 없음")
        else:
            self.head.next = self.head.next.next

    def delete_last(self):
        if self.head == None:
            print("노드 없음")
        else:
            cur = self.head.next
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = cur
        
    def print(self):
        cur = self.head.next
        print(cur.data, end="->")
        cur = cur.next
        while cur != self.head.next:
            print(cur.data, end="->")
            cur = cur.next
        print()

if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.insert_first(3)
    cll.insert_last(5)
    cll.insert_last(7)
    cll.delete_first()
    cll.insert_first(0)
    cll.delete_last()
    cll.print()