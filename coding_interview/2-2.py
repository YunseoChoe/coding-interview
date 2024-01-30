import sys
sys.path.append('..')

from data_structure.linked_list import Node
from data_structure.linked_list import LinkedList

def nth_to_last(ll: LinkedList, n: int) -> Node:
    """
    Return nth to last element of a singly linked list.
    """
    # 뒤에서 n번 = (len - n + 1)번
    # ll의 길이 구하기
    length = 0
    current = ll.head
    while current != None:
        length += 1
        current = current.next

    c = ll.head
    for _ in range(length - n):
        c = c.next

    return c.data

if __name__ == '__main__':
    # Write your test cases here
    ll = LinkedList()
    ll.insert_first(0)
    ll.insert_last(1)
    ll.insert_last(2)
    ll.insert_last(3)
    
    testcase1 = ll
    assert nth_to_last(testcase1, 1) == 3
    assert nth_to_last(testcase1, 2) == 2
    assert nth_to_last(testcase1, 3) == 1
    assert nth_to_last(testcase1, 4) == 5 # false