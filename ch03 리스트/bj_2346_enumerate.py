import collections

n = int(input())
paper = list(map(int, input().split())) #풍선 안의 종이에 적힌 수를 받음
#덱에 풍선의 위치(인덱스)와 풍선의 종이에 적힌 수를 튜플 형태로 저장함
# ex) ([(1, 3), (2, 2), (3, 1), (4, -3), (5, -1)])
dq = collections.deque((i, p) for i, p in enumerate(paper, start=1)) #start=1은 인덱스를 1부터 시작하라는 의미
result = []

while (dq):
    index, move = dq.popleft() #풍선의 번호(인덱스)와 몇 번 회전해야 하는지 받음
    result.append(index)

    if move > 0: #뽑아야 하는 위치가 현재 위치에서 오른쪽으로 가야한다면, 덱을 왼쪽 회전
        dq.rotate(-(move - 1)) #왼쪽 회전은 음수값, 처음에 popLeft를 하면서 한 칸 왼쪽으로 움직였으므로 한 칸 덜 움직임
    
    else:
        dq.rotate(-(move)) #오른쪽 회전은 양수값

print(" ".join(map(str, result)))
