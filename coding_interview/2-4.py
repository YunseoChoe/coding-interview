import sys
sys.path.append('..')
from data_structure.linked_list import LinkedList

def partition(ll: LinkedList, x: int) -> LinkedList:
    """
    Partition a linked list around a value x, such that all nodes less than x 
    come before all nodes greater than or equal to x.
    """
    # x를 기준으로 left, right 나누기
    lll = LinkedList()
    rll = LinkedList()
    current = ll.head
    while current != None:
        if current.data < x:
            lll.insert_last(current.data)
        else:
            rll.insert_last(current.data)
        current = current.next

    # 합치기
    current = lll.head
    while current.next != None:
        current = current.next
    current.next = rll.head

    return lll

if __name__ == '__main__':
    # Write your test cases here
    ll = LinkedList()
    ll.insert_first(3)
    ll.insert_last(5)
    ll.insert_last(8)
    ll.insert_last(5)
    ll.insert_last(10)
    ll.insert_last(2)
    ll.insert_last(1)
    # 3->5->8->5->10->2->1->

    # lll: 3, 2, 1
    # rll: 5, 8, 5, 10
    # 3,2,1,5,8,5,10

    ll_2 = LinkedList()
    ll_2.insert_first(0)
    ll_2.insert_last(5)
    ll_2.insert_last(3)
    ll_2.insert_last(-1)
    # 0->5->3-> -1->
    # lll: 0, -1
    # rll: 5, 3
    # 0, -1, 5, 3

    testcase1 = partition(ll, 5)
    testcase2 = partition(ll_2, 2)

    # array로 전환
    array_testcase1 = testcase1.to_array()
    array_testcase2 = testcase2.to_array()

    assert array_testcase1 == [3, 2, 1, 5, 8, 5, 10]
    assert array_testcase2 == [0, -1, 5, 3]