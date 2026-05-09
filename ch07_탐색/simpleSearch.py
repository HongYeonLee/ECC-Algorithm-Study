def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key: #탐색 성공
            if i > low: #맨 처음 요소가 아닐 경우
                A[i], A[i-1] = A[i-1], A[i] #교환하기 (자기 구성 리스트)
                i = i - 1
            return i
    return -1 #탐색 실패

#재귀로 이진 탐색 구현
def binary_search(A, key, low, high):
    if (low <= high): #항목들이 남아 있으면 (종료조건)
        middle = (low + high) // 2 #파이썬에서 /의 결과는 실수, //은 정수
        if key == A[middle]:
            return middle
        elif (key < A[middle]):
            return binary_search(A, key, low, middle - 1)
        else:
            return binary_search(A, key, middle + 1, high)
    return -1

#반복으로 이진 탐색 구현
def binary_search_iter(A, key, low, high):
    while(low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif (key > A[middle]):
            low = middle + 1
        else:
            high = middle - 1
    return -1
