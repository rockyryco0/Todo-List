import json
from django.utils import timezone
from .models import ToDo
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import os


def home_todo(request):
    todo_items = ToDo.objects.all()
    return render(request, '...yourprojectpath/todo_list.html', {
      "todo_items": todo_items
    })


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = ToDo.objects.create(added_date=current_date, text=content)
    data = [str(content), str(current_date)]
    a = {}
    a["list"] = []
    try:
        open(r"...yourprojectpath\filejson\todo.json")
    except FileNotFoundError:
        open(r"...yourprojectpath\filejson\todo.json", "w")
    try:
        with open(r"...yourprojectpath\filejson\todo.json") as feedsjson:
            a = json.load(feedsjson)
        with open(r"...yourprojectpath\filejson\todo.json", mode='w+', encoding='utf-8') as feedsjson:
            entry = {'content': content, 'added_date': str(current_date)}
            a["list"].append(entry)
            json.dump(a, feedsjson, indent=4)
    except json.JSONDecodeError:
        with open(r"...yourprojectpath\filejson\todo.json", mode='w+', encoding='utf-8') as feedsjson:
            entry = {'content': content, 'added_date': str(current_date)}
            a["list"].append(entry)
            json.dump(a, feedsjson, indent=4)
    return redirect("home")


@csrf_exempt
def delete_todo(request):
    if request.method == "POST":
        id_todo = request.POST['id_todo']
        ToDo.objects.filter(id_todo=id_todo).delete()
    return redirect("home")


def history_todo(request):
    try:
        with open(r"...yourprojectpath\filejson\todo.json") as todo_json:
            json_list = json.load(todo_json)
    except FileNotFoundError:
        messages.info(request, 'No history has been made!')
        return redirect("home")
    except json.JSONDecodeError:
        messages.info(request, 'No history has been made!')
        return redirect("home")
    return render(request, '...yourprojectpath/history_todo.html', {'json_list': json_list})


def clear_history(request):
    os.remove(r"...yourprojectpath\filejson\todo.json")
    return redirect("home")
