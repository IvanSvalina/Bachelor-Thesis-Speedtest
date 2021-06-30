#from . import speedtest

import json
import datetime
from json import dumps
from django import speedtest
from django.core import serializers
from django.http import response
from django.http.response import JsonResponse
from travello.models import Measurement
from django.shortcuts import render
from .models import Measurement
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def history(request):
    m=Measurement.objects.all()
    return render(request,'history.html',{'m':m})

def getalldatahistory(request):
    #json_data = serializers.serialize("json", m)
    #dumps_json_data = dumps(json_data)  
    if(request.is_ajax()):
        m=Measurement.objects.all()
        json_data = list(m.values())
        response={'json_data':json_data}
        return JsonResponse(response)   
    return render(request,'history.html',{'data':1})


def getdaydatahistory(request):
    #json_data = serializers.serialize("json", m)
    #dumps_json_data = dumps(json_data)  
    if(request.is_ajax()):
        m=Measurement.objects.all()
        dict = list(m.values())
        json_data=[]
        for x in dict:
            if((datetime.datetime.now()-datetime.timedelta(days=1))<x['date_time']):
                pom={}
                pom['id']=x['id']
                pom['network']=x['network']
                pom['date_time']=x['date_time']
                pom['u_speed']=x['u_speed']
                pom['d_speed']=x['d_speed']
                pom['ping']=x['ping']
                json_data.append(pom)
        response={'json_data':json_data}
        return JsonResponse(response)   
    return render(request,'history.html',{'data':1})


def getweekdatahistory(request):
    #json_data = serializers.serialize("json", m)
    #dumps_json_data = dumps(json_data)  
    if(request.is_ajax()):
        m=Measurement.objects.all()
        dict = list(m.values())
        json_data=[]
        for x in dict:
            if((datetime.datetime.now()-datetime.timedelta(days=7))<x['date_time']):
                pom={}
                pom['id']=x['id']
                pom['network']=x['network']
                pom['date_time']=x['date_time']
                pom['u_speed']=x['u_speed']
                pom['d_speed']=x['d_speed']
                pom['ping']=x['ping']
                json_data.append(pom)
        response={'json_data':json_data}
        return JsonResponse(response)   
    return render(request,'history.html',{'data':1})

def getmonthdatahistory(request):
    #json_data = serializers.serialize("json", m)
    #dumps_json_data = dumps(json_data)  
    if(request.is_ajax()):
        m=Measurement.objects.all()
        dict = list(m.values())
        json_data=[]
        for x in dict:
            if((datetime.datetime.now()-datetime.timedelta(days=30))<x['date_time']):
                pom={}
                pom['id']=x['id']
                pom['network']=x['network']
                pom['date_time']=x['date_time']
                pom['u_speed']=x['u_speed']
                pom['d_speed']=x['d_speed']
                pom['ping']=x['ping']
                json_data.append(pom)
        response={'json_data':json_data}
        return JsonResponse(response)   
    return render(request,'history.html',{'data':1})




st = speedtest.Speedtest()
servernames =[]
st.get_servers(servernames)

def measureping(request):
    if(request.is_ajax()):
        best_server=st.get_best_server()
        d_speed1=st.download()
        ping1=st.results.ping
        bs=best_server['host']+', '+best_server['name']+', '+best_server['country']
        response={'number':1,'network':bs,'d_speed':d_speed1, 'ping':ping1}
        return JsonResponse(response)   
    return render(request,'index.html',{'ping':1})
    

def measureuspeed(request):
    if(request.is_ajax()):
        u_speed1=st.upload()
        #u_speed1=1
        #mj = Measurement.objects.create(number=1,network="mreza", d_speed=d_speed1, u_speed=u_speed1,
        #ping=ping)

        response={'number':1,'network':"mreza",'u_speed':u_speed1}
        return JsonResponse(response)   
    return render(request,'index.html',{'u_speed':1})  


@csrf_exempt
def deletemention(request):
    if(request.is_ajax()):
        
        body2=json.loads(request.body)
        print(body2['id'])
        Measurement.objects.filter(id=body2['id']).delete()


        response={'number':1,'network':"mreza",'u_speed':1}
        return JsonResponse(response)   
    return render(request,'history.html',{'u_speed':1})


@csrf_exempt
def savemeas(request):
    if(request.is_ajax()):
        body=json.loads(request.body)
        #d_speed=body['d_speed']
        now = datetime.datetime.now()

        mj = Measurement.objects.create(number=1,network=body['network'],
         d_speed=body['d_speed'],
        u_speed=body['u_speed'], ping=body['ping'])



        response={'number':1,'network':"mreza",'u_speed':1}
        return JsonResponse(response)   
    return render(request,'index.html',{'u_speed':1})
        

        #mj = Measurement.objects.create(number=1,network="mreza", d_speed=d_speed1, u_speed=u_speed1,
        #ping=ping)

        