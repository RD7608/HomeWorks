def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result > 1:
            for i in range(2, result):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
