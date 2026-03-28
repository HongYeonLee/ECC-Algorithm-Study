import collections

n = int(input()) #풍선의 개수 입력받기
index = collections.deque(range(1, n + 1)) #풍선의 위치를 담은 덱
paper = collections.deque(list(map(int, input().split()))) #풍선안에 있는 종이(뽑을 위치)를 담을 덱
result = []

while(paper):
    i = index.popleft()
    move = paper.popleft()
    result.append(i)

    if move > 0: #현재 위치에서 오른쪽에 있는 풍선을 터뜨려야 한다면
        index.rotate(-(move - 1)) #풍선들을 왼쪽으로 밀기(음수값), popLeft하면서 이미 한번 밀었으므로 한번 덜 밀음
        paper.rotate(-(move - 1))
    else: #현재 위치에서 왼쪽에 있는 풍선을 터뜨려야 한다면
        index.rotate(-move) #풍선을 오른쪽으로 밀기(양수값)
        paper.rotate(-move)

print(" ".join(map(str, result)))
        
