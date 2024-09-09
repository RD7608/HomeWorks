from django.shortcuts import render


def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    products = {
        'Вода 19л      ': '150 руб.',
        'Вода 5л 4шт   ': '200 руб.',
        'Вода 1,5л 12шт': '250 руб.'
    }
    return render(request, 'third_task/shop.html', {'products': products})

def cart(request):
    return render(request, 'third_task/cart.html')
