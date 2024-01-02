data = list(input())
result = 0
temp = []

for i in range(len(data)):
    if data[i] == '(':
        temp.append('(')

    else:
        if data[i-1] == '(': 
            temp.pop()
            result += len(temp)

        else:
            temp.pop() 
            result += 1 
            
print(result)
