from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    idx, val = map(int, input().split())
    graph[idx].append(val)
    graph[val].append(idx)

queue = deque([1])
visited[1] = True

while queue:
    v = queue.popleft()
    
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            
print(sum(visited) - 1)
