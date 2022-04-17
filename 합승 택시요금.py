import heapq
graph = []
L =0

def solution(n, s, a, b, fares):
    global graph
    global L
    L =n
    graph = [[-1]*(n+1) for _ in range(n+1)]
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]

    cost = shortest_path(s, a) + shortest_path(s, b)

    for i in range(1, n+1):
        if s!=i:
            cost = min(cost, shortest_path(i, a) + shortest_path(i, b) + shortest_path(s, i))
    return cost

def shortest_path(a, b):
    D = {v: float('inf') for v in range(L+1)}
    visited = set()

    q = []
    heapq.heappush(q, [0, a])
    D[a] = 0

    while q:
        x, cur = heapq.heappop(q)
        visited.add(cur)

        for nei in range(len(graph[cur])):
            if graph[cur][nei] == -1:
                continue
            if nei not in visited:
                old_dist = D[nei]
                new_dist = D[cur] + graph[cur][nei]
                if new_dist < old_dist:
                    heapq.heappush(q, [new_dist, nei])
                    D[nei] = new_dist
    return D[b]

fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

print(solution(6,4,6,2, fares))
