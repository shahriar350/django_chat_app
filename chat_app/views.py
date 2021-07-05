from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from chat_app.forms import UserForm


def cantor_pairing(num1, num2):
    if num1 > num2:
        result = int((((num1 + num2) * (num1 + num2 + 1)) / 2) + num2)
    else:
        result = int((((num2 + num1) * (num2 + num1 + 1)) / 2) + num1)
    return result


@login_required(login_url='/login/')
def chat_view(request):
    users = list(User.objects.exclude(username=request.user.username))
    arr = []
    for user in users:
        temp = {'name': user.username, 'room': cantor_pairing(user.id,request.user.id)}
        arr.append(temp)
    return render(request, 'index.html', {'users': arr})


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(form.cleaned_data.get('username'), form.cleaned_data.get('email'),
                                     form.cleaned_data.get('password'))
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserForm()
    return render(request, 'auth/registration.html', {'form': form})


def login_set(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            raise ValidationError('Please provide valid username and password.')
    return render(request, 'auth/login.html', {})


@login_required(login_url='/login/')
def message_id(request, user_id=None):
    users = list(User.objects.exclude(username=request.user.username))
    arr = []
    for user in users:
        temp = {'name': user.username, 'room': cantor_pairing(user.id, request.user.id)}
        arr.append(temp)
    return render(request, 'chat_app.html', {'users': arr, 'room_name': user_id})
