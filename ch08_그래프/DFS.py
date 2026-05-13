def DFS(vtx, adj, s, visited): #정점 집함, 인접 행렬, 시작 정점, 방문 여부 기록 배열
    print(vtx[s], end=" ")
    visited[s] = True #시작 정점은 방문 처리
    
    for v in range(len(vtx)): #0번, 1번, 2번...
        if adj[s][v] != 0: #시작 정점과 정점 v간의 간선이 있고
            if visited[v] == False: #정점 v를 방문한 적 없으면
                DFS(vtx, adj, v, visited) #정점 v를 시작 정점으로 해서 시스템 스택 이용

vtx = ['U', 'V', 'W', 'X', 'Y']
edge = [[0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0]]
print('DFS (시작:U) : ', end='')
DFS(vtx, edge, 0, [False]*len(vtx))
print()
