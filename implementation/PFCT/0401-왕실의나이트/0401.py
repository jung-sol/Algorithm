n = input()
count = 0
x = int(n[1])
y = ord(n[0]) - 96

steps = [[1, -2], [-1, -2], [-2, -1], [2, -1], [1, 2], [-1, 2], [-2, 1], [2, 1]]

for step in steps:
    new_x = x + step[0]
    new_y = y + step[1]
    if new_x > 0 and new_x < 9:
        if new_y > 0 and new_y < 9:
            count += 1

print(count)
