from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import json, csv, time, datetime, os, sys
import pandas as pd
from .models import USR_TIMETBL_INF
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from collections import defaultdict

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST['userId']
        password = request.POST['userPass']

        user = auth.authenticate(
            request, username=username, password=password
        )
        if user is not None:
            auth.login(request, user)
            print("login success!")
            return redirect('home')
        else:
            print('login error!')
            return render(request, 'login.html',{
                'error': 'Username or Password is incorrect',
            })
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['userId'],
            password=request.POST['userPass']
        )
        auth.login(request, user)
        print('sigun success!')
        return redirect('home')
    else:
        return render(request, 'signup.html')

def logout(request):
        auth.logout(request)
        return redirect('home')

def workinfo(request):

    year = time.strftime('%Y', time.localtime(time.time()))
    month = time.strftime('%m', time.localtime(time.time()))
    day = time.strftime('%d', time.localtime(time.time()))
    Date = year + month
    DateList = []
    for i in range(1, 31):
        if i < 10:
            DateList.append(Date+ '0' + str(i))
        else:
            DateList.append(Date + str(i))
    return render(request, 'workinfo.html', {'Date' : DateList})

def addmenu(request):

    year = time.strftime('%Y', time.localtime(time.time()))
    month = time.strftime('%m', time.localtime(time.time()))
    day = time.strftime('%d', time.localtime(time.time()))
    Date = year + month
    DateList = []
    for i in range(1, 31):
        if i < 10:
            DateList.append(Date + '0' + str(i))
        else:
            DateList.append(Date + str(i))

    return render(request, 'workadd.html', {'Date': DateList})

def workadd(request):

    datas = json.loads(request.body)
    date = '20190302'
    user = 'hoin'

    # f = open('workinfo/' + date + '_' + user + '.csv', 'w', encoding='utf-8')
    # wr = csv.writer(f)
    # wr.writerow(datas)
    print("ajax Okay")

    return render(request, 'home.html')

def worksearch(request):
    if request.method == "POST":
        sYear = request.POST.get('searchYear')
        sMonth = request.POST.get('searchMonth')
        sName = request.POST.get('searchName')
        print(sYear, sMonth)

        # csv파일 읽기
        f = open('workinfo/' + sYear + sMonth + '_' + sName + '.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        workList = []
        print(rdr)
        for line in rdr:
            workList.append(line)
        f.close()
        print(workList)

    return render(request, 'workinfo.html', {'workList': workList})