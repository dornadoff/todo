from django.shortcuts import render, redirect
from .models import *
def todo(request):
    if request.method == "POST":
        Todo.objects.create(
            nomi = request.POST.get("nomi"),
            sanasi = request.POST.get("sanasi"),
            batafsil = request.POST.get("batafsil"),
            holat = request.POST.get("holat")
        )
        return redirect("/todo/")
    data = {"todo":Todo.objects.all()}
    return render(request, "todo.html", data)

def todo_ochirish(request, son):
    Todo.objects.filter(id=son).delete()
    return redirect("/todo/")

def todo_edit(request, son):
    if request.method == "POST":
        Todo.objects.filter(id=son).update(
            nomi=request.POST.get("nom"),
            sanasi = request.POST.get("sanasi"),
            batafsil = request.POST.get("batafsil"),
            holat = request.POST.get("holat")
        )
        return redirect("/todo/")

    data = {"todo":Todo.objects.get(id=son)}
    return render(request, "todo_edit.html", data)
