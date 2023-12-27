n = int(input())
data = []
result = 0

for _ in range(n):
  _, *t = list(map(int, input().split()))
  data.append(sum(t))

data.sort()

for i in range(n):
  result += data[i] * (n - i)

print(result)
