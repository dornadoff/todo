from django.shortcuts import render
from .models import *
def todo(request):
    if request.method == "POST":
        Todo.objects.create(
            nomi = request.POST.get("nomi"),
            sanasi = request.POST.get("sanasi"),
            batafsil = request.POST.get("batafsil"),
            holat = request.POST.get("holat")
        )
    data = {"todo":Todo.objects.all()}
    return render(request, "todo.html")
