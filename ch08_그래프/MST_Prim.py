INF = 999
def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        #MST에 포함되지 않은 정점 중에서 최소 dist를 갖는 정점의 인덱스 minv를 구한다
        if selected[v] == False and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj): #여기서 인접행렬은 가중치값을 기록한다. 정점 간 간선이 없으면 INF로 초기화
    n = len(vertex)
    dist = [INF] * n
    dist[0] = 0 #시작 정점만 거리가 0
    selected = [False] * n

    for _ in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')

        for v in range(n):
            if adj[u][v] != INF and not selected[v]: #간선 (u, v)가 있고 v가 MST에 포함되지 않았다면
                if adj[u][v] < dist[v]: #간선 (u, v)의 가중치 값이 dist[v]보다 작다면
                    dist[v] = adj[u][v]
        
        print(': ', dist)

vertex = ("A", "B", "C", "D", "E", "F", "G")
adj = [[0, 25, INF, 12, INF, INF, INF],
       [25, 0, 10, INF, 15, INF, INF],
       [INF, 10, 0, INF, INF, INF, 16],
       [12, INF, INF, 0, 17, 37, INF],
       [INF, 15, INF, 17, 0, 19, 14],
       [INF, INF, INF, 37, 19, 0, 42],
       [INF, INF, 16, INF, 14, 42, 0]
       ]

MSTPrim(vertex, adj)