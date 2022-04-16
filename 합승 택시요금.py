from collections import deque
def solution(n, s, a, b, fares):
    answer = 0
    graph = [[-1]*n+1 for _ in range(n+1)]

    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]

    apaths = []
    bpaths = []
    def findPaths(path, node):
        if node == a:
            apaths.append(path)
        if node == b:
            bpaths.append(path)

        for i in range(n+1):
            if graph[node][i] > -1:
                findPaths(path + i, i)

    return answer

graph = []
visited = {}
def shortest_path(n, fares, a, b):
    global graph
    global visited
    graph = [[-1]*(n+1) for _ in range(n+1)]

    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]

    q = deque()
    q.append(a)
    visited[a] = 0

    while q:
        cur = q.popleft()

        for nei in to_visit(cur):
            if nei not in visited:
                visited[nei] = visited[cur] + graph[cur][nei]
                q.append(nei)
            else:
                if visited[cur] + graph[cur][nei] < visited[nei]:
                    visited[nei] = visited[cur] + graph[cur][nei]
                    q.append(nei)

    return visited[b]

def to_visit(a):
    res = []
    for i in range(len(graph[a])):
        if graph[a][i] != -1:
            res.append(i)
    return res

fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(shortest_path(6, fares, 4, 3))
# print(solution(6,4,6,2, fares))
