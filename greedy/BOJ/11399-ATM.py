n = int(input())
data = list(map(int, input().split()))
sum = 0

data.sort()

for i in range(n):
  sum += data.pop() * (i + 1)

print(sum)
