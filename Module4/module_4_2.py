def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


# Вызов функции test_function
test_function()

# Попытка вызова inner_function вне функции test_function
# inner_function()

# При попытке вызова inner_function вне функции test_function возникнет ошибка,
# так как inner_function определена только внутри test_function.
