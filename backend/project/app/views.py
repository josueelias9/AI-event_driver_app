from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import redis
import time
import json

# Create your views here.

r = redis.Redis(host='redis-app', port=6379, db=0)
p = r.pubsub()
p.subscribe("publi")

class Home(View):    
    def get(self, request, *args, **kwargs):
        age = request.GET.get('age')
        name = request.GET.get('name')
        data = {
            "age":age,
            "name":name
        }
        return JsonResponse(data)

class Dos(View):
    def get(self, request, *args, **kwargs):
        lista = []
        for i in range(0,100):        
            a = p.get_message()
            if a == None:
                break
            # decodificamos los datos binarios
            a['data'] = a['data'].decode('utf-8')
            a['channel'] = a['channel'].decode('utf-8')
            lista.append(a)

        #print(r.pubsub_channels()[0])
        #print(lista)
        #return HttpResponse("hola")   
        return JsonResponse(lista,safe=False)