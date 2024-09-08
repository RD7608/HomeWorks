from django.shortcuts import render


def class_view(request):
    return render(request, 'second_task/class_template.html')

def func_view(request):
    return render(request, 'second_task/func_template.html')