class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root: Node = None # Node 타입

    def search(self, value):
        # 트리가 비어있는 경우
        if self.root == None:
            return None
        # 트리가 비어있지 않은 경우
        cur_node = self.root
        while cur_node != None:
            if cur_node.value < value:
                cur_node = cur_node.right
            elif cur_node.value > value:
                cur_node = cur_node.left
            else:
                return cur_node
        # 찾지 못한 경우
        return None

    def insert(self, value):
        # 트리가 비어있는 경우
        if self.root == None:
            self.root = Node(value)
            return
        # 트리가 비어있지 않은 경우
        cur_node = self.root
        while True:
            # cur_node.value < value
            if cur_node.value < value:
                if cur_node.right == None:
                    cur_node.right = Node(value)    # 새로운 노드 할당
                    break
                else:
                    # cur_node 이동
                    cur_node = cur_node.right
            # cur_node.value > value
            elif cur_node.value > value:
                if cur_node.left == None:
                    cur_node.left = Node(value)     # 새로운 노드 할당
                    break
                else:
                    # cur_node 이동
                    cur_node = cur_node.left
            
            # cur_node.value == value
            else:
                print("중복 발생 ..")
                break

    def delete(self, value):
        # 트리가 비어있을 때
        if self.root == None:
            print("트리가 비어있음..")
            return None
        # 트리가 비어있지 않은 경우
        cur_node = self.root
        parent_node = None
        while cur_node.value != value:
            # cur_node.value < value
            if cur_node.value < value:
                if cur_node.right != None:
                    parent_node = cur_node
                    cur_node = cur_node.right
                else:
                    print("value가 트리 안에 없습니다.")
                    break
            # cur_node.value > value
            elif cur_node.value > value:
                if cur_node.left != None:
                    parent_node = cur_node
                    cur_node = cur_node.left
                else:
                    print("value가 트리 안에 없습니다.")
                    break
        # value를 찾으면
        # 자식이 0개 있을 때
        if cur_node.left == None and cur_node.right == None:
            if parent_node.value < value:
                parent_node.right = None
            elif parent_node.value > value:
                parent_node.left = None
        # 자식이 1개 있을 때
        # 왼쪽
        elif cur_node.left != None and cur_node.right == None:
            if parent_node.value < value:
                parent_node.right = cur_node.left
            elif parent_node.value > value:
                parent_node.left = cur_node.left
        # 오른쪽
        elif cur_node.left == None and cur_node.right != None:
            if parent_node.value < value:
                parent_node.right = cur_node.right
            elif parent_node.value > value:
                parent_node.left = cur_node.right
        # 자식이 2개 있을 때
        else:
            # 1. 왼쪽 서브트리에서 max node 찾기
            max_node = self.find_max_node(cur_node.left) # 왼쪽 서브트리에서 가장 큰 값을 가진 노드 찾기
            # 2. 값 변경
            cur_node.value = max_node.value 
            # 3. max값 삭제
            self.delete(max_node.value)

    def find_max_node(self):
        cur_node = self.root
        while cur_node.right != None:
            cur_node = cur_node.right

    def inorder(self, cur_node = None):
        # 첫번째 호출
        if cur_node == None:
            cur_node = self.root
        else:
            self.inorder(cur_node.left)
            print(cur_node.value, end = " -> ")
            self.inorder(cur_node.right)

bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(1)
bst.insert(2)
bst.insert(5)

bst.inorder(bst.root)
print()

bst.delete(1)
bst.inorder(bst.root)
print()

bst.insert(0)
bst.inorder(bst.root)
