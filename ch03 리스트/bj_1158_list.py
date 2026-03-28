n, k = map(int, input().split()) #덱의 크기 n와 뽑을 자리 k를 받음

li = list(range(1, n+1)) #인덱스로 접근하기 위해 리스트를 사용, 1부터 n까지의 숫자로 채움
result = [] #요세푸스 순열을 담을 리스트
index = 0 #원에서 뽑을 자리

for i in range(n):
    #인덱스는 매번 뽑을 자리 k만큼 이동하므로 매번 k만큼 인덱스 값을 증가시킨다.
    #뽑는 순간 리스트의 크기가 1 줄어들면서 요소들이 앞으로 한 칸씩 이동하므로
    #다음번 뽑을 위치는 현재 위치에서 +k한 위치가 아니라 +(k - 1)한 위치가 된다
    #또한 인덱스가 리스트의 길이를 넘어가는 것을 방지하기 위해 리스트의 길이로 나누어준다
    index = (k - 1 + index) % len(li) 
    result.append(li.pop(index))

print("<" + ", ".join(map(str, result)) + ">")