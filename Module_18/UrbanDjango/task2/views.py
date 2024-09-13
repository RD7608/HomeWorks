from django.shortcuts import render
from django.views import View

class ClassView(View):
    template_name = 'second_task/class_template.html'

    def get(self, request):
        return render(request, self.template_name)


def func_view(request):
    return render(request, 'second_task/func_template.html')