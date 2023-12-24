list = d = [[0 for j in range(19)] for i in range(19)]

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    list[a - 1][b - 1] = 1

for i in range(len(list)):
  for j in range(len(list[i])):
    print(list[i][j], end = " ")
  print()
