from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

for _ in range(m):
    idx, val = map(int, input().split())
    graph[idx].append(val)
    graph[val].append(idx)
    
for i in graph:
    i.sort()
    
dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)
