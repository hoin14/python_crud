from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def home(requset):
    return render(requset, 'home.html')

def login(requset):
    if requset.method == "POST":
        username = requset.POST['userId']
        password = requset.POST['userPass']

        user = auth.authenticate(
            requset, username=username, password=password
        )
        if user is not None:
            auth.login(requset, user)
            print("login success!")
            return redirect('home')
        else:
            print('login error!')
            return render(requset, 'login.html',{
                'error': 'Username or Password is incorrect',
            })
    else:
        return render(requset, 'login.html')

def signup(requset):
    if requset.method == 'POST':
        user = User.objects.create_user(
            username=requset.POST['userId'],
            password=requset.POST['userPass']
        )
        auth.login(requset, user)
        print('sigun success!')
        return redirect('home')
    else:
        return render(requset, 'signup.html')

def logout(request):
        auth.logout(request)
        return redirect('home')