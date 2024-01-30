import sys
sys.path.append('..')
from data_structure.linked_list import LinkedList

def is_palindrome(ll: LinkedList) -> bool:
    """
    Check if a linked list is a palindrome.
    """
    # ll_list
    ll_list = []
    current = ll.head
    while current != None:
        ll_list.append(current.data)
        current = current.next

    # 팰린드롬인지 확인
    for i in range(len(ll_list)):
        if ll_list[i] != ll_list[len(ll_list) - 1 - i]:
            return 0
        return 1

if __name__ == '__main__':
    # Write your test cases here
    ll = LinkedList()
    ll.insert_first(1)
    ll.insert_last(2)
    ll.insert_last(3)

    ll_2 = LinkedList()
    ll_2.insert_first(3)
    ll_2.insert_last(9)
    ll_2.insert_last(3)
    ll_2.insert_last(5)
    ll_2.insert_first(5) 

    testcase1 = ll
    testcase2 = ll_2

    assert is_palindrome(testcase1) == False
    assert is_palindrome(testcase2) == True