from django.shortcuts import render
from .models import *
from .forms import *

Buyers = Buyer.objects.all()

existing_users = []
for each in Buyers:
    existing_users.append(each.name)

def index(request):
    return render(request, 'task1/index.html')


def shop(request):
    Games = Game.objects.all()
    context = {
        'Games': Games,
    }
    return render(request, 'task1/shop.html', context)


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