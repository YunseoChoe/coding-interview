class Node:
    def __init__(self, value):
        self.value: int = value
        self.left: Node = None
        self.right: Node = None

class BST:
    def __init__(self):
        self.root: Node = None
    
    def search(self, node: Node, value: int) -> bool:
        if node == None:
            return False
        if node.value < value:
            return self.search(node.right, value)
        elif node.value > value:
            return self.search(node.left, value)
        else:
            return True

    def insert(self, value: int):
        self.root = self._insert(self.root, value)

    def _insert(self, node: Node, value: int) -> Node:
        # node가 비었을 때
        if node == None:
            node = Node(value)
        elif node.value < value:
            node.right = self._insert(node.right, value)
        elif node.value > value:
            node.left = self._insert(node.left, value)
        return node
    
    def delete(self, value: int):
        self.root = self._delete(self.root, value)

    def _delete(self, node: Node, value) -> Node:
        if node == None:
            print("값이 없습니다.")
        if node.value < value:
            node.right = self._delete(node.right, value)
        elif node.value > value:
            node.left = self._delete(node.left, value)
        else:
            # 자식이 없을 때
            if node.right == None and node.left == None:
                return None
            # 자식이 1개 있을 때 (오른쪽 자식만 있음)
            elif node.right != None and node.left == None:
                return node.right
            # 자식이 1개 있을 때 (왼쪽 자식만 있음)
            elif node.right == None and node.left != None:
                return node.left
            # 자식이 2개 있을 때
            tmp = node.right
            while tmp.left != None:
                tmp = tmp.left
            node.value = tmp.value
            node.right = self._delete(node.right, tmp.value)
        return node
    
    def inorder(self, node: Node):
        if node == None:
            return
        else:
            self.inorder(node.left)
            print(node.value, end = "->")
            self.inorder(node.right)



bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(8)
bst.insert(9)

bst.inorder(bst.root)
# print(bst.root.value) # 5
# bst.inorder(bst.root)
print()
# bst.root = bst.delete(bst.root, 5)
# bst.root = bst.delete(bst.root, 3)
# bst.root = bst.delete(bst.root, 8)
bst.delete(5)
bst.delete(3)
bst.delete(8)

bst.inorder(bst.root)


# bst.search(bst.root, 0)
# bst.search(bst.root, 10)
# bst.search(bst.root, 3)




