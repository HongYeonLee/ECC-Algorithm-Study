import collections

n = int(input()) #풍선의 개수 입력받기
index = collections.deque(range(1, n + 1)) #풍선의 번호를 담은 덱
paper = collections.deque(list(map(int, input().split()))) #풍선안에 있는 종이(회전 수)를 담은 덱
result = []


#종이 리스트와 풍선 번호 리스트를 회전시키면서 맨 왼쪽에 있는 값을 pop한다.
while(paper): 
    i = index.popleft() # 풍선의 번호 덱에서 맨 왼쪽에 위치한 값을 pop한다. 맨 왼쪽에 있는 풍선 터뜨리기
    move = paper.popleft() # 풍선에 적힌 숫자도 꺼내서 얼만큼 회전 시켜야하는지 담는다
    result.append(i)

    if move > 0: #현재 위치에서 오른쪽에 있는 풍선을 터뜨려야 한다면
        index.rotate(-(move - 1)) #풍선들을 왼쪽으로 밀기(음수값), popLeft하면서 이미 한번 밀었으므로 한번 덜 밀음
        paper.rotate(-(move - 1))
    else: #현재 위치에서 왼쪽에 있는 풍선을 터뜨려야 한다면
        index.rotate(-move) #풍선을 오른쪽으로 밀기(양수값)
        paper.rotate(-move)

print(" ".join(map(str, result)))
        
