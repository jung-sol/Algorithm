n = int(input())

for _ in range(n):
  s = int(input())
  print(s//25, (s%25)//10, ((s%25)%10)//5, ((s%25)%10)%5)
