m = int(input(), 16)

for i in range(1, 16):
  print('%X'%m, '*%X'%i, '=%X'%(m*i), sep='')
