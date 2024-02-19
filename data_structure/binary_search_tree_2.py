# class Node:
#     def __init__(self, value):
#         self.value: int = value
#         self.left: Node = None
#         self.right: Node = None

# class BST:
#     def __init__(self):
#         self.root: Node = None
    
#     def search(self, value):
#         return self._search(self.root, value)
    
#     def _search(self, node: Node, value: int):
#         if node.value > value:
#             return self._search(node.left, value)
    
#     def insert(self, value):
#         return self._insert(self.root, value)

#     def _insert(self, value):
#         pass

#     def delete(self, value):
#         return self._delete(self.root, value)

#     def _delete(self, value):
#         pass


class Node:
    def __init__(self, value: int): 
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def search(self, value: int) -> bool:
        if self.value < value: 
            if self.right == None:
                return False
            else:
                return self.right.search(value)
        elif self.value > value:
            if self.left == None:
                return False
            else:
                return self.left.search(value)
        else:
            return True # 있으면 True

    def insert(self, value): #재귀함수
        if self.value < value:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = Node(value)
        elif self.value > value:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            print("같은 노드가 있습니다.")

    def delete(self, value):
        if self.value < value:
            self.right = self.right.delete(value)
        elif self.value > value:
            self.left = self.left.delete(value)
        # self.value == vlaue
        else:
            # 자식 노드가 0개인 경우
            if self.left == None and self.right == None:
                return None
            # 자식 노드가 1개인 경우
            # 왼쪽 자식
            elif self.left != None and self.right == None:
                return self.left
            # 오른쪽 자식
            elif self.left == None and self.right != None:
                return self.right
            # 자식 노드가 2개인 경우
            else:
                # tmp = Node(self.right.get_min_node())
                tmp = self.right.get_min_node()
                # print(f'tmp:{tmp}')
                # print(type(tmp))
                self.value = tmp
                # tmp 삭제
                self.right = self.right.delete(tmp)

        return self

    # 최솟값을 가지고 있는 노드 찾기
    def get_min_node(self):
        if self.left != None:
            return self.left.get_min_node() # 재귀 호출된 함수의 반환 값을 상위 호출자에게 반환
        else:
            return self.value
        
    # 중위순회
    def inorder(self):
        if self.left != None:
            self.left.inorder()
        print(self.value, end = "->")
        if self.right != None:
            self.right.inorder()

root = Node(10)
root.insert(13)
root.insert(0)
root.insert(14)
root.insert(1)
root.insert(11)

root.inorder()
print()

root.delete(10)
root.inorder()