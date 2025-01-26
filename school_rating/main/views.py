from django.shortcuts import render

def index(request):
    my_list = ['Элемент 1', 'Элемент 2', 'Элемент 3', 'Элемент 4', 'Элемент 5']
    context = {
        'my_list': my_list
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def courses(request):
    return render(request, 'main/courses.html')
