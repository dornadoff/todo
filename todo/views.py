from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
def todo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            Todo.objects.create(
                nomi = request.POST.get("nomi"),
                sanasi = request.POST.get("sanasi"),
                batafsil = request.POST.get("batafsil"),
                holat = request.POST.get("holat"),
                user = request.user
            )
            return redirect("/todo/")
        data = {"todo":Todo.objects.filter(user=request.user)}
        return render(request, "todo.html", data)
    return redirect("/")

def todo_ochirish(request, son):
    pl = Todo.objects.get(id=son)
    if pl.user == request.user:
        pl.delete()
    return redirect("/todo/")

def todo_edit(request, son):
    if request.method == "POST":
        Todo.objects.filter(id=son).update(
            nomi=request.POST.get("nom"),
            sanasi = request.POST.get("sanasi"),
            batafsil = request.POST.get("batafsil"),
            holat = request.POST.get("holat"),
        )
        return redirect("/todo/")

    data = {"todo":Todo.objects.get(id=son)}
    return render(request, "todo_edit.html", data)

def loginview(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get("username"),
                     password=request.POST.get("password"))
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/todo")

    return render(request, "login.html")

def logoutview(request):
    logout(request)

    return redirect("/")

def register(request):
    if request.method == "POST" and request.POST.get("p") == request.POST.get("cp"):
        User.objects.create_user(
            username = request.POST.get('l'),
            password = request.POST.get("p")
        )
        return redirect("/")
    return render(request, "register.html")
