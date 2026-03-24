class Node:
    def __init__ (self, elem, link=None):
        self.data = elem #데이터 멤버 생성 및 초기화
        self.link = link #링크 생성 및 초기화

    #self 다음에 node를 넣는 연산
    def append(self, node):
        if node is not None:
            node.link = self.link
            self.link = node

    def popNext(self):
        next = self.link
        if next is not None:
            self.link = next.link
        return next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False
    
    def getNode(self, pos):
        if pos < 0:
            return None #잘못된 위치
        
        #머리 노드에서부터 링크를 따라 pos번 이동하면 pos위치의 노드에 도착
        #위치는 0부터 시작한다고 가정함
        ptr = self.head
        for i in range(pos):
            if ptr == None: 
                return None
            ptr = ptr.link
        return ptr
    
    def getEntry(self, pos):
        node = self.getNode(pos) #pos 번째 노드를 구함
        if node == None: #해당 노드가 없는 경우
            return None
        
        return node.data #있는 경우 필드 반환

    def insert(self, pos, e):
        node = Node(e, None)
        before = self.getNode(pos - 1)

        if before == None: #리스트 맨 앞에 추가하는 경우
            node.link = self.head #self.head는 포인터임, 노드 아님
            self.head = node

        else:
            before.append(node) #아닌 경우 before 뒤에 추가

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None: #머리 노드를 삭제하려는 경우
            before = self.head #삭제하려는 머리 노드 저장
            if self.head is not None:
                self.head = self.head.link #헤드포인터는 삭제하려는 머리 노드가 가리키던걸 가리킴
            return before
        else:
            return before.popNext()
        
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count += 1
        return count
    
    def display(self, msg='LinkedList: '):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='->')
            ptr = ptr.link
        print('None')
        

s = LinkedList()
s.display('연결리스트(초기): ')
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display("연결리스트(삽입X5): ")
s.delete(2)
s.delete(3)
s.delete(0)
s.display("연결리스트(삭제X3): ")


l = []
print('파이썬list(초기): ', l)
l.insert(0, 10)
l.insert(0, 20)
l.insert(1, 30)
l.insert(len(l), 40)
l.insert(2, 50)
print('파이썬list(삽입X5): ', l)
l.pop(2)
l.pop(3)
l.pop(0)
print('파이썬list(삭제X3): ', l)