n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    idx, val = map(int, input().split())
    graph[idx].append(val)
    graph[val].append(idx)
    
    
def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    

dfs(graph, 1, visited)
print(sum(visited) - 1)
