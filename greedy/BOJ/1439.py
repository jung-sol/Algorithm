n = input()
cnt = 0

for i in range(1, len(n)):
  if n[i] != n[i - 1]:
    cnt += 1
    
print((cnt+1)//2)
