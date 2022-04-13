n = int(input())
f1, f2 = 1, 1
print(f1, f2, end=' ')
while n > 2:
    f1, f2 = f2, f1 + f2
    n = n - 1
    print(f2, end=' ')
