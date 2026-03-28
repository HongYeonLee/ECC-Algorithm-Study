import collections #덱 사용하기 위해 임포트

n, m = map(int, input().split()) #덱의 크기 n과 뽑아내려는 수의 개수 m 입력받음

dq = collections.deque(range(1, n+1))#덱 생성, 1부터 n까지의 수를 담아서 덱 생성, 빈 상태로 만들면 pop연산 불가
numbers = list(map(int, input().split()))# 뽑을 숫자들을 담은 리스트, 여기서는 편의를 위해 원소의 위치 = 원소의 값으로 설정함
count = 0

for num in numbers: #예를 들어서 2, 9, 5라는 값을 nubmers에 받았다면
    mid = len(dq)//2 #회전 방향을 정하기 위해 중앙값을 구함

    if dq[0] == num: #가장 첫번째 원소가 뽑으려는 값인 경우
        dq.popleft()
        continue

    if dq.index(num) <= mid: #뽑으려는 값이 중앙보다 왼쪽에 있다면 왼쪽 회전
        while dq[0] != num: #뽑으려는 값이 첫번째 원소가 될 때까지 왼쪽 회전
            dq.rotate(-1) #왼쪽 회전
            count += 1 #2번 연산 횟수 증가
        dq.popleft()
    else:
        while dq[0] != num:
            dq.rotate(1)
            count += 1
        dq.popleft()   

print(count)     

