n = int(input('Enter a number:'))
if n%2==0:
    print("* even")
else:
    print("* odd")
    
# ***********************************************

if n>1:
    for i in range(2, n):
        if n % i == 0:
            print(f'* {n} is not prinme number')
            break
    else:
        print(f"* {n} is prime number")
else:
    print(f'* {n} is not prinme number')


# ********************************************
n=str(n)
s = 0
# x= input('Entere a number')
for i in range(len(n)):
    y = n[i]
    p = int(y)
    z = p ** 3
    s = s + z
if s == int(n):
    print("* It's  Armstrong Number")
else:
    print("* It's not Armstrong Number")

# **********************************************

s = 0
for i in range(len(n) // 2):
    if n[i] != n[-i - 1]:
        print('* Not palandron')
        break
    else:
        s = s
if s == len(n) // 2:
    print('* Its palandrom')
