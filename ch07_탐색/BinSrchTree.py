from ch04_트리.BinaryTree import preorder


class BSTNode: #이진 탐색 트리를 위한 노드 클래스
    def __init__(self, key, value): #생성자, 탐색을 위한 키와 데이터의 값을 받음
        self.key = key
        self.value = value
        self.left = None #왼쪽 자식에 대한 링크
        self.right = None #오른쪽 자식에 대한 링크

#n을 루트로 갖는 이진 탐색 트리에서 키값이 key인 노드를 찾는 순환 함수
def search_bst(n, key): 
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key) #탐색키가 루트노드의 key값 보다 짝으면 왼쪽 서브트리 탐색
    else:
        return search_bst(n.right, key)
    
#n을 루트로 갖는 이진 탐색 트리에서 키가 아니라 값으로 노드를 찾는 함수, 전위 순회 이용
def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value:
        return n
    
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)

def insert_bst(root, node):
    if root == None: #공백노드에 도달하면 이 위치에 삽입
        return node #node를 반환, (이 노드가 현재 root 위치에 감)
    if node.key == root.key: #동일한 키는 허용하지 않음
        return root #루트를 반환, root는 변화 없음
    
    #root의 서브트리에 node 삽입
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    
    else:
        root.right = insert_bst(root.right, node)
    
    return root


def delete_bst(root, key):
    if root == None:
        return root
    
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    #key가 루트의 키와 같으면 root 삭제
    else:
        #단말 노드 또는 오른쪽 자식만 있는 경우
        if root.left == None:
            return root.right #오른쪽 자식을 끌어올림
        
        #왼쪽 자식만 있는 경우
        if root.right == None:
            return root.left
        #두 자식이 모두 있는 경우
        succ = root.right
        while succ.left != None:
            succ = succ.left #후계자를 찾고, 후계자의 데이터 복사
        
        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)
    
    return root

def print_node(msg, n):
    print(msg, n if n != None else "탐색실패")

def print_tree(msg, r):
    print(msg, end="")
    preorder(r)
    print()

data = [(6, "여섯"), (8, "여덟"), (2, "둘"), (4, "넷"), (7, "일곱"),
        (5, "다섯"), (1, "하나"), (9, "아홉"), (3, "셋"), (0, "영")]

root = None
for i in range(0, len(data)):
    root = insert_bst(root, BSTNode(data[i][0]), data[i][1])

print_tree("최초: ", root)

n = search_bst(root, 3)
print_node("srch 3: ", n)