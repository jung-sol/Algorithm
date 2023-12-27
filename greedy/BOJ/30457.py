n = int(input())
data = list(map(int, input().split()))

data.sort()
result = {}

for i in data:
  result[i] = min(2, result.get(i, 0) + 1)

print(sum(result.values()))
