import collections

n, k = map(int, input().split())
dq = collections.deque(range(1, n+1))
result = []

while (n > 0):
    for _ in range(k - 1):
        dq.append(dq.popleft()) #뽑을 자리의 수가 맨 앞으로 오게끔 앞에 있는 수를 뒤로 보내서 붙이기
    
    result.append(dq.popleft())
    n -= 1

print("<" + ", ".join(map(str, result)) + ">")