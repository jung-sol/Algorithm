list = list(map(int, input().split()))
d = max(list)

while d%list[0]!=0 or d%list[1]!=0 or d%list[2]!=0 :
  d += 1

print(d)
