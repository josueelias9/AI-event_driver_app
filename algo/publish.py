
import redis
import time
r = redis.Redis(host='localhost', port=6379, db=0)
lista = [
    "esta es una lista",
    "donde podras ver varios mensajes",
    "que seran enviados a la cola.",
    "Practiquemos!!!"
]
while True:
    for i in lista:
        r.publish('publi',i)
        print(i)
        time.sleep(1)
    




