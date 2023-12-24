a, b, c = map(int, input().split())
i = 0

while True:
  i += 1
  if i == c:
    break
  a += b

print(a)
