def test(*args):
    for i in range(len(args)):
        print("Аргумент", i, '=', args[i])

test(10, "строка", 55, [5, 4, 3], False)


# функция факториал
def factor(n):
    if n == 1:
        return 1
    return factor(n - 1) * n


a = 10
print(str(a)+"!=", factor(a))