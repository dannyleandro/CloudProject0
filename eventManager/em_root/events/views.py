from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Event, AddEventForm
from django.core import serializers


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return render(request, "login.html")


def get_events(request):
    events_list = Event.objects.all()
    return HttpResponse(serializers.serialize("json", events_list))


@csrf_exempt
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            render(request, "index.html")
        else:
            mensaje = "Nombre de usuario o clave no valido"
        return JsonResponse({"mensaje": mensaje})
    else:
        return render(request, "login.html")


@csrf_exempt
def logoutView(request):
    logout(request)
    return JsonResponse({"mensaje": 'ok'})


@csrf_exempt
def is_logged_view(request):
    if request.user.is_authenticated:
        mensaje = 'ok'
    else:
        mensaje = 'no'

    return JsonResponse({"mensaje": mensaje})


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email

        user_model.save()
        return HttpResponse(serializers.serialize('json', [user_model]))
    else:
        return render(request, "registro.html")


def get_user_view(request):
    if request.user.is_authenticated:
        return JsonResponse({"username": request.user.username,
                             "first_name": request.user.first_name,
                             "last_name": request.user.last_name,
                             "email": request.user.email})
    else:
        return JsonResponse({"username": ''})


def add_event_view(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            event = form.save()
            event.usuario = request.user
            event.save()
        return render(request, 'addEvent.html')
    else:
        form = AddEventForm()
        context = {"AddEventForm": AddEventForm}
    return render(request, 'AddEvent.html', context)
