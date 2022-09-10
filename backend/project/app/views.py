from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import redis
import time
import json

# Create your views here.

r = redis.Redis(host='localhost', port=6379, db=0)
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
        for i in range(0,20):        
            a = p.get_message()
            if a == None:
                break
            print(a)
            print(json.dumps(a))
        #print(r.pubsub_channels())
        #print(lista)
            
        return JsonResponse({"hola":"sds"},safe=False)