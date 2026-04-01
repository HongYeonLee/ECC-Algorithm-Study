class ArrayQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None]*capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        # 삽입 후가 공백 상태라는건 front가 rear가 같은 곳을 가리키고 있는 완전 포화 상태
        # 이때 front를 하나 증가시키면 가장 오래된 데이터가 삭제된다
        if self.isEmpty(): 
            self.front = (self.front + 1) % self.capacity

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            pass
    
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
    
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def display(self, msg):
        print(msg, end='= [')
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i % self.capacity], end=' ')
        print(']')

import random #난수 발생을 위해 random 모듈 임포트

if __name__ == "__main__":
    q = ArrayQueue(8) # 용량이 8이므로 실제 데이터 삽입 개수는 7개

    q.display('초기 상태')
    for i in range(6):
        q.enqueue(i)
    q.display('삽입 0 - 5')

    q.enqueue(6); q.enqueue(7)
    q.display("삽입 6, 7") #큐는 이제 포화 상태
    
    q.enqueue(8); q.enqueue(9) #삽입 후 가장 오래된 데이터 삭제
    q.display("삽입 8, 9")

    q.dequeue(); q.dequeue()
    q.display("삭제 x 2")