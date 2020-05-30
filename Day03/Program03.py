z = input(('Enter a String:'))
x=list(z)
for i in range(len(x)):
    for j in range(i+1, len(x)):
        if x[i] == x[j]:
            x[i]=""

print(''.join(x))
