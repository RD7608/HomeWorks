from django.shortcuts import render


def index(request):
    return render(request, 'fourth_task/index.html')

def shop(request):
    context = {'water': ['Бутыль 19 л', 'Бутыль 5 л 4 шт', 'Бутылка 1,5 л 12 шт']}
    return render(request, 'fourth_task/shop.html', context)

def cart(request):
    return render(request, 'fourth_task/cart.html')
