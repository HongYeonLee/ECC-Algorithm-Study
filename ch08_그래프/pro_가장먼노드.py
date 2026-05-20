import collections

def makeAdjList(n, edges):
    adj = [[] for _ in range(n)] #인접 리스트, 0 ~ 5행

    #인접 리스트 만들기
    for e in edges: #[3, 6]
        # 리스트 인덱스 범위 초과때문에 -1해서 넣음
        adj[e[0] - 1].append(e[1] - 1) #3행(3번 노드)의 인접 노드는 6번 노드
        adj[e[1] - 1].append(e[0] - 1) #6행(6번 노드)의 인접 노드는 3번 노드
    
    return adj

def solution(n, edges):
    adj = makeAdjList(n, edges) #각 노드의 인접노드를 행 별로 가지고 있는 인접리스트

    #BFS
    dq = collections.deque()
    dist = [-1] * n #1번 노드로부터의 각 노드까지의 거리를 담은 리스트

    #시작 노드 큐에 넣고 pop -> 인접한 노드들 push, 인접한 노드와 1번 노드까지의 거리 업데이트
    dq.append(0)
    dist[0] = 0 #시작노드와 시작노드까지의 거리는 0
    while dq: #큐가 공백이 될 때까지
        node = dq.popleft()
        for i in adj[node]: #현재 보고있는 노드들의 인접 노드를 돌음
            if dist[i] == -1: #해당 인접 노드를 방문한 적 없다면
                dq.append(i) #큐에 해당 인접 노드를 넣는다
                dist[i] = dist[node] + 1 #해당 노드에서 1번 노드까지의 거리는 지금 보고있는 노드까지의 거리 + 1 (지금 보는 노드의 인접 노드이므로)
    
    answer = 0
    for i in range(len(dist)):
        if dist[i] == max(dist):
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
