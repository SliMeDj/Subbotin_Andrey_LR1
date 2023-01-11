from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title':'Главная страница сайта', 'tasks':tasks})

def about(request):
    return render(request, 'main/about.html')

def nineCLASS(request):
    return render(request, 'main/nineCLASS.html')

def elevenCLASS(request):
    return render(request, 'main/elevenCLASS.html')

def contact(request):
    return render(request, 'main/contact.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def vpr(request):
    return render(request, 'main/vpr.html')