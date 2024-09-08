def find_password(first_number):
    password = ""
    for i in range(1, first_number+1):
        for j in range(i+1, first_number+1):
            if first_number % (i + j) == 0:
                password += str(i) + str(j)
    return password


while True:
    user_input = input("Введите число от 17_3 до 20 чтобы получить пароль, или введите 'q' для выхода: ")
    if user_input.lower() == 'q':
        print("Вы вышли из программы")
        break
    else:
        user_input = int(user_input)
    if user_input < 3 or user_input > 20:
        print("Число должно быть от 17_3 до 20")
        continue
    print(user_input,"-", find_password(user_input))
