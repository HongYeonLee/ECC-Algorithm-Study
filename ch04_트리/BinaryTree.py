import sys
import os

# 현재 파일의 부모의 부모 폴더(ECC-Algorithm-Study)를 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ch02_큐.ArrayQueue import ArrayQueue

class BTNode:
    def __init__ (self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

    def isLeaf(self): #단말 노드인지 확인하는 함수
        return self.left is None and self.right is None
    

#전위 순회
def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left) #왼쪽 서브 트리 처리
        preorder(n.right) #오른쪽 서브 트리 처리

#중위 순회
def inorder(n): 
    if n is not None:
        inorder(n.left) #왼쪽 서브 트리 처리
        print(n.data, end=' ')
        inorder(n.right) #오른쪽 서브 트리 처리

#후위 순회
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

#레벨 순회
def levelorder(root) :
    queue = ArrayQueue() #큐 객체 초기화
    queue.enqueue(root) #최초에 루트 노드만 들어있음
    while not queue.isEmpty(): #큐가 공백 상태가 아닌 동안
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

#전체 노드의 수 구하기
def count_node(n):
    if n is None:
        return 0
    else:
        return count_node(n.left) + count_node(n.right) + 1
    
#트리의 높이 구하기
def calc_height(n) :
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)

    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1
    
#테스트 코드
d = BTNode('D', None, None)
e = BTNode('E', None, None)
b = BTNode('B', d, e)
f = BTNode('F', None, None)
c = BTNode('C', f, None)
root = BTNode('A', b, c)

print('\n In-Order: ', end=' '); inorder(root)
print('\n Pre-Order: ', end=' '); preorder(root)
print('\n Post-Order: ', end=' '); postorder(root)
print('\n Level-Order: ', end=' '); levelorder(root)
print()

print(" 노드의 개수 = %d개" %count_node(root))
print(" 트리의 높이 = %d개" %calc_height(root))
