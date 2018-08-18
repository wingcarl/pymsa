from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Wind,Water,Weather,WindScrapy
import requests
import time,datetime
import json
import demjson
import re
from datetime import date
from datetime import datetime
from datetime import timedelta

# Create your views here.

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)
 
@require_http_methods(["GET"])
def add_wind(request):
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

@require_http_methods(["GET"])
def show_wind(request):
    response = {}
    jsdata = []
    try:
        winds = Wind.objects.all().order_by("-add_time")[:30]
        for item in reversed(winds):
            #print(item.add_time)
            wind_data={}
            wind_data["x"] = item.add_time.strftime("%Y/%m/%d %H:%M:%S")
            wind_data["y"]  = item.wind_level
            jsdata.append(wind_data)
        #response['list']  = json.loads(serializers.serialize("json", books))
        #response['msg'] = 'success'
        #response['error_num'] = 0
    except  Exception as e:
        print(str(e))
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(jsdata,safe=False)

@require_http_methods(["GET"])
def show_wind_level(request):
    response = {}
    jsdata = []
    wind_str = '实时风力 '
    try:
        winds = Wind.objects.all().order_by("-add_time")[:1]
        winds_sc = WindScrapy.objects.all().order_by("-add_time")[:1]
        for item in reversed(winds):
            wind_speed  = item.wind_level
            wind_l = get_wind_level(float(wind_speed))
            wind_str = wind_str+'港务局：'+str(wind_l)+'级风 '
        for item in winds_sc:
            wind_speed = item.wind_level
            djson = demjson.decode(wind_speed)
            wind_lr = djson[-1].get('ReData')
            wind_l = get_wind_level(float(wind_lr))
            wind_str = wind_str+'长江防汛处：'+str(wind_l)+'级风'
        #response['list']  = json.loads(serializers.serialize("json", books))
        #response['msg'] = 'success'
        #response['error_num'] = 0
    except  Exception as e:
        print(str(e))
        response['msg'] = str(e)
        response['error_num'] = 1
    response['value']=wind_str
    response['url'] = ''
    jsdata.append(response)
    return JsonResponse(jsdata,safe=False)

def get_wind_level(wind_speed):
    if wind_speed>=0 and wind_speed<=0.2:
        return 0
    elif wind_speed>=0.3 and wind_speed<1.6:
        return 1
    elif wind_speed>=1.6 and wind_speed<3.4:
        return 2
    elif wind_speed>=3.4 and wind_speed<5.5:
        return 3
    elif wind_speed>=5.5 and wind_speed<8.0:
        return 4
    elif wind_speed>=8.0 and wind_speed<10.8:
        return 5
    elif wind_speed>=10.8 and wind_speed<13.9:
        return 6
    elif wind_speed>=13.9 and wind_speed<17.2:
        return 7
    elif wind_speed>=17.2 and wind_speed<20.8:
        return 8
    elif wind_speed>=20.8 and wind_speed<24.5:
        return 9
    elif wind_speed>=24.5 and wind_speed<28.5:
        return 10
    elif wind_speed>=28.5 and wind_speed<32.6:
        return 11
    elif wind_speed>=32.6 and wind_speed<37.0:
        return 12
    elif wind_speed>=37.0 and wind_speed<41.5:
        return 13
    elif wind_speed>=41.5 and wind_speed<=46.1:
        return 14
    elif wind_speed>=46.2 and wind_speed<=50.9:
        return 15
    elif wind_speed>=51.0 and wind_speed<=56.0:
        return 16
    elif wind_speed>=56.1 and wind_speed<=61.2:
        return 17
    elif wind_speed>=61.3:
        return 18

@require_http_methods(["GET"])
def show_wind_scrapy(request):
    response = {}
    jsdata = []
    try:
        winds = WindScrapy.objects.all().order_by("-add_time")[:1]
        #wind_json = json.loads(winds)
        #print(winds[0].wind_level)
        #print(wind_json[0])
        for item in reversed(winds):
            #print(item.wind_level)
            djson = demjson.decode(item.wind_level)
            print(djson)
            #wind_json = json.loads(djson)
            #print(djson[0])
            newday = False
            for dj in djson:
                hour = dj.get('Hour')
                re_data = dj.get('ReData')
                curdate = date.today()
                lastday = curdate + timedelta(days=-1)
                wind_data={}
                if hour==0:
                    newday = True
                if newday:
                    dt = datetime(curdate.year,curdate.month,curdate.day,hour,0,0)
                    wind_data["x"]=dt.strftime("%Y/%m/%d %H:%M:%S")
                else:
                    dt = datetime(lastday.year,lastday.month,lastday.day,hour,0,0)
                    wind_data["x"]=dt.strftime("%Y/%m/%d %H:%M:%S")
                wind_data["y"]=re_data
                jsdata.append(wind_data)
            #wind_data={}
            #wind_data["x"] = item.add_time.strftime("%Y/%m/%d %H:%M:%S")
            #wind_data["y"]  = item.wind_level
            #jsdata.append(wind_data)
        #response['list']  = json.loads(serializers.serialize("json", books))
        #response['msg'] = 'success'
        #response['error_num'] = 0
    except  Exception as e:
        print(str(e))
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(jsdata,safe=False)

@require_http_methods(["GET"])
def show_water(request):
    response = {}
    jsdata = []
    try:
        waters = Water.objects.all().order_by("-add_time")[:30]
        for item in reversed(waters):
            #print(item.add_time)
            water_data={}
            water_data["x"] = item.add_time.strftime("%Y/%m/%d %H:%M:%S")
            water_data["y"]  = item.water_high
            jsdata.append(water_data)
        #response['list']  = json.loads(serializers.serialize("json", books))
        #response['msg'] = 'success'
        #response['error_num'] = 0
    except  Exception as e:
        print(str(e))
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(jsdata,safe=False)

@require_http_methods(["GET"])
def show_weather(request):
    response = {}
    jsdata = []
    try:
        weathers = Weather.objects.all().order_by("-add_time")[:1]
        for item in reversed(weathers):
            #print(item.add_time)
            weather_data={}
            #water_data["x"] = item.add_time.strftime("%Y/%m/%d %H:%M:%S")
            weather_str = item.weather_detail
            #print(type(weather_str))
            weather_chn = weather_str.encode('utf-8').decode()
            #print(bytes(weather_str).decode())

            #print(bytes(item.weather_detail).decode('utf-8'))
            weather_data["value"]  = weather_chn
            jsdata.append(weather_data)
        #response['list']  = json.loads(serializers.serialize("json", books))
        #response['msg'] = 'success'
        #response['error_num'] = 0
    except  Exception as e:
        print(str(e))
        response['msg'] = str(e)
        response['error_num'] = 1
    output = json.dumps(jsdata,ensure_ascii=False)
    print(output)
    return HttpResponse(output)

@require_http_methods(["GET"])
def show_weather_alert(request):
    response = {}
    jsdata = []
    alert_str = '大风预警：'
    try:
        weathers = Weather.objects.all().order_by("-add_time")[:1]
        for item in reversed(weathers):
            #print(item.add_time)
            weather_data={}
            #water_data["x"] = item.add_time.strftime("%Y/%m/%d %H:%M:%S")
            weather_str = item.weather_detail
            #print(type(weather_str))
            weather_chn = weather_str.encode('utf-8').decode()
            levels = re.findall(r"\d+级",weather_chn)
            it = levels[-1]
            if it=='7级' or it=='8级' or it=='9级':
                alert_str = alert_str+'三级预警'
            elif it=='10级' or it=='11级':
                alert_str = alert_str+'二级预警'
            else:
                alert_str = '暂无预警'
            #print(bytes(weather_str).decode())

            #print(bytes(item.weather_detail).decode('utf-8'))
            weather_data["value"]  = alert_str
            #jsdata.append(alert_str)
        #response['list']  = json.loads(serializers.serialize("json", books))
        #response['msg'] = 'success'
        #response['error_num'] = 0
    except  Exception as e:
        print(str(e))
        response['msg'] = str(e)
        response['error_num'] = 1
    output = json.dumps(jsdata,ensure_ascii=False)
    response['value'] = alert_str
    response['url'] = ''
    jsdata.append(response)
    return JsonResponse(jsdata,safe=False)

require_http_methods(["GET"])
def wind_check(request):
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
