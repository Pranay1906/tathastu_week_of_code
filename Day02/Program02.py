x = -1
y = 1
n = int(input('enter nth term'))
print("Fibonacci series :",end=' ')
for i in range(1, n+1):
    a = x + y
    x = y
    y = a
    print(a,end=' ')
