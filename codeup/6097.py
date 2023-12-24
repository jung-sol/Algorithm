h, w = map(int, input().split())
list = d = [[0 for j in range(w)] for i in range(h)]

n = int(input())
for _ in range(n):
  l, d, x, y = map(int, input().split())
  for i in range(l):
    if d == 1:  #   가로 = 0
      list[x - 1 + i][y - 1] = 1
    else:
      list[x - 1][y - 1 + i] = 1

for i in range(len(list)):
  for j in range(len(list[0])):
    print(list[i][j], end=' ')
  print()
