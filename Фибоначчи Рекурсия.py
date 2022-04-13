def fib(n: int) -> list:
    if n == 0:
        return [1]
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    lst = fib(n-1)
    lst.append(lst[-1] + lst[-2])
    return lst

print(*fib(8))
