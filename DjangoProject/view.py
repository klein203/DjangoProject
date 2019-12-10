from django.shortcuts import render


def hello(request):
    context = dict()
    context['hello'] = 'Hello World!'
    context['flag'] = True
    context['lst'] = [x for x in range(0, 10)]
    return render(request, 'hello.html', context)