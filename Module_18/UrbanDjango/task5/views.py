from django.shortcuts import render
from .forms import RegistrationForm


# Cписок существующих пользователей
existing_users = ["user", "user1", "admin"]

def sign_up_by_django(request):
    info = {}

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']


            if username in existing_users:
                info['error'] = "Пользователь с таким именем уже существует."
            elif password != repeat_password:
                info['error'] = "Пароли не совпадают."
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                existing_users.append(username)
                info['success'] = f'Приветствуем, {username}!'
        else:
            info['error'] = "Ошибка в обработке формы."
    else:
        form = RegistrationForm()


    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_html(request):
    info = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        # Проверка существования пользователя
        if username in existing_users:
            info['error'] = "Пользователь с таким именем уже существует."
        elif password != repeat_password:
            info['error'] = "Пароли не совпадают."
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            # Регистрация и добавление пользователя
            existing_users.append(username)
            info['success'] = f'Приветствуем, {username}!'
    else:
        info['form'] = {}
    return render(request, 'fifth_task/registration_page.html', context=info,)