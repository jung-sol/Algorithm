n = input()
data = n.split('-')
result = []

for i in data:
  sum = 0
  for j in i.split('+'):
    sum += int(j)
  result.append(str(sum))
  
print(eval('-'.join(result)))
