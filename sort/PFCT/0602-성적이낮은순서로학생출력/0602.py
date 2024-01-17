n = int(input())

arr = []

for _ in range(n):
    data = input().split()
    arr.append((data[0], int(data[1]))) # 튜플 형태
    
arr = sorted(arr, key=lambda student: student[1])

for student in arr:
    print(student[0], end = ' ')
