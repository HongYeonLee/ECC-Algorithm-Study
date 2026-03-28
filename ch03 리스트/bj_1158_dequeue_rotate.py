import collections

n, k = map(int, input().split()) #덱의 크기와 뽑아야 하는 위치 k를 받음
dq = collections.deque(range(1, n+1)) #1 ~ n까지의 수로 채운 덱 생성
result = []

#뽑아야 하는 수가 맨 왼쪽 앞으로 와야 하므로 k - 1번씩 왼쪽으로 밀면된다
for i in range(n): #총 n번 뽑아야 하므로 n번 반복
    dq.rotate(-(k - 1)) #왼쪽으로 밀어야 하므로 음수값을 넣어야 함
    result.append(dq.popleft())

print("<" + ", ".join(map(str, result)) + ">")