class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_first(self, data):
        new_node = Node(data, None, None)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, data):
        new_node = Node(data, None, None)
        if self.head == None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def delete_first(self):
        if self.head == None:
            print("노드 없음")
        else:
            next = self.head.next
            next.prev = None
            self.head = next

    def delete_last(self):
        if self.head == None:
            print("노드 없음")
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = None
            
    def print(self):
        cur = self.head
        while cur.next != None:
            print(f'{cur.data} -> ', end = "")
            cur = cur.next
        print()


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_first(3)
    dll.insert_last(4)
    dll.delete_last()
    dll.insert_first(0)
    dll.print()


