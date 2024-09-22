from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from .forms import *

# Buyers = Buyer.objects.all()

# existing_users = []
# for each in Buyers:
#    existing_users.append(each.name)

existing_users = set(Buyer.objects.values_list('name', flat=True))  # Список всех пользователей


def index(request):
    return render(request, 'task1/index.html')


def shop(request):
    page_size = request.GET.get('page_size', '3')  # Получение размера страницы
    games = Game.objects.all().order_by('id')  # Все игры, отсортированные по id

    if page_size == 'all':
        page_obj = games
    else:
        try:
            page_size = int(page_size)  # Преобразование в целое число
        except (ValueError, TypeError):
            page_size = 3  # Значение по умолчанию в случае ошибки

        paginator = Paginator(games, page_size)  # Пагинация с размером страницы
        page_number = request.GET.get('page', 1)  # Номер страницы
        page_obj = paginator.get_page(page_number)  # Пагинация

    context = {
        'page_obj': page_obj,
        'page_size': page_size,
    }
    return render(request, 'task1/shop.html', context=context)


def cart(request):
    return render(request, 'task1/cart.html')


def sign_up(request):
    info = {}

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            #            password = form.cleaned_data['password']
            #            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in existing_users:
                info['error'] = "Пользователь с таким именем уже существует."
            #            elif password != repeat_password:
            #                info['error'] = "Пароли не совпадают."
            #            elif age < 18:
            #                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, age=age)
                info['success'] = f'Приветствуем, {username}!'
        else:
            info['error'] = "Ошибка в обработке формы."
    else:
        form = RegistrationForm()

    info['form'] = form
    return render(request, 'task1/registration_page.html', context=info)
