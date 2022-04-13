n = int(input())

def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
# def is_prime(x):
#     for i in range(2, (x//2)+1):
#         if x % i == 0:
#             return False
#     return True

print(IsPrime(n))

# n = int(input())
# for i in range(2, n):
#     if n % i == 0:
#         print('НЕТ')
#         break
# else:
#     if n == 1:
#         print('НЕТ')
#     else:
#         print('ДА')
#