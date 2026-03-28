import collections

n, k = map(int, input().split())
s = []
dq = collections.deque()
result = []
for i in range(k):
    num, char = input().split()
    s.append((int(num), char))

for i in range(n):
    dq.append('?')

for num, char in s:
    dq.rotate(num)
    if dq[0] == '?':
        dq[0] = char
    elif dq[0] == char:
        continue
    else:
        result = '!'
        break
    result = dq

seen = set()

for char in dq:
    if char in seen and char != '?':
        result = '!'
        break
    else:
        seen.add(char)
    

print("".join(result))