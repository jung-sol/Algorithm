n = int(input())
sum = 0
count = 0

for i in range(n):
    if sum + i >= n:
        break
    sum += i
    count += 1

idx = n - sum - 1

if count % 2 == 0:
    print(f'{idx + 1}/{count - idx}')
else:
    print(f'{count - idx}/{idx + 1}')
