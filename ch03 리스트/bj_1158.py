import collections #덱 사용을 위해 콜렉션 임포트

n, k = map(int, input().split()) #덱의 크기 n와 뽑을 자리 k를 받음

dq = collections.deque(range(1, n+1)) #덱을 1부터 n까지의 숫자로 채움
result = [] #요세푸스 순열을 담을 리스트
index = -1
for i in range(n):
    index = (k + index) % len(dq)
    result = dq.pop(index)

print(result)


