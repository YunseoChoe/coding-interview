from typing import List

class Node:
    def __init__(self, data: int, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_first(self, data: int):
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_of_nodes += 1
    
    def insert_last(self, data: int):
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
        self.num_of_nodes += 1

    def delete_first(self):
        if self.head == None:
            print("노드 없음")
        else:
            next = self.head.next
            self.head = next

    def delete_last(self):
        if self.head == None:
            print("노드 없음")
        elif self.head.next == None:
            self.head = None
        else:
            cur = self.head
            while cur.next.next != None:
                cur = cur.next
            cur.next = None

    def print(self):
        cur = self.head
        while cur != None:
            print(cur.data, end = "")
            print("->", end = "")
            cur = cur.next
        print()
    
    def to_array(self) -> List:
        pass

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_first(3)
    ll.insert_last(7)
    ll.insert_first(1)
    ll.insert_last(5)
    ll.delete_first()
    ll.delete_last()
    ll.print()

