n= int(input("enter number"))
for i in range(n,0,-1):
    print(f"{i}*"*(i-1)+f'{i}')
for i in range(2,n+1):
    print(f"{i}*"*(i-1)+f'{i}')
