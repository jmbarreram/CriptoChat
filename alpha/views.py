from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from chat_app import settings

from .models import Chat

def Create_User(request):
    next = request.GET.get('next', '/login/')
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if username is not None and email is not None and password is not None:
            user = User.objects.create_user(username,email,password)
            user.save()
            return HttpResponseRedirect('/login/')
        return HttpResponse("User, email or password missing.")
    return render(request, "alpha/create_user.html", {'next': next})

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "alpha/login.html", {'next': next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def Home(request):
    c = Chat.objects.all()
    return render(request, "alpha/home.html", {'home': 'active', 'chat': c})

def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

def Messages(request):
    c = Chat.objects.all()
    return render(request, 'alpha/messages.html', {'chat': c})
