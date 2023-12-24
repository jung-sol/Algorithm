array = []

for _ in range(10):
    array.append(list(map(int, input().split())))

x, y = 1, 1

while True:
  array[x][y] = 9
  if array[x][y + 1] == 0:
    y += 1
  elif array[x + 1][y] == 0:
    x += 1
  else:
    if array[x][y + 1] == 2:
      array[x][y + 1] = 9
    elif array[x + 1][y] == 2:
      array[x + 1][y] = 9
    break
    
for i in range(len(array)):
  for j in range(len(array[i])):
    print(array[i][j], end = ' ')
  print()
