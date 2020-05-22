n = 6
for i in range(n-1, 0, -1):
    print("*" * i + ' ' * (n-1 - i)*2 + '*' * i)
for i in range(1,n):
    print("*" * i + ' ' * (n-1 - i)*2 + '*' * i)
