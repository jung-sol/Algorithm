cnt = 0
data = []

n = int(input())

for _ in range(n):
  data.append(int(input()))

for i in range(n - 1, 0, -1):
  while data[i] <= data[i - 1]:
    data[i - 1] -= 1
    cnt += 1

print(cnt)
