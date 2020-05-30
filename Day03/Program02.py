def String(List):
    return ''.join(List)
def Permute(a, l, r):
    if l == r:
        print(String(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            Permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]



string = "ABC"
n = len(string)
a = list(string)
Permute(a, 0, n - 1)
