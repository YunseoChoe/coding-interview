import sys
sys.path.append('..')
from data_structure.linked_list import LinkedList

def sum_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """
    Sum two linked lists. Each node contains a single digit and the digits are 
    stored in reverse order.
    """
    # ll1 길이 구하기
    ll1_length = 0
    current = ll1.head
    while current != None:
        ll1_length +=1
        current = current.next
    # ll2 길이 구하기
    ll2_length = 0
    current = ll2.head
    while current != None:
        ll2_length +=1
        current = current.next

    # list_1, list_2 배열 초기화
    list_1 = []
    for i in range(ll1_length):
        list_1.append(0)
    list_2 = []
    for i in range(ll2_length):
        list_2.append(0)

    # 역순으로 저장
    current = ll1.head
    current2 = ll2.head
    while True:
        for i in range(ll1_length - 1, -1, -1):
            list_1[i] = current.data
            current = current.next
        for i in range(ll2_length - 1, -1, -1):
            list_2[i]= current2.data
            current2 = current2.next
        break

    # 합
    list_1_int = ""
    list_2_int = ""
    for i in range(len(list_1)):
        list_1_int += str(list_1[i])
    for i in range(len(list_2)):
        list_2_int += str(list_2[i])
    list_1_int = int(list_1_int)
    list_2_int = int(list_2_int)

    sum = list_1_int + list_2_int
    
    return sum

if __name__ == '__main__':
    # Write your test cases here
    ll = LinkedList()
    ll.insert_first(7)
    ll.insert_last(1)
    ll.insert_last(6)
    # # 7->1->6-> == 617

    ll_2 = LinkedList()
    ll_2.insert_first(5)
    ll_2.insert_last(9)
    ll_2.insert_last(2)
    # # 5->9->2-> == 295

    assert sum_lists(ll, ll_2) == 912 # [9, 1, 2]
