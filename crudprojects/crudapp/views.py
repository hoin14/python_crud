from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import json
import csv
import time
import datetime
import pandas as pd
from .models import USR_TIMETBL_INF
from django.http import HttpResponse

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

    year = time.strftime('%Y', time.localtime(time.time()))
    month = time.strftime('%m', time.localtime(time.time()))
    day = time.strftime('%d', time.localtime(time.time()))
    Date = year + '-' + month + '-'
    DateList = []
    DayList = []
    for i in range(1, 31):
        DateList.append(Date+ str(i))
        DayList.append(str(i))
    return render(requset, 'workinfo.html', {'Date' : DateList, 'Day' : DayList})

def workadd(requset):
    if requset.method == "POST":
        sTime = requset.POST.get('startTime', '')
        eTime = requset.POST.get('endTime', '')
        user = requset.POST.get('user', '')
        sTimeArray = [];
        sTimeArray = requset.getParameterValues("startTime");

        print(sTimeArray)
        print(eTime)
        print(user)
        # #csv파일 쓰기
        # f = open('workinfo/' + date + '_' + user + '.csv', 'w', encoding='utf-8', newline='')
        # wr = csv.writer(f)
        # wr.writerow([date, sTime, dTime])
        # f.close()
        # print(f)
    return render(requset, 'home.html')

def worksearch(requset):
    if requset.method == "POST":
        sYear = requset.POST.get('searchYear')
        sMonth = requset.POST.get('searchMonth')
        sName = requset.POST.get('searchName')
        print(sYear, sMonth)

        # csv파일 읽기
        f = open('workinfo/' + sYear + sMonth + '_' + sName + '.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        workList = []
        for line in rdr:
            workList.append(line)
        f.close()
        print(workList)

    return render(requset, 'workinfo.html', {'workList': workList})

def favorites(request):
    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "NOT AJAX"
    return HttpResponse(message)