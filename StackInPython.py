s1 = list()

msg = input("문자열 입력1: ")
for c in msg:
    s1.append(c)

print("문자열 출력1: ", end='')

while(len(s1) > 0):
    print(s1.pop(), end='')

print()

import queue

s2 = queue.LifoQueue(maxsize=100)

msg2 = input("문자열 입력2: ")
for c in msg2:
    s2.put(c)

print("문자열 출력2: ", end='')
while not s2.empty():
    print(s2.get(), end='')

print()