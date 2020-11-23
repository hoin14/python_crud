from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import json
from .models import USR_TIMETBL_INF


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

def postlike(request):

        customer = {
            'id' : 15,
            'name' : 'Tom',
        }
        jsonString = json.dumps(customer)

        print(jsonString)

        return render(request, 'login.html', {'id' : id})

def workinfo(requset):
    return render(requset, 'workinfo.html')

def worksearch(requset):
    if requset.method == "POST":
        search_year= requset.POST.get('searchYear', '')
        search_month = requset.POST.get('searchMonth', '')
        search_name = requset.POST.get('searchName', '')

        all = USR_TIMETBL_INF.objects.all()
        result=[]

        for usrs1 in all.filter(USRID__contains='hoin'):

            # str_split=str.split('|')

            # year = str_split.split[0]
            # starttime = str_split.split[1]
            # outtime = str_split.split[2]
            # print(year, starttime, outtime)

        usrs = USR_TIMETBL_INF.objects.all()

    return render(requset, 'workinfo.html', {'usrs': usrs})