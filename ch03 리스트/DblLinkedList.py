class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next
    
    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
            self.next = node
    
    def popNext(self):
        node = self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node
    
class DblLinkedList():
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False

    def getEntry(self, pos):
        node = self.getNode(pos) #pos 번째 노드를 구함
        if node == None: #해당 노드가 없는 경우
            return None
    
    def getNode(self, pos):
        if pos < 0:
            return None #잘못된 위치
        
        #머리 노드에서부터 링크를 따라 pos번 이동하면 pos위치의 노드에 도착
        #위치는 0부터 시작한다고 가정함
        ptr = self.head
        for i in range(pos):
            if ptr == None: 
                return None
            ptr = ptr.next
        return ptr

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.next
            count += 1
        return count
    
    def display(self, msg='DblLinkedList: '):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='<=>')
            ptr = ptr.next
        print('None')

    def insert(self, pos, e):
        node = DNode(e)
        before = self.getNode(pos - 1) #삽입할 위치 이전 노드 탐색
        if before == None:
            #node의 다음 노드가 현재 head가 되고,
            #그 노드의 prev를 node로 수정하며,
            #마지막으로 머리 노드 head를 node로 변경
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
            self.head = node
        else:
            before.append(node)

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None: #머리 노드 삭제일 경우
            before = self.head
            if self.head is not None:
                self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return before
        else:
            before.popNext()
        

s = DblLinkedList()
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
