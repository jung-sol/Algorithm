n = int(input())
result = [1] * n
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            result[i] += 1

for i in result:
    print(i, end=' ')
