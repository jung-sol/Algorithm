n = int(input())

for i in range(1, n+1):
  x = i % 10
  if x in (3, 6, 9):
    print('X', end=' ')
  else:
    print(i, end=' ')
