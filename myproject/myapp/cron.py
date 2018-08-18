from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Wind,Water,WindScrapy
import requests
import time,datetime
import json
# Create your views here.

def check():
    response = {}
    try:
       #请求地址
        url = "http://58.211.227.41:10007/report/public/winddata"
       #发送get请求
        r = requests.get(url)
        u = int(str(r.json()[0].get("receivetime"))[0:10])
        timeArray = time.localtime(u)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        print(otherStyleTime)    # 2017--12--11 19:18:02
        wind = Wind(add_time=otherStyleTime,wind_level=r.json()[0].get("tdz_qnh"),wind_direction=r.json()[0].get("tdz_bl_1a"))
        wind.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def water_check():
    response = {}
    try:
       #请求地址
        url = "http://58.211.227.41:10007/report/public/depthdata"
       #发送get请求
        r = requests.get(url)
        u = int(str(r.json()[0].get("date"))[0:10])
        timeArray = time.localtime(u)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        print(otherStyleTime)    # 2017--12--11 19:18:02
        water = Water(add_time=otherStyleTime,water_high=round(r.json()[0].get("depth"),1))
        water.save()
        #print(water.water_high)
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        print(str(e))
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def wind_check():
    response = {}
    rstr = ''
    print('hello')
    try:
       #请求地址
        url = "http://www.zjg121.com/zjgqxj2/QXXX/GetInfo.ashx?title=weather&infotype=FS&station=%E9%95%BF%E6%B1%9F%E9%98%B2%E6%B1%9B%E5%A4%84"
       #发送get请求
        r = requests.get(url)
        print(r.text)
        #rstr = json.dumps(r)
        #print(rstr)
        nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
        wind = WindScrapy(add_time=nowTime,wind_level=r.text)
        wind.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        print(str(e))
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(r.text,safe=False)
