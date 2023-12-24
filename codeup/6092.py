n = int(input())
c = list(map(int, input().split()))

list = [0] * 23

for i in range(len(c)):
  list[c[i] - 1] += 1

for i in range(len(list)):
  print(list[i], end = ' ')
