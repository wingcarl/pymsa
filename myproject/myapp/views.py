from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Wind
import requests
import time
# Create your views here.
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

