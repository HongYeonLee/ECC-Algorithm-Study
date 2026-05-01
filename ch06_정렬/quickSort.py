def quick_sort(A, left, right):
    if (left < right): #정렬 범위가 2개 이상인 경우
        q = partition(A, left, right) #피벗을 중심으로 리스트의 두 부분을 분할
        quick_sort(A, left, q -1) #분할된 리스트의 왼쪽 정렬
        quick_sort(A, q + 1, right) #분할된 리스트의 오른쪽 정렬

def partition(A, left, right):
    pivot = A[left]
    low = left + 1
    high = right

    while (low < high): #low와 high이 역전되지 않는 한 반복
        while low <= right and A[low] <= pivot:
            low += 1 #A[low] <= 피벗이면 low를 오른쪽으로 진행
        while high >= left and A[high] > pivot:
            high -= 1 #A[high] > 피벗이면 high을 왼쪽으로 진행
        
        if low < high: #역전이 아니면 두 레코드 교환
            A[low], A[high] = A[high], A[low]
    
    #마지막으로 피벗과 high을 교환하고 피벗의 인덱스 high을 리턴
    A[left], A[high] = A[high], A[left]
    return high

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

print("Original : ", data)
quick_sort(data, 0, len(data) - 1)
print("QuickSort : ", data)