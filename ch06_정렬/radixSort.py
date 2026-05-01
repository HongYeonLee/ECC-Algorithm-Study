from collections import deque

def radix_sort(A):
    queues = [] #버킷을 담을 리스트
    for i in range(BUCKETS): #버킷개의 큐를 만들어 버킷리스트에 추가
        queues.append(deque())
    
    n = len(A)
    factor = 1 #가장 낮은 자릿수부터 시작
    for d in range(DIGITS): #각 자릿수에 대해 처리
        for i in range(n): #모든 항목을 큐에 삽입
            queues[(A[i]//factor) % BUCKETS].append(A[i])
            
        #0번부터 모든 버킷에 저장된 요소를 순서대로 꺼내 입력리스트 A에 다시 저장
        i = 0
        for b in range(BUCKETS):
            while queues[b]:
                A[i] = queues[b].popleft()
                i += 1

        factor *= BUCKETS #그 다음 자릿수로 이동
        print("step", d+1, A)

import random
BUCKETS = 10
DIGITS = 4

data = [random.randint(1, 9999) for _ in range(10)]
radix_sort(data)
print("Radix: ", data)
