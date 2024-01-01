n = int(input())

queue = list(range(1, n + 1))
data = []

while len(queue) > 1:
    data.append(queue.pop(0))
    queue.append(queue.pop(0))

data.append(queue.pop(0))

for d in data:
    print(d, end=' ')
