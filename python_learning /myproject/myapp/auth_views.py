from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here.


def my_login(request):

    if request.method == 'POST':
        user_name = request.POST["user_name"]
        password = request.POST["password"]
        user = authenticate(request, username=user_name, password=password)
        print("user_name is", user_name)
        print("password is", password)
        print("user is", user)

        if user is not None:
            print("success!")
            login(request, user)
            return redirect('/')
        print("fail!")
    return render(request, 'examples/login.html')

# @login_required(login_url='/login/')
def my_logout(request):
        logout(request)
        print("logged out")
        return redirect('/login/')

