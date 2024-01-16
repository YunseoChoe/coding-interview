class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.root: Node = None 

    def search(self, value):
        # 트리가 비어있는 경우
        if self.root == None:
            print("트리가 비어있습니다.")
            return None
        # 트리가 비어있지 않은 경우
        cur_node = self.root
        while True:
            # cur_node.value < value
            if cur_node.value < value:
                cur_node = cur_node.right
            # cur_node.value > value
            elif cur_node.value > value:
                cur_node = cur_node.left
            # cur_node.value == value
            elif cur_node.value == value:
                return value
            else:
                print("vatlue가 트리 안에 없습니다.")
                break

    def insert(self, value):
        # 트리가 비어있다면
        if self.root == None:
            self.root = Node(value)
            return
        # 트리가 비어있지 않다면
        cur_node = self.root
        while True:
            # cur_node.value < value
            if cur_node.value < value:
                if cur_node.right != None:
                    cur_node = cur_node.right
                else:
                    break
            # cur_node.value > value
            elif cur_node.value > value:
                if cur_node.left != None:
                    cur_node = cur_node.left
                else:
                    break
            # cur_node.value == value
            else:
                print("중복 발생...")
                break
            
        if cur_node.value < value:
            cur_node.right = Node(value)
        elif cur_node.value > value:
            cur_node.left = Node(value)


    def delete(self, value):
        # 트리가 비어있는 경우
        if self.root == None:
            print("트리가 비어있습니다.")
        # 트리가 비어있지 않은 경우
        

    def inorder(self):
        pass








