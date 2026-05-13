def ST_DFS(vtx, adj, s, visited):
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                print("(", vtx[s], vtx[v], ")", end="") #(A, B)는 간선 표현 방법
                ST_DFS(vtx, adj, v, visited)

from queue import Queue
def ST_BFS(vtx, aList, s):
    n = len(vtx)
    visited = [False]*n

    Q = Queue()
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        s = Q.get()
        
        for v in aList[s]:
            if visited[v] == False:
                Q.put(v)
                print("(", vtx[s], vtx[v], ")", end="")
                visited[v] = True

vtx = ['U', 'V', 'W', 'X', 'Y']
edge = [[0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0]]
print('ST_DFS(시작:U): ', end='')
ST_DFS(vtx, edge, 0, [False]*len(vtx))
print()

aList = [[1, 2],
         [0, 2, 3],
         [0, 1, 4],
         [1],
         [2]]

print("ST_BFS(시작:U): ", end="")
ST_BFS(vtx, aList, 0)
print()