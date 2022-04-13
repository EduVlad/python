# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst = []
# здесь продолжайте программу (используйте список lst_in)
for i in lst_in:
    while i.count('  '):
        i = i.replace('  ', ' ')
    print(i)