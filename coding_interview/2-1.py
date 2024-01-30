import sys
sys.path.append('..')

from data_structure.linked_list import LinkedList

def delete_duplicates(ll: LinkedList) -> LinkedList:
    """
    Remove duplicates from an unsorted linked list.
    """
    # ll_list
    ll_list = []
    current = ll.head
    while current != None:
        ll_list.append(current.data)
        current = current.next
    
    # 딕셔너리에 저장
    # int -> str
    for i in range(len(ll_list)):
        ll_list[i] = str(ll_list[i])
    # dict 초기화
    dict = {}
    for i in range(len(ll_list)):
        # dict안에 있다면
        if ll_list[i] in dict:
            dict[ll_list[i]] += 1
        # dict안에 없다면
        else:
            dict[ll_list[i]] = 1
    
    # list에 저장
    list = []
    for key in dict:
        if dict[key] == 1:
            list.append(int(key))
        else:
            for _ in range(1):  # 1번만
                list.append(int(key))

    return list

if __name__ == '__main__':
    # Write your test cases here
    ll = LinkedList()
    ll.insert_first(1)
    ll.insert_last(2)
    ll.insert_last(3)
    ll.insert_first(0)
    ll.insert_last(4)
    ll.insert_last(4)
    ll.insert_last(4)
    ll.insert_last(3)
    ll.insert_first(4)
    ll.print() #  4 0 1 2 3 4 4 4 3

    ll_2 = LinkedList()
    ll_2.insert_first(-1)
    ll_2.insert_last(1)
    ll_2.insert_last(1)
    ll_2.insert_last(2)
    ll_2.insert_last(3)
    ll_2.insert_last(3)
    ll_2.print() # -1 1 1 2 3 3

    testcase1 = ll
    testcase2 = ll_2
    assert delete_duplicates(testcase1) == [4, 0, 1, 2, 3]
    assert delete_duplicates(testcase2) == [-1, 1, 2, 3]