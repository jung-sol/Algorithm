n, l = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
for i in range(n):
  if data[i] <= l:
    l += 1
    continue

print(l)
