import sys
sys.path.append('..')
from data_structure.linked_list import LinkedList

def sum_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """
    Sum two linked lists. Each node contains a single digit and the digits are 
    stored in reverse order.
    """
    # 역순
    sum1 = LinkedList()
    sum2 = LinkedList()
    current1 = ll1.head
    current2 = ll2.head
    while current1 != None: 
        sum1.insert_first(current1.data)
        current1 = current1.next
    while current2 != None:
        sum2.insert_first(current2.data)
        current2 = current2.next

    # 정수로 저장
    str1 = ""
    str2 = ""
    current1 = sum1.head
    current2 = sum2.head

    while current1 != None:
        str1 += str(current1.data)
        current1 = current1.next
    while current2 != None:
        str2 += str(current2.data)
        current2 = current2.next

    # 더하기
    sum = int(str1) + int(str2)
    sum = str(sum)
    ll_sum = LinkedList()

    for i in range(len(sum)):
        ll_sum.insert_first(int(sum[i]))

    # ll_sum.print()

    return ll_sum

if __name__ == '__main__':

    # Write your test cases here
    ll = LinkedList()
    ll.insert_first(7)
    ll.insert_last(1)
    ll.insert_last(6)
    # 7->1->6-> == 617

    ll_2 = LinkedList()
    ll_2.insert_first(5)
    ll_2.insert_last(9)
    ll_2.insert_last(2)
    # 5->9->2-> == 295

    testcase1 = sum_lists(ll, ll_2)

    # array로 변환
    array_testcase1 = testcase1.to_array()

    assert array_testcase1 == [2, 1, 9] 