a, b, c, d = map(int, input().split())
i = 0

while True:
  i += 1
  if i == d:
    break
  a = a * b + c

print(a)
