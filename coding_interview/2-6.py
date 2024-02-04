import sys
sys.path.append('..')
from data_structure.linked_list import LinkedList

def is_palindrome(ll: LinkedList) -> bool:
    """
    Check if a linked list is a palindrome.
    """
    # 연결리스트 뒤집기
    lk = ll.head
    reversed_ll = LinkedList()
    while lk != None:
        reversed_ll.insert_first(lk.data)
        lk = lk.next

    # 팰린드롬인지 확인
    # ll vs reverser_ll
    current1 = ll.head
    current2 = reversed_ll.head
    while current1 != None:
        # 하나라도 다르면 False
        if current1.data != current2.data:
            return 0
        current1 = current1.next
        current2 = current2.next
    # 모두 같으면 True
    return 1

if __name__ == '__main__':
    # Write your test cases here
    ll = LinkedList()
    ll.insert_first(1)
    ll.insert_last(2)
    ll.insert_last(3)
    # 1->2->3->

    ll_2 = LinkedList()
    ll_2.insert_first(3)
    ll_2.insert_last(9)
    ll_2.insert_last(3)
    ll_2.insert_last(5)
    ll_2.insert_first(5) 
    # 5->3->9->3->5->

    testcase1 = ll
    testcase2 = ll_2

    assert is_palindrome(testcase1) == False
    assert is_palindrome(testcase2) == True